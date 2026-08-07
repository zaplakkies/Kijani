# Kijani Robot — Web Programming Guide
Firmware & Web Interface Updates via ESP32 Web Interface

Author: Marc d’Hotman de Villiers  
Project: Kijani Robotics Platform  
Version: V1 (Draft)

---

# 1. Overview

The Kijani robot supports **fully remote updates** of both:

- ⚙️ Firmware (.bin file)
- 🌐 Web interface files (HTML / JS / CSS)

This allows users to:
- Update robot behaviour without USB
- Modify control interfaces from a browser
- Deploy custom control systems per mission or event

The system is designed around an ESP32 running:
- OTA firmware partitions (app0/app1)
- LittleFS filesystem for web assets
- Async web server for file handling

---

# 2. System Architecture

## 2.1 Flash Layout

| Partition | Type | Purpose |
|-----------|------|---------|
| app0 | OTA firmware | Firmware slot A |
| app1 | OTA firmware | Firmware slot B |
| LittleFS | Filesystem | Web pages + assets |
| NVS | Storage | Settings |

---

## 2.2 Separation of Responsibilities

| Component | Stored in | Updated via |
|-----------|----------|-------------|
| Firmware | app0 / app1 | `/updatefirmware` |
| Web UI | LittleFS | `/upload` |
| Settings | NVS | `/updatesettings` |

---

# 3. Connecting to the Robot

## 3.1 WiFi Access Point Mode

On startup, the robot creates a WiFi network:


MootBot_xxxx


Connect using:
- Password: configured in settings (or default if new device)

Then open browser:


http://10.10.10.10


---

# 4. Web Interface Overview

The web interface provides:

- File manager (LittleFS)
- Firmware updater (OTA)
- Control panel (motors + servos)
- Settings editor
- System diagnostics

---

# 5. Firmware Update (OTA)

## 5.1 Purpose

This feature updates the robot’s **core firmware** without USB.

---

## 5.2 How It Works

- Uploads a `.bin` file
- Writes to inactive OTA partition (app0 or app1)
- Switches boot partition automatically
- Reboots system

---

## 5.3 Requirements

- File must be a valid ESP32 firmware `.bin`
- Must match current partition scheme
- Stable power supply required during update

---

## 5.4 Where is this bin file


- if you build the project on platformio/vscode it can be found in .pio/build/esp32/firmware.bin
- if you just want to update from the git repo the firmware can be found in the binary folder


---

## 5.5 Web Usage Flow

1. Open firmware update page
2. Select `firmware.bin`
3. Click upload
4. Wait for confirmation
5. Device reboots automatically

---

## 5.6 Safety Notes

Before updating firmware:
- Stop all motors
- Avoid physical load on system
- Ensure battery voltage is stable

---

# 6. Web Interface Update (LittleFS)

## 6.1 Purpose

Allows updating:
- HTML pages
- JavaScript
- CSS files
- images/icons

---

## 6.2 Danger


This is how you brick the unit, make sure you know what you are doing as overwriting key files like index.html will mean you will need to fix it by doing an upload via the usb cable. There are no safeguards to stop you doing something stupid. If you do want to update the index.html file its recommended that you download it and then reupkload it as another name so if the new index.html is broken you can still use the old one under the different name.


---

## 6.3 How It Works

- File is streamed to ESP32
- Stored directly into LittleFS
- Immediately available after upload

---

## 6.4 Example Usage

Go to index.html, select the file to upload and click upload.

---

## 6.5 File Access

Files are served automatically:


http://10.10.10.10/index.html
http://10.10.10.10/control.html
...

Default file:

index.html


---

# 7. Best Practices
## 7.1 Firmware updates
- Always test locally first
- Ensure battery is stable
- Avoid motor load during flashing

## 7.2 Web updates
- Keep file sizes small
- Avoid blocking JS
- Use async fetch calls

Users are encouraged to build their own control interfaces using the provided API.