# Recursive Config File Updater

This Python script scans necessary `.cfg` files in the folder it is placed in, including all subdirectories, and replaces a specified string with a user-provided replacement path. It's designed for use cases like updating overlay .cfg's paths in configuration files for RetroPie or other similar projects. Includes all MAME overlays for FB Alpha, FinalBurn Neo, MAME, MAME 2003 (0.78), MAME 2003-Plus and MAME 2010. 

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

### 2. Inside the retroarch folder you will find the 'Run This to Update CFGs.py' script

### 3. Run the script and it will ask you to, "Enter the Replacement path:" in my case it is /storage/E7BF-C3B1/RetroArch/overlay/ArcadeBezels/ this is the retroarch location where you will store the overlays and configs in the next step 

### 4. Drag the config and overlay folders to the correct location of your RetroArch install
