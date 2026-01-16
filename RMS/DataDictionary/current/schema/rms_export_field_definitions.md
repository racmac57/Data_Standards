# RMS Export — Field Definitions (Draft v1)

This document summarizes **RMS export columns** used in CAD data cleaning and enrichment workflows and standardizes naming, allowed values, and calculation logic.

## Column name mapping (export → standard)

Some RMS export headers contain spaces; the "standard" name is what we use in mapping/schema work.

- `Case Number` → `CaseNumber`
- `Incident Date` → `IncidentDate`
- `Incident Time` → `IncidentTime`
- `Incident Date_Between` → `IncidentDateBetween`
- `Incident Time_Between` → `IncidentTimeBetween`
- `Report Date` → `ReportDate`
- `Report Time` → `ReportTime`
- `Incident Type_1` → `IncidentType1`
- `Incident Type_2` → `IncidentType2`
- `Incident Type_3` → `IncidentType3`
- `FullAddress` → `FullAddress`
- `Grid` → `Grid`
- `Zone` → `Zone`
- `Narrative` → `Narrative`
- `Total Value Stolen` → `TotalValueStolen`
- `Total Value Recover` → `TotalValueRecover`
- `Registration 1` → `Registration1`
- `Make1` → `Make1`
- `Model1` → `Model1`
- `Reg State 1` → `RegState1`
- `Registration 2` → `Registration2`
- `Reg State 2` → `RegState2`
- `Make2` → `Make2`
- `Model2` → `Model2`
- `Reviewed By` → `ReviewedBy`
- `CompleteCalc` → `CompleteCalc`
- `Officer of Record` → `OfficerOfRecord`
- `Squad` → `Squad`
- `Det_Assigned` → `DetAssigned`
- `Case_Status` → `CaseStatus`
- `NIBRS Classification` → `NIBRSClassification`

## Field-by-field definitions

### `CaseNumber` *(export header: `Case Number`)*

- **Definition**: RMS case identifier (primary key / join key to CAD ReportNumberNew).
- **Format**: `YY-NNNNNN` with optional supplemental suffix letter, e.g. `25-000001`, `25-000001A`.
  - **Regex**: `^\d{2}-\d{6}([A-Z])?$`
- **Logic**:
  - `YY` = last two digits of the **year the case was created**
  - `NNNNNN` = sequential number starting at `000001` on January 01 each year
  - **Supplementals**: same base number, with a suffix letter starting at `A` (then `B`, `C`, …)
- **Validation rules**:
  - Must be non-null.
  - Must match the regex.
  - Must not be parsed as numeric (keep as text to preserve leading zeros).
- **Join key**: Primary key for matching to CAD `ReportNumberNew`.

### `IncidentDate` *(export header: `Incident Date`)*

- **Definition**: Date when the incident occurred (not necessarily when reported).
- **Type**: date (stored as date type, exported as Excel date serial or MM/dd/yyyy format).
- **Accepted formats**:
  - Excel date serial number
  - `MM/dd/yyyy`
  - `M/d/yyyy`
  - ISO8601 date (`YYYY-MM-DD`)
- **Validation rules**:
  - May be null (incidents without confirmed dates).
  - If present, must be a valid date.
  - Should be ≤ `ReportDate` (flag if incident date is after report date).
- **Matching use**: Can be used as part of multi-column matching strategy (with IncidentTime, FullAddress).

### `IncidentTime` *(export header: `Incident Time`)*

- **Definition**: Time when the incident occurred (not necessarily when reported).
- **Type**: time (stored as time type, exported as Excel time or HH:mm format).
- **Accepted formats**:
  - Excel time serial number
  - `HH:mm`
  - `H:mm`
  - `HH:mm:ss`
- **Validation rules**:
  - May be null.
  - If present, must be a valid time-of-day.
- **Matching use**: Can be combined with `IncidentDate` for temporal matching to CAD `TimeofCall`.

### `IncidentDateBetween` *(export header: `Incident Date_Between`)*

- **Definition**: End date of a date range for incidents occurring "between" dates.
- **Type**: date.
- **Validation rules**:
  - May be null (most incidents are point-in-time).
  - If present, should be ≥ `IncidentDate`.

### `IncidentTimeBetween` *(export header: `Incident Time_Between`)*

- **Definition**: End time of a time range for incidents occurring "between" times.
- **Type**: time.
- **Validation rules**:
  - May be null (most incidents are point-in-time).
  - If present and `IncidentDateBetween` matches `IncidentDate`, should be ≥ `IncidentTime`.

### `ReportDate` *(export header: `Report Date`)*

