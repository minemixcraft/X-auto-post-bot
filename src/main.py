import argparse
import sys
import importlib
from config.settings import SHARED_HASHTAGS, UI_CONFIG

def get_bot_ui():
    from src.ui import terminal as bot_ui
    return bot_ui

def main():
    import sys
    # Configure stdout/stderr to use UTF-8 encoding to prevent UnicodeEncodeError in Windows terminal
    if sys.stdout.encoding != 'utf-8':
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except AttributeError:
            pass
    if sys.stderr.encoding != 'utf-8':
        try:
            sys.stderr.reconfigure(encoding='utf-8')
        except AttributeError:
            pass

    parser = argparse.ArgumentParser(description="Twitter/X Auto-Posting Bot Runner")
    parser.add_argument("--bot", required=True, help="Name of the bot (e.g. greenhaven, moonchill, stray_cat_1, stray_cat_2)")
    parser.add_argument("--mode", required=True, choices=["auto", "manual", "diagnose"], help="Run mode")
    parser.add_argument("--dry-run", action="store_true", help="Run in dry run mode without posting to Twitter API")
    args = parser.parse_args()

    # Load system settings and override dry run if flag is set
    from config import settings
    if args.dry_run:
        settings.SYSTEM_CONFIG["DRY_RUN"] = True

    # Normalize bot name to load bot-specific config
    bot_normalized = args.bot.lower().replace(" ", "_")
    
    # Map normalized names to user-friendly titles
    bot_titles = {
        "greenhaven": "GreenHaven",
        "moonchill": "Moonchill",
        "stray_cat_1": "Stray Cat 1",
        "stray_cat_2": "Stray Cat 2"
    }
    bot_title = bot_titles.get(bot_normalized, args.bot)

    try:
        bot_module = importlib.import_module(f"config.bots.{bot_normalized}")
        bot_data = bot_module.DATA
    except ImportError:
        print(f"❌ Error: Bot configuration for '{args.bot}' (module 'config.bots.{bot_normalized}') not found.")
        sys.exit(1)

    bot_ui = get_bot_ui()
    show_preview = UI_CONFIG.get("SHOW_PREVIEW", True)

    if args.mode == "diagnose":
        from src.core.diagnostics import run_x_diagnostics
        test_image = None
        if "images" in bot_data and len(bot_data["images"]) > 0:
            test_image = bot_data["images"][0]
        run_x_diagnostics(test_image_path=test_image)
    elif args.mode == "auto":
        from src.core.workflow import run_autopost_workflow
        run_autopost_workflow(bot_title, bot_data, SHARED_HASHTAGS, bot_ui, show_preview)
    elif args.mode == "manual":
        from src.core.workflow import run_manual_workflow
        run_manual_workflow(bot_title, bot_data, SHARED_HASHTAGS, bot_ui, show_preview)

if __name__ == "__main__":
    main()
