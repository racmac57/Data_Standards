# Changelog

All notable changes to this Standards folder (structure and key artifacts) will be documented here.

## [v0.3.0] - 2025-12-30

### Added
- **RMS Export Field Definitions** (`rms_export_field_definitions.md`)
  - Comprehensive documentation of 29 RMS export fields
  - Organized into 8 logical groups: Incident Identification, Temporal, Incident Classification, Location, Incident Details, Property, Vehicle, Personnel, and Case Management
  - Each field includes: Export Header, Standard Name, Definition, Source Field, Format/Regex, Logic, Validation Rules, Mapping Notes, and Group classification
  - Special narrative extraction logic for deriving suspect descriptions, vehicle details, property information, and modus operandi (M.O.)
  - Multi-column matching strategy usage summary showing which RMS fields are used in each matching strategy
  - Data quality validation rules summary organized by field group
  - Integration references to `rms_to_cad_field_map_v2_enhanced.json` and `multi_column_matching_strategy.md`

### Enhanced
- **CAD Export Field Definitions** (`CAD/DataDictionary/current/schema/cad_export_field_definitions.md`)
  - Finalized draft v1.0 comprehensive CAD export field definitions and validation rules
  - Cross-referenced with RMS definitions and mapping schemas
  - Standardized field naming conventions and validation patterns
- Updated `README.md` with reference to comprehensive RMS field definitions
- Updated `SUMMARY.md` to reflect new schema documentation
- Enhanced cross-referencing between CAD and RMS schema documentation

## 2025-12-15

- Created CAD/RMS/CAD_RMS `DataDictionary/` scaffolding:
  - `current/schema`, `current/domains`, `current/defaults`
  - `archive`, `templates`, `scripts`
- Added root documentation files:
  - `README.md`, `SUMMARY.md`, `CHANGELOG.md`
- Added per-DataDictionary documentation files:
  - `CAD/DataDictionary/{README.md,SUMMARY.md,CHANGELOG.md}`
  - `RMS/DataDictionary/{README.md,SUMMARY.md,CHANGELOG.md}`
  - `CAD_RMS/DataDictionary/{README.md,SUMMARY.md,CHANGELOG.md}`
- Added bootstrap scaffolding + placement script:
  - `CAD_RMS/DataDictionary/scripts/init_cad_rms_standards.ps1`
- Copied cross-system field maps into the canonical cross-system location:
  - `CAD_RMS/DataDictionary/current/schema/cad_to_rms_field_map.json`
  - `CAD_RMS/DataDictionary/current/schema/rms_to_cad_field_map.json`
- Initialized local Git repository:
  - `.git/` created (branch `main`)
  - `.gitignore` added

## 2025-12-17

- Added CAD export field definitions / validation rules (draft):
  - `CAD/DataDictionary/current/schema/cad_export_field_definitions.md`
- Updated summaries to reference the new CAD definitions document.
