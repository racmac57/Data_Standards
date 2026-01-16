[CmdletBinding()]
param(
  [string]$StandardsRoot = "C:\Users\carucci_r\OneDrive - City of Hackensack\09_Reference\Standards",
  [string]$IncomingJsonDir = "C:\_Sandbox\incoming_json",
  [switch]$CopyOnly
)

$ErrorActionPreference = "Stop"

function Ensure-Dir([string]$Path) {
  if (-not (Test-Path -LiteralPath $Path)) {
    New-Item -ItemType Directory -Path $Path | Out-Null
  }
}

function Ensure-Doc([string]$Path, [string]$Content) {
  if (-not (Test-Path -LiteralPath $Path)) {
    New-Item -ItemType File -Path $Path -Value $Content | Out-Null
  }
}

function Place-File([string]$Source, [string]$Dest) {
  if (-not (Test-Path -LiteralPath $Source)) {
    Write-Host "Missing source: $Source"
    return
  }
  $destDir = Split-Path -Path $Dest -Parent
  Ensure-Dir $destDir

  if ($CopyOnly) {
    Copy-Item -LiteralPath $Source -Destination $Dest -Force
    Write-Host "Copied: $Source -> $Dest"
  } else {
    Move-Item -LiteralPath $Source -Destination $Dest -Force
    Write-Host "Moved:  $Source -> $Dest"
  }
}

# --- Scaffolding roots
$cadRoot   = Join-Path $StandardsRoot "CAD\DataDictionary"
$rmsRoot   = Join-Path $StandardsRoot "RMS\DataDictionary"
$crossRoot = Join-Path $StandardsRoot "CAD_RMS\DataDictionary"

$targets = @(
  "$cadRoot\current\schema", "$cadRoot\current\domains", "$cadRoot\current\defaults",
  "$cadRoot\archive", "$cadRoot\templates", "$cadRoot\scripts",

  "$rmsRoot\current\schema", "$rmsRoot\current\domains", "$rmsRoot\current\defaults",
  "$rmsRoot\archive", "$rmsRoot\templates", "$rmsRoot\scripts",

  "$crossRoot\current\schema",
  "$crossRoot\archive", "$crossRoot\scripts"
)

$targets | ForEach-Object { Ensure-Dir $_ }

# --- Standard docs (created only if missing)
$readmeText = @"
DataDictionary

Purpose

Store schema, defaults, and domains for exports.

Folders

current\schema: field maps and schema
current\defaults: default rules
current\domains: allowed value sets
archive: dated snapshots
"@

$summaryText = @"
Status

Structure created.
JSONs (if provided) placed into schema folders.
"@

$changelogText = @"
CHANGELOG

2025-12-15

Initial structure.
"@

Ensure-Doc (Join-Path $cadRoot "README.md") $readmeText
Ensure-Doc (Join-Path $cadRoot "SUMMARY.md") $summaryText
Ensure-Doc (Join-Path $cadRoot "CHANGELOG.md") $changelogText

Ensure-Doc (Join-Path $rmsRoot "README.md") $readmeText
Ensure-Doc (Join-Path $rmsRoot "SUMMARY.md") $summaryText
Ensure-Doc (Join-Path $rmsRoot "CHANGELOG.md") $changelogText

Ensure-Doc (Join-Path $crossRoot "README.md") $readmeText
Ensure-Doc (Join-Path $crossRoot "SUMMARY.md") $summaryText
Ensure-Doc (Join-Path $crossRoot "CHANGELOG.md") $changelogText

# --- JSON placements (only moves/copies if source exists)
$placements = @(
  # CAD
  @{ src = "cad_field_map.json";        dst = "$cadRoot\current\schema\cad_field_map.json" },
  @{ src = "cad_fields_schema.json";    dst = "$cadRoot\current\schema\cad_fields_schema.json" },

  # RMS
  @{ src = "rms_field_map.json";        dst = "$rmsRoot\current\schema\rms_field_map.json" },
  @{ src = "rms_fields_schema.json";    dst = "$rmsRoot\current\schema\rms_fields_schema.json" },

  # Cross-system
  @{ src = "cad_to_rms_field_map.json"; dst = "$crossRoot\current\schema\cad_to_rms_field_map.json" },
  @{ src = "rms_to_cad_field_map.json"; dst = "$crossRoot\current\schema\rms_to_cad_field_map.json" }
)

foreach ($p in $placements) {
  $srcPath = Join-Path $IncomingJsonDir $p.src
  Place-File $srcPath $p.dst
}

Write-Host "Done."


