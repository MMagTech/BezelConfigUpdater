# Recursive Config File Updater

This Python script scans `.cfg` files in the folder it is placed in, including all subdirectories, and replaces a specified string with a user-provided replacement path. It's designed for use cases like updating paths in configuration files for RetroPie or other similar projects.

---

## Features

- Recursively processes all `.cfg` files in the directory and its subdirectories.
- Replaces occurrences of a default target string (`/opt/retropie/configs/all/retroarch/overlay/ArcadeBezels/`) with a user-defined path.
- Ensures only `.cfg` files are modified.
- Provides clear logs of which files were updated and which files required no changes.

---

## Requirements

- **Python 3.6 or newer**
- Runs on **Windows**, **Linux**, and **macOS**.

---

## How to Use

### 1. Download the Script
Clone the repository or download the script directly:

```bash
git clone https://github.com/your-username/your-repo-name.git

### 2. Download the Script
