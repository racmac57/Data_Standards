# Multi-Column Matching Strategy for CAD-RMS Integration

**Document Version**: 2.0  
**Last Updated**: 2025-12-30  
**Purpose**: Define strategies for confident matching between CAD and RMS records using multiple columns when primary key matching fails or is uncertain

---

## Overview

While the primary join key (`ReportNumberNew` ↔ `Case Number`) provides exact matching for most records, multi-column matching strategies enable confident matching when:

1. Primary keys are missing or corrupted
2. Primary keys don't match due to data entry errors
3. Supplemental records need to be linked (e.g., `25-000001A` vs `25-000001`)
4. Validation of primary key matches is required

---

## Matching Strategy Hierarchy

### 1. Primary Key Match (Exact)

**Strategy**: Direct key matching with normalization  
**Confidence**: 1.0 (100%)  
**Fields Used**:
- CAD: `ReportNumberNew`
- RMS: `Case Number`

**Normalization Rules**:
- Trim whitespace
- Collapse internal whitespace (e.g., `"25 - 000001"` → `"25-000001"`)
- Remove non-printable characters
- Case-insensitive matching

**Implementation**:
```python
def normalize_case_number(value):
    if pd.isna(value):
        return ''
    s = str(value).strip()
    s = ' '.join(s.split())  # Collapse whitespace
    s = ''.join(char for char in s if char.isprintable())
    return s

cad_df['_key_normalized'] = cad_df['ReportNumberNew'].apply(normalize_case_number)
rms_df['_key_normalized'] = rms_df['Case Number'].apply(normalize_case_number)
merged = cad_df.merge(rms_df, left_on='_key_normalized', right_on='_key_normalized', how='left')
```

---

### 2. Temporal + Address Match

**Strategy**: Match on incident date/time plus address similarity  
**Confidence Threshold**: 0.85 (85%)  
**Use Case**: Primary key missing or doesn't match, but temporal and location data are available

**Fields Required**:
- CAD: `TimeofCall`, `FullAddress2`
- RMS: `IncidentDate`, `IncidentTime`, `FullAddress`

**Matching Rules**:

| Field Pair | Tolerance/Similarity | Weight | Score Calculation |
|------------|---------------------|--------|-------------------|
| `TimeofCall` ↔ `IncidentDate` | Same day | 0.4 | 1.0 if same day, 0.0 otherwise |
| `TimeofCall` ↔ `IncidentTime` | Within 1 hour | 0.3 | Linear decay from 1.0 (0 min) to 0.0 (60 min) |
| `FullAddress2` ↔ `FullAddress` | Fuzzy string match (threshold 0.85) | 0.3 | Levenshtein-based similarity (0.0 to 1.0) |

**Confidence Score Formula**:
```
confidence = (date_match_score × 0.4) + (time_match_score × 0.3) + (address_similarity × 0.3)
```

**Implementation Notes**:
- Date matching: Extract date component from `TimeofCall`, compare to `IncidentDate`
- Time matching: Extract time component, calculate absolute difference in minutes, apply linear decay
- Address similarity: Use `fuzzywuzzy` or `rapidfuzz` library for Levenshtein-based similarity
  - Normalize addresses: lowercase, remove punctuation, normalize street suffixes (St → Street, Ave → Avenue)
  - Threshold: Only consider matches with similarity ≥ 0.85

**Example**:
```python
from rapidfuzz import fuzz
from datetime import timedelta

def temporal_address_match(cad_row, rms_row):
    scores = []
    
    # Date match (weight 0.4)
    cad_date = cad_row['TimeofCall'].date()
    rms_date = pd.to_datetime(rms_row['IncidentDate']).date()
    date_score = 1.0 if cad_date == rms_date else 0.0
    scores.append(date_score * 0.4)
    
    # Time match (weight 0.3)
    cad_time = cad_row['TimeofCall'].time()
    rms_time = pd.to_datetime(rms_row['IncidentTime'], format='%H:%M').time()
    time_diff = abs((datetime.combine(date.today(), cad_time) - 
                     datetime.combine(date.today(), rms_time)).total_seconds() / 60)
    time_score = max(0, 1.0 - (time_diff / 60))  # Linear decay over 60 minutes
    scores.append(time_score * 0.3)
    
    # Address similarity (weight 0.3)
    addr_sim = fuzz.ratio(normalize_address(cad_row['FullAddress2']), 
                          normalize_address(rms_row['FullAddress'])) / 100.0
    if addr_sim < 0.85:
        return 0.0  # Below threshold, reject match
    scores.append(addr_sim * 0.3)
    
    return sum(scores)
```

---

### 3. Officer + Temporal Match

**Strategy**: Match on officer plus date/time  
**Confidence Threshold**: 0.80 (80%)  
**Use Case**: Primary key missing, but officer assignment and temporal data are reliable

