# CAD DataDictionary (status)

## Current schema artifacts

Located in `current/schema/`:

- `cad_export_field_definitions.md` (Draft v1.0 - finalized 2025-12-30) - Comprehensive CAD export field definitions and validation rules
  - Field-by-field documentation with export header mapping
  - Validation rules, formats, and allowed values for all CAD export fields
  - Temporal field derivation logic and standard naming conventions
  - Cross-referenced with RMS field definitions for integration

## Cross-system mappings

Cross-system CAD-RMS mapping files are located in `CAD_RMS/DataDictionary/current/schema/`:

- `cad_to_rms_field_map.json` (v2.0) - Enhanced CAD-to-RMS mapping with multi-column matching
- `rms_to_cad_field_map.json` (v2.0) - Enhanced RMS-to-CAD mapping with multi-column matching
- `multi_column_matching_strategy.md` - Multi-column matching strategy documentation

See `../CAD_RMS/DataDictionary/` for cross-system mapping schemas and documentation.


