# Summary (current state)

## Repository Structure (v2.0.0)

This repository contains a single `.git/` at the root level. The `unified_data_dictionary/` folder is integrated as a normal directory (not a submodule).

### Canonical Locations

| Schema Type | Location |
|-------------|----------|
| CAD field definitions | `CAD/DataDictionary/current/schema/` |
| RMS field definitions | `RMS/DataDictionary/current/schema/` |
| Cross-system mappings | `CAD_RMS/DataDictionary/current/schema/` |

### Archive

The `archive/` directory contains:
- `packages/` - Packaging artifacts (Standards.7z)
- `legacy_copies/` - Old file versions for reference
- `removed_duplicates/` - Duplicate files removed during cleanup

See `archive/README.md` for retention policy (30 days after merge).

### Chatlog Storage

Chatlogs are stored in `unified_data_dictionary/docs/chatlogs/`:
- `chunked/<chunk_id>/` - Direct flat structure
- Each chunk contains: `*_transcript.json`, `*_transcript.md`, `*_sidecar.json`, `*.origin.json`

---

## What exists now

- **CAD**
  - `CAD/DataDictionary/current/schema/` contains:
    - `cad_export_field_definitions.md` (Draft v1.0 - finalized 2025-12-30) - Comprehensive CAD export field definitions and validation rules
- **RMS**
  - `RMS/DataDictionary/` scaffolding exists (schema/domains/defaults + archive/templates/scripts)
  - `rms_export_field_definitions.md` - Comprehensive field definitions (29 fields, 8 groups)
- **Cross-system**
  - `CAD_RMS/DataDictionary/current/schema/` contains:
    - `cad_to_rms_field_map.json`
    - `rms_to_cad_field_map.json`
    - `multi_column_matching_strategy.md`
    - `rms_export_field_definitions.md` (root-level comprehensive documentation)
- **Call Type Classification**
  - `docs/call_type_category_mapping.md` - Complete Call Type to Category Type documentation
  - `mappings/call_type_category_mapping.json` - JSON lookup for programmatic access
  - `mappings/call_types_*.csv` - 11 category-specific CSV files for targeted loading
  - Primary reference: `09_Reference/Classifications/CallTypes/CallType_Categories.csv` (649 entries, with Incident_Norm column, 11 ESRI standard categories only) - **Single Source of Truth**
- **ETL Configuration**
  - `config/response_time_filters.json` - Response Time ETL filtering rules (How Reported, Category_Type, incident exclusions, inclusion overrides)

## Notes

- Cross-system field maps are located in the canonical cross-system location:
  - `CAD_RMS/DataDictionary/current/schema/` (v2.0 enhanced mappings with multi-column matching strategies)
  - CAD directory contains only CAD-specific schema files (cross-system mappings removed 2025-12-30 for clarity)

- A bootstrap script is available at:
  - `CAD_RMS/DataDictionary/scripts/init_cad_rms_standards.ps1`

- Root + per-DataDictionary documentation exists:
  - Root: `README.md`, `SUMMARY.md`, `CHANGELOG.md`
  - Per DataDictionary: `*/DataDictionary/{README.md,SUMMARY.md,CHANGELOG.md}`

- This folder is a local Git repo:
  - Single `.git/` at repository root
  - `.gitignore` present
  - `unified_data_dictionary/` is integrated (no nested repo)

## Recent Enhancements

### 🚀 Response Time Filter Configuration v1.2.2 (2026-01-14)

**ETL Configuration Added**
- New `config/` directory created for ETL configuration files
- Added `config/response_time_filters.json` - JSON configuration for Response Time ETL filtering rules
- Used by Response Time Monthly Generator script (v2.0.0)
- Configuration includes:
  - How Reported exclusions (Self-Initiated)
  - Category_Type exclusions (4 categories)
  - Specific incident exclusions (41 incidents)
  - Inclusion overrides (14 incidents kept despite category exclusion)

### 🚀 Call Type to Category Type Mapping v1.2.1 (2026-01-09)

**Backup Strategy Added**
- Timestamped backups created automatically in both CallTypes directory and Standards directory
- Backup script available: `scripts/backup_calltype_categories.py`
- "Latest" copy maintained in Standards directory for quick access

### 🚀 Call Type to Category Type Mapping v1.2.0 (2026-01-08)

**Category Standardization Complete**
- All categories standardized to 11 ESRI standard categories only
- Non-standard categories mapped to ESRI equivalents
- Added 9 remaining unmatched types (total now 649 entries)

### 🚀 Call Type to Category Type Mapping v1.0 (2026-01-08)

**Call Type Classification System - Added**
- **Primary Reference File**: `CallType_Categories.csv` (649 entries) - ESRI standardized classification - **Single Source of Truth**
  - Location: `09_Reference/Classifications/CallTypes/CallType_Categories.csv`
  - Format: Incident, Incident_Norm, Category_Type, Response_Type
  - Includes Incident_Norm column for normalized matching
  - E.D.P. variations (E.D.P., EDP, edp, etc.) all map to "Mental Health Incident"
  - **11 ESRI Standard Categories Only**: All non-standard categories have been mapped to ESRI standard
  - 11 standardized categories (Administrative and Support, Assistance and Mutual Aid, Community Engagement, Criminal Incidents, Emergency Response, Investigations and Follow-Ups, Juvenile-Related Incidents, Public Safety and Welfare, Regulatory and Ordinance, Special Operations and Tactical, Traffic and Motor Vehicle)
  - 3 Response Types (Emergency, Urgent, Routine)
- **Documentation**: `docs/call_type_category_mapping.md` - Complete breakdown of all Call Types by Category Type
- **Category-Specific Files**: 11 CSV files in `mappings/call_types_*.csv` for targeted script loading
- **JSON Mapping**: `mappings/call_type_category_mapping.json` - Programmatic lookup dictionaries
  - `call_type_to_category`: Quick category lookup
  - `call_type_to_response`: Response type lookup
  - `category_to_call_types`: All call types per category
- **Purpose**: Streamline knowledge base with script-referenceable files for RMS Incident Type classification and filtering

### 🚀 Schema Documentation v0.3.0 (2025-12-30)

**CAD Export Field Definitions - Finalized (Draft v1.0)**
- Comprehensive CAD export field definitions and validation rules
- Field-by-field documentation with export header to standard name mapping
- Validation rules, formats, and allowed values for all CAD export fields (ReportNumberNew, Incident, HowReported, temporal fields, location fields, etc.)
- Temporal field derivation logic and standard naming conventions
- Cross-referenced with RMS field definitions for integration

**RMS Export Field Definitions - Added (v1.0)**
- Comprehensive RMS export schema documentation
  - 29 documented fields across 8 functional categories
  - Groups: Incident Identification, Temporal, Incident Classification, Location, Incident Details, Property, Vehicle, Personnel, Case Management
  - Each field includes validation rules, format patterns, CAD mapping references, and multi-column matching strategy usage
  - Special narrative extraction logic for deriving suspect descriptions, vehicle details, property information, and M.O.
  - Integrated with `rms_to_cad_field_map_v2_enhanced.json` and multi-column matching strategies
  - Data quality validation rules summary organized by field group