**Fields Required**:
- CAD: `Officer`, `TimeofCall`
- RMS: `OfficerOfRecord`, `IncidentDate`, `IncidentTime`

**Matching Rules**:

| Field Pair | Similarity/Matching | Weight | Score Calculation |
|------------|-------------------|--------|-------------------|
| `Officer` ↔ `OfficerOfRecord` | Normalized officer match | 0.5 | 1.0 if normalized match, 0.0 otherwise |
| `TimeofCall` ↔ `IncidentDate` | Same day | 0.3 | 1.0 if same day, 0.0 otherwise |
| `TimeofCall` ↔ `IncidentTime` | Within 2 hours | 0.2 | Linear decay from 1.0 (0 min) to 0.0 (120 min) |

**Officer Normalization**:
- Remove title prefixes (Officer, Ofc., OIC, etc.)
- Remove rank suffixes (Badge #, ID numbers)
- Normalize name order (Last, First → First Last)
- Case-insensitive comparison
- Handle comma-separated lists (take first officer from CAD)

**Confidence Score Formula**:
```
confidence = (officer_match_score × 0.5) + (date_match_score × 0.3) + (time_match_score × 0.2)
```

**Implementation Notes**:
- Officer matching: Use officer standardization lookup table (e.g., `Assignment_Master_V2.csv`) if available
- Fallback to normalized string comparison if lookup table unavailable
- Time tolerance is 2 hours (wider than temporal_address_match) because officer assignment may span shifts

---

### 4. Address + Zone + Approximate Date Match

**Strategy**: Match on address plus zone plus approximate date  
**Confidence Threshold**: 0.75 (75%)  
**Use Case**: Primary key missing, temporal data unreliable, but location data is strong

**Fields Required**:
- CAD: `FullAddress2`, `ZoneCalc` (PDZone)
- RMS: `FullAddress`, `Zone`

**Fields Optional**:
- CAD: `TimeofCall`
- RMS: `IncidentDate`

**Matching Rules**:

| Field Pair | Similarity/Matching | Weight | Score Calculation |
|------------|-------------------|--------|-------------------|
| `FullAddress2` ↔ `FullAddress` | Fuzzy string match (threshold 0.90) | 0.5 | Levenshtein-based similarity (0.0 to 1.0) |
| `ZoneCalc` ↔ `Zone` | Exact match | 0.3 | 1.0 if exact match, 0.0 otherwise |
| `TimeofCall` ↔ `IncidentDate` | Within 7 days | 0.2 | Linear decay from 1.0 (0 days) to 0.0 (7 days), optional |

**Confidence Score Formula**:
```
confidence = (address_similarity × 0.5) + (zone_match_score × 0.3) + (optional_date_score × 0.2)
```

**Implementation Notes**:
- Higher address similarity threshold (0.90) than temporal_address_match because date/time validation is weaker
- Zone must match exactly (integers 5-9)
- Date match is optional—if missing, confidence is calculated from address + zone only (weights normalized to 0.625 and 0.375)

---

## Matching Workflow

### Step 1: Primary Key Match

```python
# Normalize and merge on primary key
cad_df['_key_norm'] = cad_df['ReportNumberNew'].apply(normalize_case_number)
rms_df['_key_norm'] = rms_df['Case Number'].apply(normalize_case_number)

primary_merged = cad_df.merge(rms_df, left_on='_key_norm', right_on='_key_norm', 
                               how='left', suffixes=('_cad', '_rms'))
primary_merged['merge_match_flag'] = primary_merged['_key_norm_rms'].notna()
primary_merged['merge_confidence_score'] = primary_merged['merge_match_flag'].astype(float)
primary_merged['merge_matching_strategy'] = primary_merged['merge_match_flag'].map(
    {True: 'primary_key', False: None}
)
```

### Step 2: Identify Unmatched Records

```python
unmatched_cad = primary_merged[~primary_merged['merge_match_flag']].copy()
unmatched_rms = rms_df[~rms_df['_key_norm'].isin(
    primary_merged[primary_merged['merge_match_flag']]['_key_norm']
)].copy()
```

### Step 3: Apply Alternative Matching Strategies (in order of confidence)

For each unmatched CAD record, try strategies in this order:

1. **Temporal + Address Match** (threshold 0.85)
2. **Officer + Temporal Match** (threshold 0.80)
3. **Address + Zone + Approximate Date Match** (threshold 0.75)

```python
def apply_alternative_matching(unmatched_cad, unmatched_rms, strategies):
    results = []
    
    for cad_idx, cad_row in unmatched_cad.iterrows():
        best_match = None
        best_score = 0.0
        best_strategy = None
        
        for strategy in strategies:
            if not strategy_has_required_fields(cad_row, strategy):
                continue
                
            for rms_idx, rms_row in unmatched_rms.iterrows():
                score = calculate_match_score(cad_row, rms_row, strategy)
                
                if score >= strategy['confidence_threshold'] and score > best_score:
                    best_match = rms_row
                    best_score = score
                    best_strategy = strategy['strategy_name']
        
        if best_match is not None:
            results.append({
                'cad_idx': cad_idx,
                'rms_idx': best_match.name,
                'confidence': best_score,
                'strategy': best_strategy
            })
    
    return results
```

### Step 4: Merge Results

```python
# Apply alternative matches
alt_matches = apply_alternative_matching(unmatched_cad, unmatched_rms, strategies)

# Update primary_merged with alternative matches
for match in alt_matches:
    cad_idx = match['cad_idx']
    rms_idx = match['rms_idx']
    primary_merged.loc[cad_idx, 'merge_confidence_score'] = match['confidence']
    primary_merged.loc[cad_idx, 'merge_matching_strategy'] = match['strategy']
    # Merge RMS data fields
    for col in rms_df.columns:
        primary_merged.loc[cad_idx, f'{col}_rms'] = unmatched_rms.loc[rms_idx, col]
```

---

## Validation and Quality Assurance

### Match Quality Flags

Add flags to merged output:

- `merge_match_flag`: Boolean indicating if any match was found
- `merge_confidence_score`: Confidence score (0.0 to 1.0)
- `merge_matching_strategy`: Strategy used (`primary_key`, `temporal_address_match`, `officer_temporal_match`, `address_zone_match`, or `null`)

### Quality Checks

1. **High Confidence Matches Only**: Only apply alternative matches if confidence ≥ threshold
2. **One-to-One Enforcement**: If multiple RMS records match one CAD record, select highest confidence match
3. **One-to-Many Prevention**: If one RMS record matches multiple CAD records, flag for manual review (may indicate data quality issue)
4. **Temporal Consistency**: Validate that matched records have consistent temporal ordering (e.g., `TimeofCall` close to `IncidentDate`/`IncidentTime`)

### Reporting

Generate match quality report:

- Total records matched by primary key
- Total records matched by alternative strategies (by strategy type)
- Total records unmatched
- Distribution of confidence scores
- Examples of low-confidence matches for manual review

---

## Performance Considerations

### Indexing

Create indexes on matching fields before applying strategies:

```python
# Index on normalized keys
cad_df = cad_df.set_index('_key_norm')
rms_df = rms_df.set_index('_key_norm')

# Index on date for temporal matching
cad_df['_date'] = pd.to_datetime(cad_df['TimeofCall']).dt.date
rms_df['_date'] = pd.to_datetime(rms_df['IncidentDate']).dt.date
cad_df = cad_df.set_index('_date', append=True)
rms_df = rms_df.set_index('_date', append=True)
```

### Batch Processing

For large datasets, process in batches:

- Primary key match: Process entire dataset (pandas merge is efficient)
- Alternative strategies: Process unmatched records in batches (e.g., 10,000 CAD records at a time)
- Use parallel processing for similarity calculations (multiprocessing or joblib)

### Caching

Cache normalized values and similarity calculations:

```python
# Cache normalized addresses
address_cache = {}
def normalize_address_cached(addr):
    if addr not in address_cache:
        address_cache[addr] = normalize_address(addr)
    return address_cache[addr]
```

---

## Edge Cases and Special Handling

### 1. Missing Required Fields

If a strategy requires fields that are missing, skip that strategy for that record. Log the reason for skipping.

### 2. Multiple Matches Above Threshold

If multiple RMS records match one CAD record with confidence above threshold:
- Select the highest confidence match
- Log all matches above threshold for review
- Flag record with `merge_ambiguous_match = True`

### 3. Supplemental Case Numbers

Handle supplemental case numbers (e.g., `25-000001A`) by:
- Primary key match: Try exact match first
- If no exact match, try base case number match (`25-000001`)
- Use alternative strategies only if base case number also fails

### 4. Data Quality Issues

Flag potential data quality issues:
- Primary key matches with low confidence in alternative fields (e.g., different addresses, different dates)
- Alternative matches with confidence just above threshold (may indicate false positives)

---

## References

- `cad_export_field_definitions.md` - CAD field definitions
- `rms_export_field_definitions.md` - RMS field definitions (v1.0 - comprehensive)
- `cad_to_rms_field_map.json` - Mapping schema with matching strategies
- `rms_to_cad_field_map.json` - Reverse mapping schema

---

📄 **For full definitions of the RMS fields used in fuzzy, temporal, and ID matching strategies, see:**
[`rms_export_field_definitions.md`](./rms_export_field_definitions.md)

This comprehensive document includes:
- All 29 RMS export fields organized into 8 functional groups
- Validation rules, format specifications, and regex patterns
- Multi-column matching strategy usage by field
- Narrative extraction logic for suspect descriptions, vehicle details, and M.O.
- CAD integration and backfill mapping notes

---

## Change Log

| Date | Version | Changes |
|------|---------|---------|
| 2025-12-30 | 2.0 | Initial comprehensive multi-column matching strategy document |
