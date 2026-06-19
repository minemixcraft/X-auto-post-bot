# upload_secrets.ps1
# Script to upload local X (Twitter) Bot API credentials to GitHub

$credentialsPath = Join-Path $PSScriptRoot "config/credentials.env"

# 1. Check if config/credentials.env exists, if not create a template
if (-not (Test-Path $credentialsPath)) {
    $template = @"
# ==============================================================================
# X (Twitter) Bot Credentials Configuration File
# ------------------------------------------------------------------------------
# Put your API keys and tokens for each bot account here.
# Keep this file secure. It is already added to .gitignore and will NOT be committed.
# ==============================================================================

# GreenHaven (GH)
GH_CONSUMER_KEY="your_value_here"
GH_CONSUMER_SECRET="your_value_here"
GH_X_ACCESS_TOKEN="your_value_here"
GH_X_ACCESS_TOKEN_SECRET="your_value_here"

# Moonchill (MC)
MC_CONSUMER_KEY="your_value_here"
MC_CONSUMER_SECRET="your_value_here"
MC_X_ACCESS_TOKEN="your_value_here"
MC_X_ACCESS_TOKEN_SECRET="your_value_here"

# Stray Cat 1 (SC1)
SC1_CONSUMER_KEY="your_value_here"
SC1_CONSUMER_SECRET="your_value_here"
SC1_X_ACCESS_TOKEN="your_value_here"
SC1_X_ACCESS_TOKEN_SECRET="your_value_here"

# Stray Cat 2 (SC2)
SC2_CONSUMER_KEY="your_value_here"
SC2_CONSUMER_SECRET="your_value_here"
SC2_X_ACCESS_TOKEN="your_value_here"
SC2_X_ACCESS_TOKEN_SECRET="your_value_here"
"@
    
    # Ensure config folder exists
    $configDir = Split-Path $credentialsPath
    if (-not (Test-Path $configDir)) {
        New-Item -ItemType Directory -Path $configDir -Force | Out-Null
    }
    
    Set-Content -Path $credentialsPath -Value $template -Encoding UTF8
    Write-Output "======================================================================"
    Write-Output "Created credentials template at: config/credentials.env"
    Write-Output "======================================================================"
    Write-Output "Please edit that file, put your real API keys/tokens, and then run this script again."
    Exit
}

# 2. Check GitHub CLI installation
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    Write-Output "[ERROR] GitHub CLI ('gh') is not installed or not in PATH."
    Write-Output "Please install it from https://cli.github.com/ and try again."
    Exit
}

# 3. Check GitHub CLI auth status
Write-Output "Checking GitHub CLI authentication status..."
& gh auth status 2>&1 | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Output "[WARN] You are not logged into GitHub CLI."
    Write-Output "Starting GitHub CLI login flow..."
    & gh auth login
    if ($LASTEXITCODE -ne 0) {
        Write-Output "[ERROR] GitHub CLI login failed. Please authenticate manually and try again."
        Exit
    }
} else {
    Write-Output "[SUCCESS] Authenticated in GitHub CLI."
}

# 4. Read credentials
Write-Output "Reading credentials from config/credentials.env..."
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

if ($secrets.Count -eq 0) {
    Write-Output "[ERROR] No valid credentials found in config/credentials.env."
    Write-Output "Please make sure to replace 'your_value_here' with your real API keys."
    Exit
}

Write-Output "Found $($secrets.Count) credentials to upload. Starting upload to GitHub..."

# 5. Upload credentials to GitHub
$repo = (git remote get-url origin) -replace '^https://github.com/', '' -replace '\.git$', '' -replace '^git@github.com:', ''
foreach ($key in $secrets.Keys) {
    $val = $secrets[$key]
    Write-Output "Uploading credential: $key to repository $repo..."
    $val | gh secret set $key --repo $repo
    if ($LASTEXITCODE -eq 0) {
        Write-Output "   [SUCCESS] Successfully set credential: $key"
    } else {
        Write-Output "   [FAIL] Failed to set credential: $key"
    }
}

Write-Output "Credentials upload process finished!"
