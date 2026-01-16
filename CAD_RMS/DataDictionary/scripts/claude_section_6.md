## 6. Config & Mappings (Source of Truth in Repo)

Do not duplicate mapping logic or field definitions in this doc. Treat the repo's schema and dictionary files as the single source of truth.

### 6.1 Mapping Schemas

Use the v2.0 JSON mapping schemas for CAD↔RMS integration:

- `CAD_RMS/DataDictionary/current/schema/cad_to_rms_field_map.json`  
- `CAD_RMS/DataDictionary/current/schema/rms_to_cad_field_map.json`  
- `CAD_RMS/DataDictionary/current/schema/multi_column_matching_strategy.md`  

These define:

- **Primary join keys**: `ReportNumberNew` ↔ `Case Number`  
- **Multi-column matching strategies**:
  - Temporal + address (confidence threshold: 0.85)
  - Officer + temporal (confidence threshold: 0.80)
  - Address + zone + approximate date (confidence threshold: 0.75)
- **Confidence thresholds and matching rules**

Implementation code should:

- Load these JSON files at runtime (or via a config loader).  
- Use them to drive join logic instead of hard-coding mappings.  
- Reference `multi_column_matching_strategy.md` for detailed strategy documentation.

### 6.2 Field Definitions

Field definitions are Markdown and should be referenced from the repo:

- `CAD/DataDictionary/current/schema/cad_export_field_definitions.md`  
- `rms_export_field_definitions.md` (root level)

They contain:

- Export header → canonical name mappings.  
- Field definitions, validation rules, formats, and usage notes.  
- Data quality validation rules organized by field group.

ETL and analysis code should consult these docs when:

- Interpreting source fields.  
- Validating values.  
- Adding new metrics or joins.  
- Implementing data quality checks.

### 6.3 Implementation Example

See `CAD_RMS/DataDictionary/scripts/cad_rms_merge_loader.py` for a working example that:

- Loads the mapping JSON schema
- Implements primary key matching with normalization
- Applies alternative matching strategies in order
- Returns matches with confidence scores and strategy tracking
