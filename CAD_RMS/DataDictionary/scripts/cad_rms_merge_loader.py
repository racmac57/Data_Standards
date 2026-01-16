"""
CAD-RMS Merge Loader with Multi-Column Matching Strategies

This module implements the CAD-RMS merge workflow using the mapping schemas
defined in CAD_RMS/DataDictionary/current/schema/

Assumptions:
- Mapping JSON at: CAD_RMS/DataDictionary/current/schema/cad_to_rms_field_map.json
- Uses pandas and rapidfuzz for matching
"""

import json
from datetime import datetime, date
from pathlib import Path
from typing import Dict, Tuple, Optional

import pandas as pd
from rapidfuzz import fuzz

# -------------------------------------------------------------------
# Config
# -------------------------------------------------------------------

BASE_PATH = Path("C:/Users/carucci_r/OneDrive - City of Hackensack")
CAD_PATH = BASE_PATH / "05_EXPORTS/_CAD/full_year/2025/2025_Yearly_CAD.xlsx"
RMS_PATH = BASE_PATH / "05_EXPORTS/_RMS/full_year/2025/2025_Yearly_RMS.xlsx"

MAPPING_JSON = Path(
    "CAD_RMS/DataDictionary/current/schema/cad_to_rms_field_map.json"
)

# -------------------------------------------------------------------
# Helpers: normalization
# -------------------------------------------------------------------

def normalize_case_number(value: object) -> str:
    """Normalize case / report numbers (ReportNumberNew, Case Number)."""
    if pd.isna(value):
        return ""
    s = str(value).strip()
    s = " ".join(s.split())  # collapse internal whitespace
    s = "".join(ch for ch in s if ch.isprintable())
    return s.upper()  # case-insensitive comparison

def normalize_address(addr: object) -> str:
    """Very simple address normalization; you can plug in your own."""
    if pd.isna(addr):
        return ""
    s = str(addr).upper().strip()
    # basic punctuation removal
    for ch in [",", ".", "#"]:
        s = s.replace(ch, " ")
    s = " ".join(s.split())
    # TODO: optional: normalize street suffixes using a lookup table
    return s

def parse_time(value, fmt=None):
    """Parse time values with fallback handling."""
    if pd.isna(value):
        return None
    if isinstance(value, datetime):
        return value
    if isinstance(value, date):
        return datetime.combine(value, datetime.min.time())
    if fmt:
        try:
            return datetime.strptime(str(value), fmt)
        except ValueError:
            pass
    # fallback: let pandas parse
    try:
        return pd.to_datetime(value)
    except:
        return None

# -------------------------------------------------------------------
# Load mapping JSON (structure-aware but tolerant)
# -------------------------------------------------------------------

def load_mapping(path: Path) -> dict:
    """Load the mapping JSON schema."""
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

# You can extend this if you want to drive behavior dynamically from JSON
mapping_spec = load_mapping(MAPPING_JSON)

# -------------------------------------------------------------------
# Strategy implementations
# -------------------------------------------------------------------

def score_temporal_address(cad_row, rms_row) -> float:
    """
    Strategy 2: Temporal + Address.
    Fields:
      CAD: TimeofCall, FullAddress2
      RMS: IncidentDate, IncidentTime, FullAddress
    """
    scores = []

    # Date match (weight 0.4)
    cad_dt = parse_time(cad_row["TimeofCall"])
    rms_date = parse_time(rms_row["IncidentDate"])
    if rms_date:
        rms_date = rms_date.date()

    if cad_dt is None or rms_date is None:
        return 0.0

    cad_date = cad_dt.date()
    date_score = 1.0 if cad_date == rms_date else 0.0
    scores.append(date_score * 0.4)

    # Time match (weight 0.3, within 60 min)
    rms_time = parse_time(rms_row["IncidentTime"], fmt="%H:%M")
    if rms_time is None:
        return 0.0
    if isinstance(rms_time, datetime):
        rms_time = rms_time.time()
    elif isinstance(rms_time, str):
        # Try parsing as time string
        try:
            rms_time = datetime.strptime(rms_time, "%H:%M").time()
        except:
            return 0.0

    cad_time = cad_dt.time()
    cad_dt_comb = datetime.combine(date.today(), cad_time)
    rms_dt_comb = datetime.combine(date.today(), rms_time)
    diff_min = abs((cad_dt_comb - rms_dt_comb).total_seconds() / 60.0)
    time_score = max(0.0, 1.0 - diff_min / 60.0)
    scores.append(time_score * 0.3)

    # Address similarity (weight 0.3, threshold 0.85)
    cad_addr = normalize_address(cad_row["FullAddress2"])
    rms_addr = normalize_address(rms_row["FullAddress"])

    addr_sim = fuzz.ratio(cad_addr, rms_addr) / 100.0
    if addr_sim < 0.85:
        return 0.0

    scores.append(addr_sim * 0.3)

    return sum(scores)

