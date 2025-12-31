# Changelog (CAD DataDictionary)

## 2025-12-30

- **CAD Export Field Definitions Finalized** (v0.3.0 release)
  - Finalized `cad_export_field_definitions.md` as draft v1.0
  - Comprehensive field-by-field documentation with validation rules, formats, and allowed values
  - Cross-referenced with RMS export field definitions for integration mapping
  - Standardized field naming conventions (export header → standard name mapping)
  - Documented validation rules for all 19+ CAD export fields including ReportNumberNew, Incident, HowReported, temporal fields, location fields, and disposition
- **Directory Structure Cleanup**: Removed cross-system mapping files from CAD directory for consistency:
  - Removed `cad_to_rms_field_map.json` (legacy v1.0)
  - Removed `rms_to_cad_field_map.json` (legacy v1.0)
  - Cross-system mappings now located only in `CAD_RMS/DataDictionary/current/schema/` (enhanced v2.0)
- CAD directory now contains only CAD-specific schema files for clarity and maintainability

## 2025-12-17

- Added draft CAD export field definitions / validation rules:
  - `current/schema/cad_export_field_definitions.md`

## 2025-12-15

- Standardized folder scaffolding (`current/schema|domains|defaults`, `archive`, `templates`, `scripts`).
- Confirmed presence of cross-system field maps under `current/schema/` (later moved to CAD_RMS directory on 2025-12-30).
