<#
.SYNOPSIS
  Launch Claude Fable 5 on the taobanker adversarial-review package.

.DESCRIPTION
  Runs Claude Code non-interactively with model claude-fable-5[1m],
  xhigh effort, project working directory fixed to project-taobanker.
  Writes a session log under 06-fable-brief/runs/.

.EXAMPLE
  pwsh -File .\06-fable-brief\Launch-Fable5.ps1
  pwsh -File .\06-fable-brief\Launch-Fable5.ps1 -Interactive
#>
[CmdletBinding()]
param(
  [switch]$Interactive,
  [ValidateSet("low","medium","high","xhigh","max")]
  [string]$Effort = "xhigh",
  [string]$Model = "claude-fable-5[1m]"
)

$ErrorActionPreference = "Stop"
# PSScriptRoot = .../project-taobanker/06-fable-brief → project root is parent
$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$Claude = Join-Path $env:USERPROFILE ".local\bin\claude.exe"
if (-not (Test-Path $Claude)) {
  throw "Claude Code not found at $Claude"
}

$PromptPath = Join-Path $PSScriptRoot "FABLE_LAUNCH_PROMPT.md"
$Prompt = Get-Content -Path $PromptPath -Raw -Encoding utf8

$RunDir = Join-Path $PSScriptRoot "runs"
New-Item -ItemType Directory -Force -Path $RunDir | Out-Null
$stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$LogPath = Join-Path $RunDir "fable5-$stamp.log"
$StatusPath = Join-Path $RunDir "fable5-$stamp.status.txt"

Set-Location $Root

$common = @(
  "--model", $Model,
  "--effort", $Effort,
  "--dangerously-skip-permissions"
)

Write-Host "Root:   $Root"
Write-Host "Model:  $Model"
Write-Host "Effort: $Effort"
Write-Host "Log:    $LogPath"

if ($Interactive) {
  "interactive launch $stamp" | Set-Content $StatusPath
  & $Claude @common $Prompt 2>&1 | Tee-Object -FilePath $LogPath
  exit $LASTEXITCODE
}

# Non-interactive: full print session (long-running math review)
"running print session $stamp" | Set-Content $StatusPath
$argsPrint = $common + @(
  "-p", $Prompt,
  "--output-format", "text"
)

try {
  & $Claude @argsPrint 2>&1 | Tee-Object -FilePath $LogPath
  $code = $LASTEXITCODE
  "exit_code=$code finished=$(Get-Date -Format o)" | Set-Content $StatusPath
  if (Test-Path (Join-Path $PSScriptRoot "VERDICT.md")) {
    Add-Content $StatusPath "VERDICT.md present"
  } else {
    Add-Content $StatusPath "VERDICT.md MISSING"
  }
  exit $code
} catch {
  "FAILED: $_" | Set-Content $StatusPath
  throw
}