def score_officer_temporal(cad_row, rms_row) -> float:
    """
    Strategy 3: Officer + Temporal.
    Fields:
      CAD: Officer, TimeofCall
      RMS: OfficerOfRecord, IncidentDate, IncidentTime
    """
    scores = []

    # Officer normalization (very simple; plug in Assignment_Master lookup if desired)
    cad_off = str(cad_row["Officer"]).upper().strip() if not pd.isna(cad_row["Officer"]) else ""
    rms_off = str(rms_row["OfficerOfRecord"]).upper().strip() if not pd.isna(rms_row["OfficerOfRecord"]) else ""

    officer_match = 1.0 if cad_off and cad_off == rms_off else 0.0
    scores.append(officer_match * 0.5)

    cad_dt = parse_time(cad_row["TimeofCall"])
    rms_date = parse_time(rms_row["IncidentDate"])
    if rms_date:
        rms_date = rms_date.date()
    rms_time = parse_time(rms_row["IncidentTime"], fmt="%H:%M")
    if rms_time and isinstance(rms_time, datetime):
        rms_time = rms_time.time()
    elif rms_time and isinstance(rms_time, str):
        try:
            rms_time = datetime.strptime(rms_time, "%H:%M").time()
        except:
            rms_time = None

    if cad_dt is None or rms_date is None or rms_time is None:
        return 0.0

    cad_date = cad_dt.date()
    date_score = 1.0 if cad_date == rms_date else 0.0
    scores.append(date_score * 0.3)

    cad_time = cad_dt.time()
    cad_dt_comb = datetime.combine(date.today(), cad_time)
    rms_dt_comb = datetime.combine(date.today(), rms_time)
    diff_min = abs((cad_dt_comb - rms_dt_comb).total_seconds() / 60.0)

    # 2-hour (120 min) window
    time_score = max(0.0, 1.0 - diff_min / 120.0)
    scores.append(time_score * 0.2)

    return sum(scores)

def score_address_zone_approx_date(cad_row, rms_row) -> float:
    """
    Strategy 4: Address + Zone + Approx Date.
    Fields:
      CAD: FullAddress2, ZoneCalc, (optional TimeofCall)
      RMS: FullAddress, Zone, (optional IncidentDate)
    """
    scores = []

    # Address similarity (0.5, threshold 0.90)
    cad_addr = normalize_address(cad_row["FullAddress2"])
    rms_addr = normalize_address(rms_row["FullAddress"])
    addr_sim = fuzz.ratio(cad_addr, rms_addr) / 100.0
    if addr_sim < 0.90:
        return 0.0
    scores.append(addr_sim * 0.5)

    # Zone exact match (0.3)
    cad_zone = str(cad_row["ZoneCalc"]).strip() if not pd.isna(cad_row["ZoneCalc"]) else ""
    rms_zone = str(rms_row["Zone"]).strip() if not pd.isna(rms_row["Zone"]) else ""
    zone_score = 1.0 if cad_zone and cad_zone == rms_zone else 0.0
    scores.append(zone_score * 0.3)

    # Approximate date (0.2, within 7 days), optional
    cad_dt = parse_time(cad_row.get("TimeofCall"))
    rms_date = parse_time(rms_row.get("IncidentDate"))
    if rms_date:
        rms_date = rms_date.date()
    
    if cad_dt is not None and rms_date is not None:
        diff_days = abs((cad_dt.date() - rms_date).days)
        date_score = max(0.0, 1.0 - diff_days / 7.0)
        scores.append(date_score * 0.2)
    else:
        # If date is missing, rescale weights for addr + zone only
        # addr: 0.5 / 0.8 = 0.625, zone: 0.3 / 0.8 = 0.375
        return addr_sim * 0.625 + zone_score * 0.375

    return sum(scores)

