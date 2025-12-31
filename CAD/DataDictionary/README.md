# CAD DataDictionary

This folder stores the **CAD export** data dictionary artifacts: schemas, value domains, defaults, and supporting scripts.

## CAD export field definitions

The comprehensive "data dictionary style" definitions (formats, derivations, allowed values, validations) for the CAD export live at:

- `current/schema/cad_export_field_definitions.md` (Draft v1.0 - finalized 2025-12-30)

This document provides field-by-field documentation including:
- Export header to standard name mapping
- Field definitions, data types, and formats
- Validation rules and allowed values
- Temporal field derivation logic
- Cross-references to RMS integration mappings

## Cross-system mappings

**Note**: Cross-system CAD-RMS mapping files are located in `CAD_RMS/DataDictionary/current/schema/`, not in this directory. This directory contains only CAD-specific schema files.

For CAD-RMS integration mappings, see:
- `../CAD_RMS/DataDictionary/current/schema/cad_to_rms_field_map.json` (v2.0)
- `../CAD_RMS/DataDictionary/current/schema/rms_to_cad_field_map.json` (v2.0)
- `../CAD_RMS/DataDictionary/current/schema/multi_column_matching_strategy.md`

## Layout

- `current/schema/`: CAD-specific schemas and field definitions (JSON, Markdown)
- `current/domains/`: allowed value sets / enumerations (JSON)
- `current/defaults/`: default rules (JSON)
- `archive/`: dated snapshots
- `templates/`: reusable templates
- `scripts/`: helper scripts
