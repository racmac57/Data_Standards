# RMS DataDictionary

This folder stores the **RMS export** data dictionary artifacts: schemas, value domains, defaults, and supporting scripts.

## RMS export field definitions

Comprehensive field definitions (formats, derivations, allowed values, validations) for RMS exports:

- `current/schema/rms_export_field_definitions.md` - Complete documentation of 29 RMS fields including field names, data types, validation rules, and usage in CAD-RMS integration workflows

## Cross-system mappings

**Note**: Cross-system CAD-RMS mapping files are located in `CAD_RMS/DataDictionary/current/schema/`, not in this directory. This directory contains only RMS-specific schema files.

For CAD-RMS integration mappings, see:
- `../CAD_RMS/DataDictionary/current/schema/cad_to_rms_field_map.json` (v2.0)
- `../CAD_RMS/DataDictionary/current/schema/rms_to_cad_field_map.json` (v2.0)
- `../CAD_RMS/DataDictionary/current/schema/multi_column_matching_strategy.md`

## Layout

- `current/schema/`: RMS-specific schemas and field definitions (JSON, Markdown)
- `current/domains/`: allowed value sets / enumerations (JSON)
- `current/defaults/`: default rules (JSON)
- `archive/`: dated snapshots
- `templates/`: reusable templates
- `scripts/`: helper scripts