- **Definition**: Date when the report was filed/created in RMS.
- **Type**: date.
- **Accepted formats**: Same as `IncidentDate`.
- **Validation rules**:
  - May be null (rare).
  - If both present, should be ≥ `IncidentDate` (flag if report date precedes incident date by more than reasonable threshold, e.g., 30 days).

### `ReportTime` *(export header: `Report Time`)*

- **Definition**: Time when the report was filed/created in RMS.
- **Type**: time.
- **Accepted formats**: Same as `IncidentTime`.
- **Validation rules**:
  - May be null.

### `IncidentType1` *(export header: `Incident Type_1`)*

- **Definition**: Primary incident type classification code/description.
- **Type**: text (string).
- **Validation rules**:
  - May be null.
  - Should match controlled vocabulary (to be defined from RMS incident type reference).
- **Backfill priority**: Priority 1 for backfilling CAD `Incident` field.

### `IncidentType2` *(export header: `Incident Type_2`)*

- **Definition**: Secondary incident type classification (if multiple types apply).
- **Type**: text (string).
- **Validation rules**:
  - May be null.
- **Backfill priority**: Priority 2 for backfilling CAD `Incident` field.

### `IncidentType3` *(export header: `Incident Type_3`)*

- **Definition**: Tertiary incident type classification (if multiple types apply).
- **Type**: text (string).
- **Validation rules**:
  - May be null.
- **Backfill priority**: Priority 3 for backfilling CAD `Incident` field.

### `FullAddress` *(export header: `FullAddress`)*

- **Definition**: Full incident location address string.
- **Type**: text (string).
- **Expected format**: Contains commas (observed in sample data).
  - **Example pattern**: `Street, City, State ZIP` (exact components may vary)
- **Validation rules**:
  - May be null (some incidents may not have addresses).
  - If present, should contain at least one comma.
- **Matching use**: Can be used as part of multi-column matching strategy (with CaseNumber, temporal fields).
- **Backfill use**: Used to backfill CAD `FullAddress2` when CAD address is missing or invalid.

### `Grid`

- **Definition**: CAD grid / map grid identifier.
- **Type**: text (string).
- **Validation rules**:
  - May be null.
  - If present, should match a controlled list of known grid codes (same as CAD Grid domain).
- **Backfill use**: Used to backfill CAD `Grid` when CAD grid is missing.

### `Zone` *(export header: `Zone`)*

- **Definition**: Patrol/PD zone code assigned to the incident.
- **Type**: integer or text (stored as string in current schema; observed as integer in analysis).
- **Observed range**: `5`–`9` (integers only, consistent with CAD PDZone).
- **Validation rules**:
  - May be null.
  - If present: must be an integer and within the valid zone domain (same as CAD ZoneCalc/PDZone).
- **Backfill use**: Used to backfill CAD `PDZone` when CAD zone is missing (28.5% backfill rate observed).

### `Narrative`

- **Definition**: Detailed narrative text describing the incident, actions taken, and outcomes.
- **Type**: text (string, may be long-form text with multiple paragraphs).
- **Validation rules**:
  - May be null (some reports may not have narratives).
  - If present, may contain newlines, special characters, and unstructured text.
- **Matching use**: Can be used for fuzzy text matching when primary keys don't match (with caution due to unstructured nature).

### `TotalValueStolen` *(export header: `Total Value Stolen`)*

- **Definition**: Total monetary value of stolen property in dollars.
- **Type**: number (decimal).
- **Accepted formats**:
  - Numeric value
  - Currency text (with $, commas)
- **Validation rules**:
  - May be null (not all incidents involve theft).
  - If present, must be ≥ 0.

### `TotalValueRecover` *(export header: `Total Value Recover`)*

- **Definition**: Total monetary value of recovered property in dollars.
- **Type**: number (decimal).
- **Accepted formats**: Same as `TotalValueStolen`.
- **Validation rules**:
  - May be null.
  - If present, must be ≥ 0.
  - Should be ≤ `TotalValueStolen` (flag if recovered exceeds stolen).

### `Registration1` *(export header: `Registration 1`)*

- **Definition**: Vehicle registration/license plate number for first vehicle involved.
- **Type**: text (string).
- **Validation rules**:
  - May be null (not all incidents involve vehicles).
  - Format varies by state (see `RegState1`).

### `Make1` *(export header: `Make1`)*

- **Definition**: Vehicle make (manufacturer) for first vehicle.
- **Type**: text (string).
- **Examples**: `Ford`, `Toyota`, `Honda`, `Chevrolet`.
- **Validation rules**:
  - May be null.
  - Should match against known vehicle make list if available.

