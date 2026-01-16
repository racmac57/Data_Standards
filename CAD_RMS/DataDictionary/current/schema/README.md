# CAD-RMS Cross-System Mapping Schema

This directory contains enhanced mapping schemas and strategies for integrating CAD (Computer-Aided Dispatch) and RMS (Records Management System) data.

## Files

### Core Mapping Schemas

- **`cad_to_rms_field_map.json`** (v2.0) - Enhanced CAD-to-RMS field mapping with multi-column matching strategies
- **`rms_to_cad_field_map.json`** (v2.0) - Enhanced RMS-to-CAD field mapping with multi-column matching strategies

### Documentation

- **`multi_column_matching_strategy.md`** - Comprehensive guide to multi-column matching strategies for confident record linking

## Version 2.0 Enhancements

The enhanced mapping schemas (v2.0) include:

1. **Multi-Column Matching Strategies**: Three alternative matching strategies beyond primary key matching:
   - Temporal + Address Match (confidence threshold: 0.85)
   - Officer + Temporal Match (confidence threshold: 0.80)
   - Address + Zone + Approximate Date Match (confidence threshold: 0.75)

2. **Confidence Scoring**: Each match includes a confidence score (0.0 to 1.0) indicating match quality

3. **Match Strategy Tracking**: Audit fields track which matching strategy was used for each record

4. **Enhanced Audit Fields**: Additional metadata fields for match quality analysis and troubleshooting

## Usage

### Primary Key Matching

The primary join key (`ReportNumberNew` ↔ `Case Number`) should be used first for exact matching. The enhanced schemas maintain backward compatibility with primary key matching.

### Alternative Matching Strategies

When primary key matching fails or confidence is low, the alternative matching strategies can be applied according to the workflow defined in `multi_column_matching_strategy.md`.

### Backward Compatibility

The enhanced schemas are backward compatible with v1.0 schemas. Existing code that uses primary key matching will continue to work. Alternative matching strategies are additive enhancements.

## Related Documentation

- **CAD Field Definitions**: `../../CAD/DataDictionary/current/schema/cad_export_field_definitions.md`
- **RMS Field Definitions**: `../../RMS/DataDictionary/current/schema/rms_export_field_definitions.md`
- **Mapping Rules**: `../../../unified_data_dictionary/mappings/mapping_rules.md`

## Schema Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-12-15 | Initial mapping schema with primary key matching |
| 2.0 | 2025-12-30 | Added multi-column matching strategies, confidence scoring, enhanced audit fields |