# -------------------------------------------------------------------
# High-level merge workflow
# -------------------------------------------------------------------

def merge_cad_rms(cad_df: pd.DataFrame, rms_df: pd.DataFrame) -> pd.DataFrame:
    """
    Merge CAD and RMS dataframes using primary key first, then alternative strategies.
    
    Returns merged dataframe with:
    - merge_match_flag: boolean indicating if match was found
    - merge_confidence_score: float confidence score (0.0-1.0)
    - merge_matching_strategy: string indicating which strategy was used
    """
    # 1. Primary key match on normalized case number
    cad_df = cad_df.copy()
    rms_df = rms_df.copy()

    # Get field names from mapping spec
    cad_key_field = mapping_spec["join_keys"]["primary"]["cad_source_field_name"]
    rms_key_field = mapping_spec["join_keys"]["primary"]["rms_source_field_name"]

    cad_df["_key_norm"] = cad_df[cad_key_field].apply(normalize_case_number)
    rms_df["_key_norm"] = rms_df[rms_key_field].apply(normalize_case_number)

    merged = cad_df.merge(
        rms_df,
        on="_key_norm",
        how="left",
        suffixes=("_cad", "_rms"),
    )

    merged["merge_match_flag"] = merged[rms_key_field].notna()
    merged["merge_confidence_score"] = merged["merge_match_flag"].astype(float)
    merged["merge_matching_strategy"] = merged["merge_match_flag"].map(
        {True: "primary_key", False: None}
    )

    # 2. Identify unmatched sets
    unmatched_cad = merged[~merged["merge_match_flag"]].copy()

    matched_keys = merged.loc[merged["merge_match_flag"], "_key_norm"].dropna().unique()
    unmatched_rms = rms_df[~rms_df["_key_norm"].isin(matched_keys)].copy()

    # 3. Apply alternative strategies in order
    strategies = [
        ("temporal_address", 0.85, score_temporal_address),
        ("officer_temporal", 0.80, score_officer_temporal),
        ("address_zone_approx_date", 0.75, score_address_zone_approx_date),
    ]

    # For simplicity, brute-force within reasonable sample.
    # For production, window by date and/or index.
    for cad_idx, cad_row in unmatched_cad.iterrows():
        best_score = 0.0
        best_strategy = None
        best_rms_idx = None

        for strat_name, threshold, scorer in strategies:
            for rms_idx, rms_row in unmatched_rms.iterrows():
                score = scorer(cad_row, rms_row)
                if score >= threshold and score > best_score:
                    best_score = score
                    best_strategy = strat_name
                    best_rms_idx = rms_idx

            if best_rms_idx is not None:
                # We already found a good match for this CAD row; stop trying lower strategies
                break

        if best_rms_idx is not None:
            # Update merged row
            merged.loc[cad_idx, "merge_confidence_score"] = best_score
            merged.loc[cad_idx, "merge_matching_strategy"] = best_strategy
            merged.loc[cad_idx, "merge_match_flag"] = True

            # Copy RMS columns into *_rms side for this CAD row
            for col in rms_df.columns:
                if col not in ["_key_norm"]:  # Skip internal columns
                    merged.loc[cad_idx, f"{col}_rms"] = unmatched_rms.loc[best_rms_idx, col]

            # Remove used RMS record from pool to preserve 1:1 mapping
            unmatched_rms = unmatched_rms.drop(index=best_rms_idx)

    return merged

if __name__ == "__main__":
    # Example usage
    cad = pd.read_excel(CAD_PATH)
    rms = pd.read_excel(RMS_PATH)

    merged = merge_cad_rms(cad, rms)

    # Quick QA summary
    print("Total CAD records:", len(cad))
    print("Matched records:", merged["merge_match_flag"].sum())
    print("\nMatching strategy breakdown:")
    print(merged["merge_matching_strategy"].value_counts(dropna=False))

    # Save for inspection
    merged.to_parquet("2025_CAD_RMS_merged.parquet")
    print(f"\nSaved merged results to: 2025_CAD_RMS_merged.parquet")