### `Model1` *(export header: `Model1`)*

- **Definition**: Vehicle model for first vehicle.
- **Type**: text (string).
- **Examples**: `F-150`, `Camry`, `Civic`, `Silverado`.
- **Validation rules**:
  - May be null.

### `RegState1` *(export header: `Reg State 1`)*

- **Definition**: State abbreviation for first vehicle registration.
- **Type**: text (string).
- **Expected format**: Two-letter US state abbreviation (e.g., `NJ`, `NY`, `PA`).
- **Validation rules**:
  - May be null.
  - If present, should be valid US state abbreviation (50 states + DC).

### `Registration2` *(export header: `Registration 2`)*

- **Definition**: Vehicle registration/license plate number for second vehicle involved.
- **Type**: text (string).
- **Validation rules**: Same as `Registration1`.

### `RegState2` *(export header: `Reg State 2`)*

- **Definition**: State abbreviation for second vehicle registration.
- **Type**: text (string).
- **Validation rules**: Same as `RegState1`.

### `Make2` *(export header: `Make2`)*

- **Definition**: Vehicle make (manufacturer) for second vehicle.
- **Type**: text (string).
- **Validation rules**: Same as `Make1`.

### `Model2` *(export header: `Model2`)*

- **Definition**: Vehicle model for second vehicle.
- **Type**: text (string).
- **Validation rules**: Same as `Model1`.

### `ReviewedBy` *(export header: `Reviewed By`)*

- **Definition**: Officer or supervisor identifier who reviewed the case.
- **Type**: text (string).
- **Validation rules**:
  - May be null (cases may not yet be reviewed).
  - Should match standardized officer naming convention (same as `OfficerOfRecord`).

### `CompleteCalc` *(export header: `CompleteCalc`)*

- **Definition**: Boolean flag indicating whether the case is marked as complete.
- **Type**: boolean.
- **Accepted formats**:
  - Boolean (`true`/`false`)
  - `0`/`1`
  - `Y`/`N`
  - `Yes`/`No`
  - `Complete`/`Incomplete`
- **Validation rules**:
  - May be null (defaults to incomplete).
  - If present, must be coercible to boolean.

### `OfficerOfRecord` *(export header: `Officer of Record`)*

- **Definition**: Primary officer assigned to the case in RMS.
- **Type**: text (string).
- **Validation rules**:
  - May be null (some cases may not have assigned officers).
  - Should match standardized officer naming convention (align to `CAD/SCRPA/Assignment_Master_V2.csv` standardization outputs).
- **Backfill use**: Used to backfill CAD `Officer` when CAD officer is missing.
- **Matching use**: Can be used as part of multi-column matching strategy (with CaseNumber, temporal fields, address).

### `Squad`

- **Definition**: Squad/unit identifier for the assigned officer.
- **Type**: text (string).
- **Validation rules**:
  - May be null.

### `DetAssigned` *(export header: `Det_Assigned`)*

- **Definition**: Detective identifier assigned to the case (if applicable).
- **Type**: text (string).
- **Validation rules**:
  - May be null (not all cases require detective assignment).

### `CaseStatus` *(export header: `Case_Status`)*

- **Definition**: Current status of the case in RMS.
- **Type**: text (string).
- **Expected values**: To be defined from RMS case status domain (e.g., `Open`, `Closed`, `Pending`, `Under Investigation`).
- **Validation rules**:
  - May be null.
  - Should match controlled vocabulary (to be defined).

### `NIBRSClassification` *(export header: `NIBRS Classification`)*

- **Definition**: NIBRS (National Incident-Based Reporting System) classification code.
- **Type**: text (string).
- **Validation rules**:
  - May be null (not all incidents have NIBRS classifications).
  - If present, should match NIBRS code structure (to be validated against NIBRS reference).

## Open confirmations (to finalize v1)

1. Confirm the canonical allowed domains for:
   - `CaseStatus` (status values)
   - `IncidentType1/2/3` (incident type codes/descriptions)
   - `NIBRSClassification` (NIBRS code structure and valid values)
2. Confirm whether supplementals can exceed `Z` (e.g., `AA`) or are limited to single-letter suffix (same as CAD).
3. Confirm timezone for `IncidentDate`/`IncidentTime` and `ReportDate`/`ReportTime` (recommend documenting as `America/New_York`).
4. Provide controlled vocabulary lists for vehicle makes and models (if available).
5. Confirm whether `IncidentDate`/`IncidentTime` should always match or be close to CAD `TimeofCall` for same case number (data quality validation).
