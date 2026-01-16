# RMS DataDictionary (status)

## Current schema artifacts

Located in `current/schema/`:

- `rms_export_field_definitions.md` - Comprehensive RMS export field definitions documenting 29 fields including:
  - Primary keys: `CaseNumber`
  - Temporal fields: `IncidentDate`, `IncidentTime`, `ReportDate`, `ReportTime`
  - Incident classification: `IncidentType1`, `IncidentType2`, `IncidentType3`
  - Location fields: `FullAddress`, `Grid`, `Zone`
  - Officer fields: `OfficerOfRecord`, `Squad`, `DetAssigned`
  - Vehicle fields: `Registration1/2`, `Make1/2`, `Model1/2`, `RegState1/2`
  - Other fields: `Narrative`, `CaseStatus`, `NIBRSClassification`, and more
- `README.md` - Schema directory documentation and related file references

## Cross-system mappings

Cross-system CAD-RMS mapping files are located in `CAD_RMS/DataDictionary/current/schema/`:

- `cad_to_rms_field_map.json` (v2.0) - Enhanced CAD-to-RMS mapping with multi-column matching
- `rms_to_cad_field_map.json` (v2.0) - Enhanced RMS-to-CAD mapping with multi-column matching
- `multi_column_matching_strategy.md` - Multi-column matching strategy documentation

See `../CAD_RMS/DataDictionary/` for cross-system mapping schemas and documentation.


