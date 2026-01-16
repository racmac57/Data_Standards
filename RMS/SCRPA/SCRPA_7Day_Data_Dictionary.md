# SCRPA 7-Day Outputs — Data Dictionary

**Generated:** 2025-12-29 20:25:35

## Overview
This dictionary documents the new 7-Day outputs replacing `SCRPA_7Day_Filtered.csv`:

- **Detailed:** `SCRPA_7Day_Detailed.csv`
- **Summary:** `SCRPA_7Day_Summary.csv`

### Cycle Logic
- The 7-Day cycle is defined by **Report Date** values present in the file.
- `CycleStartDate` = minimum `Report Date` in the dataset.
- `CycleEndDate` = maximum `Report Date` in the dataset.
- **LagDay**: incidents with `Incident Date` **before** `CycleStartDate`.

### Key Definitions
- `IsLagDay` *(boolean)*: `true` when `Incident Date` < `CycleStartDate`.
- `LagDays` *(integer)*: days incident precedes `CycleStartDate` (0 if not lagday).
- `IncidentToReportDays` *(integer)*: days between `Report Date` and `Incident Date` (QA metric).
- `IncidentType` *(text)*: normalized from `Incident Type_1` by removing statute suffix and replacing 'Attempted Burglary' with 'Burglary' (e.g., `"Burglary - 2C:18-2"` → `"Burglary"`).
- `Crime_Category` *(text)*: crime category matching `all_crimes.m` logic. Only tracked categories (excluding 'Other') appear in Summary.

## Detailed Dataset — `SCRPA_7Day_Detailed.csv`

| Column | Type | Description |
|---|---|---|
| Case Number | object | **Source**: original 7-Day export. |
| Incident Date | object | **Source**: original 7-Day export. |
| Incident Time | object | **Source**: original 7-Day export. |
| Incident Date_Between | object | **Source**: original 7-Day export. |
| Incident Time_Between | object | **Source**: original 7-Day export. |
| Report Date | object | **Source**: original 7-Day export. |
| Report Time | object | **Source**: original 7-Day export. |
| Incident Type_1 | object | **Source**: original 7-Day export. |
| Incident Type_2 | object | **Source**: original 7-Day export. |
| Incident Type_3 | object | **Source**: original 7-Day export. |
| FullAddress | object | **Source**: original 7-Day export. |
| Grid | object | **Source**: original 7-Day export. |
| Zone | float64 | **Source**: original 7-Day export. |
| Narrative | object | **Source**: original 7-Day export. |
| Total Value Stolen | float64 | **Source**: original 7-Day export. |
| Total Value Recover | float64 | **Source**: original 7-Day export. |
| Registration 1 | object | **Source**: original 7-Day export. |
| Make1 | object | **Source**: original 7-Day export. |
| Model1 | object | **Source**: original 7-Day export. |
| Reg State 1 | object | **Source**: original 7-Day export. |
| Registration 2 | object | **Source**: original 7-Day export. |
| Reg State 2 | object | **Source**: original 7-Day export. |
| Make2 | object | **Source**: original 7-Day export. |
| Model2 | object | **Source**: original 7-Day export. |
| Reviewed By | object | **Source**: original 7-Day export. |
| CompleteCalc | object | **Source**: original 7-Day export. |
| Officer of Record | object | **Source**: original 7-Day export. |
| Squad | object | **Source**: original 7-Day export. |
| Det_Assigned | object | **Source**: original 7-Day export. |
| Case_Status | object | **Source**: original 7-Day export. |
| NIBRS Classification | float64 | **Source**: original 7-Day export. |
| CycleStartDate | date | Start date of the current 7-Day cycle (by Report Date). |
| CycleEndDate | date | End date of the current 7-Day cycle (by Report Date). |
| IsLagDay | boolean | True if Incident Date precedes CycleStartDate. |
| LagDays | integer | Days Incident Date precedes CycleStartDate (0 if not lagday). |
| IncidentToReportDays | integer | Days between Report Date and Incident Date. |
| IncidentType | text | Normalized incident type from `Incident Type_1` (for reference). |
| Crime_Category | text | Crime category matching `all_crimes.m` logic: 'Burglary Auto', 'Motor Vehicle Theft', 'Burglary - Comm & Res', 'Robbery', 'Sexual Offenses', or 'Other'. |

## Summary Dataset — `SCRPA_7Day_Summary.csv`

| Column | Type | Description |
|---|---|---|
| Crime_Category | text | Crime category aligned with `all_crimes.m` logic (excludes 'Other'). |
| LagDayCount | integer | Count of those incidents where `IsLagDay = true`. |
| TotalCount | integer | Number of incidents in the 7-Day cycle (by Report Date). |

## Reconciliation
- `sum(Summary.TotalCount excluding TOTAL row) = rowcount(Detailed where Crime_Category != 'Other')`
- `sum(Summary.LagDayCount excluding TOTAL row) = count(Detailed.IsLagDay = true where Crime_Category != 'Other')`
- Summary includes a TOTAL row at the bottom with aggregated counts

## Backward Compatibility
- All original columns from `SCRPA_7Day_Filtered.csv` are preserved in **Detailed**.
- The previous file is **deprecated** in favor of the two new outputs.
