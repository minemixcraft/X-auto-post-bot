# 🛸 Twitter/X Auto-Posting Bot Project

This project contains a suite of automated and manual posting bots for multiple Twitter/X accounts (GreenHaven, Moonchill, Stray Cat 1, Stray Cat 2) running on GitHub Actions or locally.

---

## 📁 Project Architecture

The codebase has been refactored to follow **Clean Architecture** and **Separation of Concerns**:

* **`src/`**: Contains core logic, modular UI layers (clean text and ASCII art versions), scheduling logic, and helpers.
  * **`src/main.py`**: Unified Command-Line (CLI) dispatcher/entry point.
  * **`src/core/`**: Tweepy API connectors, workflows, and diagnostics.
  * **`src/ui/`**: Clean text and ASCII art terminal interfaces.
  * **`src/utils/`**: Time calculations, tweet weight analyzers, and input validators.
* **`config/`**: Decoupled settings.
  * **`config/settings.py`**: System rates, scheduler configurations, and shared hashtags.
  * **`config/bots/`**: Bot-specific messages and assets settings.
* **`assets/`**: Images categorized by bot/feature.
* **`docs/`**: Local documentation, operations journal, and account credentials.
  * **NOTE:** This folder is ignored in `.gitignore` to prevent sensitive credentials and local history from being pushed online.
* **`.github/workflows/`**: Consolidated GitHub Actions workflows.
  * **`Auto_Post.yml`**: Scheduled runner coordinating all 4 bots via matrix strategy.
  * **`Manual_Post.yml`**: Dispatches manual runs on demand.
  * **`Diagnose_Credentials.yml`**: Runs diagnostics checks on API credentials.

---

## 🚀 How to Run Locally

Install the required dependencies:
```bash
pip install -r requirements.txt
```

Set up your Twitter API credentials in your environment variables:
```bash
$env:CONSUMER_KEY="your_api_key"
$env:CONSUMER_SECRET="your_api_secret"
$env:X_ACCESS_TOKEN="your_access_token"
$env:X_ACCESS_TOKEN_SECRET="your_access_token_secret"
```

### Modes of Execution

#### 1. System Diagnostics Mode
Run verification on the connection API keys, credentials validity, rate limit, and media upload capability:
```bash
python -m src.main --bot greenhaven --mode diagnose
```

#### 2. Manual Posting (Immediate)
Run immediate tweet creation workflow (skipping scheduler cutoff delays):
```bash
python -m src.main --bot greenhaven --mode manual
```

#### 3. Automatic Scheduled Posting
Runs the scheduled queue, waiting for target time and injecting a randomized delay for anti-bot protection:
```bash
python -m src.main --bot greenhaven --mode auto
```

#### 4. Testing (Dry-Run Mode)
To run and inspect the outputs and media preparation locally without posting to live X accounts, append `--dry-run`:
```bash
python -m src.main --bot greenhaven --mode manual --dry-run
```
