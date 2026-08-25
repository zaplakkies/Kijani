---
id: workshops
title: Workshop & Event Organizer's Guide
sidebar_position: 7
---

# Workshop & Event Organizer's Guide

This guide is for educators, STEM instructors, Scout leaders, and event organizers planning to host Kijani battle bot building sessions or competitive tournaments.

Because Kijani is extremely affordable and robust, deploying 10 to 50 bots simultaneously is straightforward when following a structured provisioning workflow.

---

## 1. Bulk Provisioning Workflow

When preparing a large batch of robots, do not flash them randomly. Follow this sequential pipeline:

```text
  ┌─────────────────────────────────────────────────────────────┐
  │ 1. Assemble Kijani Controller Board                         │
  └──────────────────────────────┬──────────────────────────────┘
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │ 2. Flash Core Firmware over USB                             │
  └──────────────────────────────┬──────────────────────────────┘
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │ 3. Run 'pio run -t deployfs' to write LittleFS static pages │
  └──────────────────────────────┬──────────────────────────────┘
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │ 4. Run 'pio run -t qr_gen' to query MAC & create sticker    │
  └──────────────────────────────┬──────────────────────────────┘
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │ 5. Print out sticker sheet & apply to robot chassis         │
  └──────────────────────────────┴──────────────────────────────┘
```

This ensures that every robot is labeled with its exact connection QR code and SSID (e.g., `MootBot_E89F6D`) before distribution to students.

### High-Speed Automation with `qrflashstorm`

Instead of running these steps manually board-by-board, Kijani provides an automated high-speed bulk provisioning tool called **`qrflashstorm`**. This makes deploying large quantities extremely fast and hands-free.

With `qrflashstorm`, you only need to:
1. **Assemble all your units** beforehand.
2. **Install the utility requirements**:
   ```bash
   pip install -r dev_scripts/requirements.txt
   ```
3. **Start the watcher daemon**:
   ```bash
   pio run -t qrflashstorm
   ```
4. **Plug in a board via USB**: The script automatically:
   - Detects the newly-connected board.
   - Compiles and uploads the core firmware.
   - Compiles and uploads the LittleFS static pages.
   - Queries the board's unique MAC address over serial.
   - Generates a Wi-Fi connection QR code and appends/merges it into `assets/qr/stickers.pdf`.
5. **Unplug the board and plug in a new one**: The daemon immediately detects the new device and begins the programming cycle again.
   
By simply swapping USB cables between boards, you can program the entire firmware, filesystem, and generate/append the physical QR codes in record time!

---

## 2. Generating & Printing Sticker Sheets

Do not print single PNG files manually. Kijani includes a PDF compositor tool that merges all generated device stickers into a standard grid format for A4 label sheets:

1. Generate connection PNGs for all completed boards using `pio run -t qr_gen`, or automatically compile them during the `qrflashstorm` workflow.
2. Locate the merging script:
   ```bash
   python dev_scripts/append_qr_to_pdf.py
   ```
   *(Note: `qrflashstorm` calls this automatically to compile stickers into a single PDF sheet in real-time.)*
3. This creates formatted PDFs (like `stickers.pdf` under `assets/qr/`) which you can print onto pre-cut label sheets.
4. Stick each QR directly on the robot's physical armor plate. Participants can immediately join the bot's WiFi by scanning the sticker.

---

## 3. WiFi Environment Management (Multi-Robot Events)

Running multiple WiFi access points in a single room can cause RF interference. Follow these practices during workshops or battles:

* **SSID and Password Uniqueness:** Maintain open networks with unique SSIDs (`MootBot_<MAC>`). Do not make every robot use the exact same SSID, otherwise devices will fail to connect.
* **Disconnect Inactive Bots:** Instruct participants to turn off their robots (`OFF` switch) when not driving or queuing for battles. This frees up the 2.4GHz spectrum.
* **Avoid High Web Traffic:** Encourage users not to leave settings editors or large file upload managers open during match play, keeping the bandwidth clear for real-time motor signals.

---

## 4. Hosting a Tournament

Kijani bots are perfect for combat categories like "Antweight" (150g) and "Beetleweight" (1.36kg).
* **Failsafes:** Advise all competitors to configure their control pages to stop sending motor commands when they close the browser. If a phone is dropped or turned off, the robot will safely halt due to API timeouts or connection losses.
* **Charging Stations:** Set up a centralized charging table with multiple Micro USB cables powered by high-output power hubs. Remind players: **Always turn the switch to OFF during charging** to maximize charging speed.

---

## 5. Development Scripts Directory Explained

The `/dev_scripts` directory contains several utility scripts integrated as custom PlatformIO targets. These scripts automate building, uploading, debugging, and QR generation:

* **`qrflashstorm.py`** (Run via `pio run -t qrflashstorm`):
  An automated serial port polling daemon. Once started, it continuously monitors USB ports for newly connected boards. When a board is detected, it automatically uploads the firmware and filesystem, queries the MAC address over serial, generates a Wi-Fi open connection QR code, and appends it to a centralized `assets/qr/stickers.pdf` file. To stop the daemon, press `Ctrl+C` (or kill the process if the PlatformIO environment intercepts the keyboard interrupt).
* **`append_qr_to_pdf.py`** (Run via `pio run -t append_qr_to_pdf`):
  Detects the connected device, generates its QR code in memory, and appends or overlays it as a labeled grid entry into the PDF sheet `assets/qr/stickers.pdf`.
* **`qr_gen.py`** (Run via `pio run -t qr_gen`):
  Queries the MAC address of the connected board over serial, formats an open Wi-Fi credentials QR payload (`WIFI:T:nopass;S:MootBot_<MAC>;;`), and exports a standalone sticker image to `assets/qr/MootBot_<MAC>.png` containing both the QR code and the SSID text.
* **`deploy.py`** (Run via `pio run -t deploy`):
  A convenience wrapper target that compiles and uploads the firmware (`pio run -t upload`) and then compiles and uploads the LittleFS static files image (`pio run -t deployfs`) in sequence.
* **`deployfs.py`** (Run via `pio run -t deployfs`):
  Compiles and uploads the frontend files and static pages within the `data/` folder as a LittleFS partition image onto the microcontroller.
* **`dev.py`** (Run via `pio run -t dev`):
  Builds and deploys both firmware and filesystem, and immediately starts the PlatformIO serial monitor (`pio device monitor`) for active developer debugging.
* **`requirements.txt`**:
  Lists Python dependencies (including `reportlab`, `pypdf2`, `pillow`, and `qrcode`) needed to run the QR-generation and PDF-appending scripts. Install them with `pip install -r dev_scripts/requirements.txt`.
