---
id: developer-tools
title: Developer Tooling & Automation
sidebar_position: 2
---

import { CpuIcon } from '@phosphor-icons/react';

# Developer Tooling & Automation

The Kijani repository includes automated developer workflows integrated directly into **PlatformIO** and **SCons** scripts. These scripts help compile static assets, flash filesystems, read board parameters, and generate QR stickers for physical robots.

---

## 1. Custom PlatformIO Targets

Instead of manually running secondary Python scripts, Kijani registers these functions as native PlatformIO targets. You can run them using the PlatformIO sidebar or via the command line.

### `deployfs` (Deploy Filesystem)
Builds and uploads the `/data` folder contents to the ESP32 partition as a LittleFS image.
* **Command:**
  ```bash
  pio run -t deployfs
  ```
* **Under the Hood:**
  It compiles the `/data` folder using the custom `littlefsbuilder.py` parameters and then runs the `uploadfs` target to program the chip.

### `qr_gen` (QR Connection Sticker Generator)
Detects a USB-connected robot, pulls its hardware MAC address over serial, and exports an auto-connect Wi-Fi QR sticker image.
* **Command:**
  ```bash
  pio run -t qr_gen
  ```
* **Under the Hood:**
  1. Detects the correct serial port (e.g., `/dev/ttyUSB0` or `COM3`).
  2. Runs `esptool.py` (or uses native serial commands) to query the ESP32’s physical MAC address.
  3. Automatically computes the SSID based on the standard naming convention: `MootBot_<MAC>`.
  4. Renders a combined sticker PNG image at `assets/qr/MootBot_<MAC>.png` containing a Wi-Fi connection QR payload (`WIFI:T:nopass;S:MootBot_<MAC>;;`) and the text label.

---

## 2. LittleFS Builder Script (`littlefsbuilder.py`)

ESP32 development with PlatformIO historically uses SPIFFS or LittleFS. Kijani standardizes on **LittleFS** for high performance and reliability.

The SCons file `littlefsbuilder.py` is included in the project root to override PlatformIO's default filesystem tool:
```python
Import("env")
env.Replace( MKSPIFFSTOOL=env.get("PROJECT_DIR") + '/mklittlefs' )
```

When you compile a filesystem image, PlatformIO will execute the pre-built `mklittlefs` binary included in the repository rather than standard tooling, ensuring exact partition layout compatibility.

---

## 3. Advanced Developer Scripts (`/dev_scripts`)

The `/dev_scripts` directory contains helper tools for deployment and production flashing:

* **`qr_gen.py`**: The core generator that registers the `qr_gen` target.
* **`append_qr_to_pdf.py`**: A batch utility that scans generated PNG stickers in `assets/qr/` and compiles them into printable sticker sheets (matching A4 sheets). Excellent for organizing large events!
* **`requirements.txt`**: List of Python requirements for running these generator scripts. To install them, run:
  ```bash
  pip install -r dev_scripts/requirements.txt
  ```
