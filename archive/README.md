# Archive Directory

This directory contains archived files from the Standards repository restructuring.

## Contents

### packages/
Contains packaging artifacts like `.7z` archives.
- `Standards.7z` - Repository snapshot package

### legacy_copies/
Contains older versions of files kept for reference.
- Root-level legacy mapping files (pre-v2.0)
- `udd_git_backup/` - Backup of unified_data_dictionary/.git before removal

### removed_duplicates/
Contains duplicate files that were removed during cleanup.
- `CallType_Categories_backup_20260109_214115.csv` - Duplicate of CallType_Categories_latest.csv

## Retention Policy

- **Retention period:** 30 days after merge to main branch
- **After validation period:** Contents may be deleted or moved to external backup
- **Deletion should be documented** in CHANGELOG.md

## Archive Date

Created: 2026-01-15 (cleanup/standards-restructure branch)

## Notes

These files are tracked in Git for audit trail purposes. They can be safely deleted after the retention period if no longer needed for reference.
