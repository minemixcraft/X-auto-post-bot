# run_local.ps1
# Script to run the X (Twitter) Bot locally using credentials from config/credentials.env

$credentialsPath = Join-Path $PSScriptRoot "config/credentials.env"

# 1. Check if config/credentials.env exists
if (-not (Test-Path $credentialsPath)) {
    Write-Host "[ERROR] config/credentials.env not found." -ForegroundColor Red
    Write-Host "Creating a template config/credentials.env file..." -ForegroundColor Yellow
    # Trigger upload_secrets.ps1 to generate the template file
    & (Join-Path $PSScriptRoot "upload_secrets.ps1")
    Exit
}

# 2. Read credentials into a hash table
$secrets = @{}
$lines = Get-Content $credentialsPath
foreach ($line in $lines) {
    $line = $line.Trim()
    if ($line.StartsWith("#") -or $line -eq "") {
        continue
    }
    if ($line -match '^([^=]+)=(.*)$') {
        $key = $Matches[1].Trim()
        $value = $Matches[2].Trim().Trim('"').Trim("'")
        if ($value -ne "your_value_here" -and $value -ne "") {
            $secrets[$key] = $value
        }
    }
}

# Interactive Menu Helper Function
function Show-Menu {
    param (
        [string]$Title,
        [string[]]$Options
    )

    $selectedIndex = 0
    $running = $true

    # Hide cursor
    $oldCursorVisible = [Console]::CursorVisible
    try {
        [Console]::CursorVisible = $false
    } catch {}

    $startRow = [Console]::CursorTop

    while ($running) {
        [Console]::SetCursorPosition(0, $startRow)

        Write-Host "==========================================" -ForegroundColor Cyan
        Write-Host " $Title" -ForegroundColor Cyan
        Write-Host "==========================================" -ForegroundColor Cyan

        for ($i = 0; $i -lt $Options.Length; $i++) {
            if ($i -eq $selectedIndex) {
                Write-Host "  > $($Options[$i])" -ForegroundColor Cyan -BackgroundColor Black
            } else {
                Write-Host "    $($Options[$i])"
            }
        }
        Write-Host "==========================================" -ForegroundColor Cyan

        $key = [Console]::ReadKey($true)
        if ($key.Key -eq "UpArrow") {
            if ($selectedIndex -gt 0) { $selectedIndex-- }
        } elseif ($key.Key -eq "DownArrow") {
            if ($selectedIndex -lt ($Options.Length - 1)) { $selectedIndex++ }
        } elseif ($key.Key -eq "Enter") {
            $running = $false
        }
    }

    try {
        [Console]::CursorVisible = $oldCursorVisible
    } catch {}
    Write-Host "" # New line after selection
    return $selectedIndex
}

# 3. Choose Bot Account
$botOptions = @(
    "GreenHaven (GH)",
    "Moonchill (MC)",
    "Stray Cat 1 (SC1)",
    "Stray Cat 2 (SC2)"
)
$botChoiceIdx = Show-Menu -Title "Select Bot Account to Run" -Options $botOptions

$botName = ""
$prefix = ""
switch ($botChoiceIdx) {
    0 { $botName = "greenhaven"; $prefix = "GH_" }
    1 { $botName = "moonchill"; $prefix = "MC_" }
    2 { $botName = "stray_cat_1"; $prefix = "SC1_" }
    3 { $botName = "stray_cat_2"; $prefix = "SC2_" }
}

# 4. Choose Mode
$modeOptions = @(
    "Manual (Select tweet, preview, and post)",
    "Auto (Automated scheduled posting)",
    "Diagnose (Check API access & credentials test)"
)
$modeChoiceIdx = Show-Menu -Title "Select Run Mode" -Options $modeOptions

$mode = ""
switch ($modeChoiceIdx) {
    0 { $mode = "manual" }
    1 { $mode = "auto" }
    2 { $mode = "diagnose" }
}

# 5. Choose Dry Run
$dryRunFlag = ""
if ($mode -ne "diagnose") {
    $dryRunOptions = @(
        "Yes (Test mode - do not post real tweets)",
        "No (LIVE mode - post real tweets to X)"
    )
    $dryRunIdx = Show-Menu -Title "Run in Dry Run (Test) mode?" -Options $dryRunOptions
    if ($dryRunIdx -eq 1) {
        $dryRunFlag = ""
        Write-Host "[WARN] Warning: The bot will post real tweets to X!" -ForegroundColor Yellow
    } else {
        $dryRunFlag = "--dry-run"
        Write-Host "[INFO] Dry-run mode enabled (no tweets will actually be posted)." -ForegroundColor Cyan
    }
}

# 6. Map and Verify Credentials
$env:CONSUMER_KEY = $secrets["$($prefix)CONSUMER_KEY"]
$env:CONSUMER_SECRET = $secrets["$($prefix)CONSUMER_SECRET"]
$env:X_ACCESS_TOKEN = $secrets["$($prefix)X_ACCESS_TOKEN"]
$env:X_ACCESS_TOKEN_SECRET = $secrets["$($prefix)X_ACCESS_TOKEN_SECRET"]

if (-not $env:CONSUMER_KEY -or -not $env:CONSUMER_SECRET -or -not $env:X_ACCESS_TOKEN -or -not $env:X_ACCESS_TOKEN_SECRET) {
    Write-Host "`n[ERROR] Missing credentials for $botName ($($prefix)CONSUMER_KEY etc.) in config/credentials.env." -ForegroundColor Red
    Write-Host "Please open config/credentials.env and provide the keys for this bot first." -ForegroundColor Yellow
    Exit
}

# 7. Execute the Bot
Write-Host "`nLaunching bot: $botName in '$mode' mode..." -ForegroundColor Green
$cmdArgs = @("-m", "src.main", "--bot", $botName, "--mode", $mode)
if ($dryRunFlag) {
    $cmdArgs += $dryRunFlag
}

python @cmdArgs
