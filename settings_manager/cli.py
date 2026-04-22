import argparse
import json
from settings_manager.registry import delete_settings, load_settings, save_settings
from settings_manager.settings import Settings


def cmd_save(args: argparse.Namespace) -> None:
    current = load_settings()
    updated = Settings(
        theme=args.theme or current.theme,
        language=args.language or current.language,
        window_width=args.width or current.window_width,
        window_height=args.height or current.window_height,
    )
    save_settings(updated)
    print("Settings saved.")
    print(json.dumps(updated.to_dict(), indent=2))


def cmd_load(args: argparse.Namespace) -> None:
    settings = load_settings()
    print(json.dumps(settings.to_dict(), indent=2))


def cmd_reset(args: argparse.Namespace) -> None:
    delete_settings()
    print("Settings reset to defaults.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="settings_manager",
        description="Manage application settings stored in the Windows registry.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # save
    save_parser = subparsers.add_parser("save", help="Save settings")
    save_parser.add_argument("--theme", help="UI theme (e.g. light, dark)")
    save_parser.add_argument("--language", help="Language code (e.g. en, fr)")
    save_parser.add_argument("--width", type=int, help="Window width in pixels")
    save_parser.add_argument("--height", type=int, help="Window height in pixels")
    save_parser.set_defaults(func=cmd_save)

    # load
    load_parser = subparsers.add_parser("load", help="Load and print current settings")
    load_parser.set_defaults(func=cmd_load)

    # reset
    reset_parser = subparsers.add_parser("reset", help="Delete saved settings")
    reset_parser.set_defaults(func=cmd_reset)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)
