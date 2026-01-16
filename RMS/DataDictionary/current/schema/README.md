# RMS Data Dictionary Schema

This directory contains schema definitions for RMS (Records Management System) export fields.

## Files

- **`rms_export_field_definitions.md`** - Comprehensive field definitions for RMS export columns, including:
  - Field names and mappings (export header → standard/internal names)
  - Data types and formats
  - Validation rules
  - Usage in CAD-RMS integration workflows
  - Matching strategy applications

## Related Documentation

- **CAD Field Definitions**: `../../CAD/DataDictionary/current/schema/cad_export_field_definitions.md`
- **CAD-RMS Mapping**: `../../CAD_RMS/DataDictionary/current/schema/`
- **Mapping Rules**: `../../../unified_data_dictionary/mappings/mapping_rules.md`

## Field Usage in Matching Strategies

Several RMS fields are used in multi-column matching strategies:

- **Primary Join Key**: `CaseNumber` (Case Number)
- **Temporal Matching**: `IncidentDate`, `IncidentTime`
- **Address Matching**: `FullAddress`
- **Officer Matching**: `OfficerOfRecord`
- **Zone Matching**: `Zone`
- **Backfill Fields**: `IncidentType1/2/3`, `FullAddress`, `Grid`, `Zone`, `OfficerOfRecord`

See `../../CAD_RMS/DataDictionary/current/schema/multi_column_matching_strategy.md` for details on how these fields are used in matching strategies.
