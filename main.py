"""
main.py — Command Nexus Entry Point

Command Nexus is a modular all-in-one utility platform built to centralize
backups, diagnostics, recovery tools, automation, maintenance, and advanced
system management into a unified command-driven environment.

Usage:
    python main.py
"""

import sys
import os

from Config.settings import SETTINGS

# ---------------------------------------------------------------------------
# Version and identity (single source of truth lives in Config/settings.py)
# ---------------------------------------------------------------------------
APP_NAME = SETTINGS["app_name"]
APP_VERSION = SETTINGS["app_version"]


def clear_screen():
    """Clear the terminal screen on Windows and Unix-like systems."""
    os.system("cls" if os.name == "nt" else "clear")


def print_banner():
    """Display the Command Nexus banner."""
    print("=" * 50)
    print(f"  {APP_NAME}  v{APP_VERSION}")
    print("  Modular Utility Platform")
    print("=" * 50)
    print()


def print_menu():
    """Display the main navigation menu."""
    print("Main Menu")
    print("-" * 30)
    print("  1. Backups")
    print("  2. Diagnostics")
    print("  3. Recovery Tools")
    print("  4. Automation")
    print("  5. Maintenance")
    print("  6. Device Management")
    print()
    print("  0. Exit")
    print("-" * 30)


def handle_choice(choice: str) -> bool:
    """
    Process the user's menu selection.

    Returns False when the user chooses to exit (option 0),
    True otherwise so the main loop can continue.
    """
    if choice == "0":
        print("\nExiting Command Nexus. Goodbye!")
        return False

    # --- Placeholder handlers (to be replaced with real module calls) ------
    handlers = {
        "1": "Backups module — coming soon.",
        "2": "Diagnostics module — coming soon.",
        "3": "Recovery Tools module — coming soon.",
        "4": "Automation module — coming soon.",
        "5": "Maintenance module — coming soon.",
        "6": "Device Management module — coming soon.",
    }

    if choice in handlers:
        print(f"\n  {handlers[choice]}")
    else:
        print("\n  Invalid option. Please try again.")

    input("\n  Press Enter to continue...")
    return True


def main():
    """Main application loop."""
    while True:
        clear_screen()
        print_banner()
        print_menu()

        try:
            choice = input("Select an option: ").strip()
        except (KeyboardInterrupt, EOFError):
            # Allow Ctrl+C or EOF to exit gracefully
            print("\n\nInterrupted. Exiting Command Nexus.")
            sys.exit(0)

        if not handle_choice(choice):
            break


if __name__ == "__main__":
    main()
