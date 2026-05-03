# Config/__init__.py
#
# This package exposes the application configuration to all other modules.
# Import settings from here rather than reading files directly in core modules.

from Config.settings import SETTINGS

__all__ = ["SETTINGS"]
