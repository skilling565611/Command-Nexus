"""
Config/settings.py — Application-wide configuration for Command Nexus.

All tunable values live here so that modules never hard-code paths or
preferences.  Keys can be overridden later by reading a user config file
(e.g. JSON or INI) without changing any other source file.
"""

import os

# ---------------------------------------------------------------------------
# Application metadata
# ---------------------------------------------------------------------------
APP_NAME = "Command Nexus"
APP_VERSION = "0.1.0"

# ---------------------------------------------------------------------------
# Directory paths (relative to the project root)
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PATHS = {
    "core":    os.path.join(BASE_DIR, "Core"),
    "config":  os.path.join(BASE_DIR, "Config"),
    "docs":    os.path.join(BASE_DIR, "Docs"),
    "logs":    os.path.join(BASE_DIR, "Logs"),
    "scripts": os.path.join(BASE_DIR, "Scripts"),
    "tools":   os.path.join(BASE_DIR, "Tools"),
    "backups": os.path.join(BASE_DIR, "Backups"),
}

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
LOG_FILE = os.path.join(PATHS["logs"], "command_nexus.log")
LOG_LEVEL = "INFO"  # DEBUG | INFO | WARNING | ERROR | CRITICAL

# ---------------------------------------------------------------------------
# Consolidated settings dict (importable by other modules)
# ---------------------------------------------------------------------------
SETTINGS = {
    "app_name":    APP_NAME,
    "app_version": APP_VERSION,
    "base_dir":    BASE_DIR,
    "paths":       PATHS,
    "log_file":    LOG_FILE,
    "log_level":   LOG_LEVEL,
}
