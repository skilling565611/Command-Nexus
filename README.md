# Command Nexus

**Command Nexus** is a modular all-in-one utility platform built to centralize
backups, diagnostics, recovery tools, automation, maintenance, and advanced
system management into a unified command-driven environment.

---

## Features (Planned)

| Module | Description |
|---|---|
| **Backups** | Create, schedule, and restore system/data backups |
| **Diagnostics** | Health checks, system info, and performance reports |
| **Recovery Tools** | File recovery, repair utilities, and restore points |
| **Automation** | Script runner, task scheduler, and workflow engine |
| **Maintenance** | Disk cleanup, log rotation, and system optimisation |
| **Device Management** | Inventory, monitoring, and remote actions |

---

## Project Structure

```
Command-Nexus/
├── Core/           # Core modules — one sub-module per feature area
├── Config/         # Application configuration and settings
├── Docs/           # Project documentation and guides
├── Logs/           # Runtime log files (not committed to Git)
├── Scripts/        # Standalone helper scripts and automation utilities
├── Tools/          # Shared utility functions used across modules
├── Backups/        # Backup archives created at runtime (placeholder)
├── main.py         # Application entry point — run this to start
├── README.md       # Project overview (this file)
└── LICENSE         # Apache 2.0 licence
```

---

## Getting Started

**Requirements:** Python 3.8 or later — no third-party packages needed.

```bash
# Clone the repository
git clone https://github.com/skilling565611/Command-Nexus.git
cd Command-Nexus

# Launch the platform
python main.py
```

---

## Usage

Command Nexus is operated entirely from the terminal.  
After launching you will see a numbered menu:

```
==================================================
  Command Nexus  v0.1.0
  Modular Utility Platform
==================================================

Main Menu
------------------------------
  1. Backups
  2. Diagnostics
  3. Recovery Tools
  4. Automation
  5. Maintenance
  6. Device Management

  0. Exit
------------------------------
Select an option:
```

> **Exit is always option 0.**

---

## Roadmap

- [x] Initial project scaffold
- [ ] Logging infrastructure
- [ ] Backup module (local file backups)
- [ ] Diagnostics module (CPU, memory, disk)
- [ ] Recovery Tools module
- [ ] Automation / script runner
- [ ] Maintenance utilities
- [ ] Device Management module
- [ ] Optional GUI layer

---

## Contributing

1. Fork the repository and create a feature branch.
2. Keep each module isolated inside its own folder under `Core/`.
3. Use only the Python standard library unless a third-party package is
   explicitly approved and added to `requirements.txt`.
4. Submit a pull request with a clear description of your changes.

---

## Licence

Distributed under the **Apache License 2.0**.  
See [`LICENSE`](LICENSE) for full terms.
