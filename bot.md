# X Auto-Posting Bot: Antigravity Initialization & System Rules

## 1. Project Overview
This project contains a suite of automated and manual posting bots for multiple Twitter/X accounts (GreenHaven, Moonchill, Stray Cat 1, Stray Cat 2) running locally or via GitHub Actions.

## 2. Clean Architecture Guidelines
The codebase has been refactored to follow **Clean Architecture** and **Separation of Concerns**. When writing, modifying, or creating new files, strictly adhere to this structure:

### `src/` (Core Application Logic)
*   **`src/main.py`**: Unified Command-Line (CLI) dispatcher/entry point. Do not put business logic here.
*   **`src/core/`**: Tweepy API connectors, workflows, scheduling mechanisms, and diagnostics.
*   **`src/ui/`**: Terminal interfaces (clean text and ASCII art versions). No API calls should be made from the UI layer.
*   **`src/utils/`**: Time calculations, validators, analyzers, and independent helpers.

### `config/` (Settings & Data)
*   **`config/settings.py`**: System rates, global configurations, and shared hashtags.
*   **`config/bots/`**: Bot-specific messages, assets, and unique configurations.

### `assets/` (Media)
*   Contains images categorized by bot/feature. No code belongs here.

### `docs/` (Documentation)
*   Centralized documentation (accounts, diagnostics history, suspension rules).

## 3. General Coding Rules
-   **Python Standard**: Ensure all code is modular, type-hinted, and adheres to PEP 8 standards.
-   **No Hardcoding**: All API keys, tokens, and sensitive data MUST be read from environment variables or decoupled `.env` files.
-   **Separation of Concerns**: Never mix UI rendering with API requesting logic. Keep the `core/` isolated.
-   **Execution Modes**: New features should support testing (dry-run mode) to verify execution before posting to live accounts.

## 4. How Antigravity Should Assist
When requested to add a new bot or feature:
1.  **Read this document** for structural context.
2.  Add bot-specific configurations to `config/bots/`.
3.  Add media to `assets/<bot_name>/`.
4.  Modify `src/core/workflow.py` and `src/main.py` to route the new bot.
5.  Always verify imports and adhere to the established Clean Architecture layer separation.
