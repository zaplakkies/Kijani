---
id: revisions
title: Hardware Revisions
sidebar_position: 3
---

# Hardware Revisions

Kijani has evolved through several hardware iterations to optimize power delivery, safety, and assembly ease.

## Revision Summary

| Board Version | Main Processor | Key Features / Changes | Status |
| :--- | :--- | :--- | :--- |
| **V1** | ESP32-WROOM-32E | Initial prototype. Had software-controlled enable lines for 5V and 8V rails. | Deprecated |
| **V2** | ESP32-WROOM-32E | Removed `en5v` and `en8v` lines (rails always enabled for simplicity). Added dedicated servo support. | Legacy |
| **V3** | ESP32-WROOM-32E | Added `dvrsleep` pin pull-down logic, revised battery ADC divider circuit, improved boost converter isolation, added helper headers and custom polarity labels on silk. | **Current Production** |

---

## Pinout Mapping Table

Use the following reference for pin mappings inside your custom firmware modifications.

| Pin Name | Function | ESP32 GPIO | Active State / Details |
| :--- | :--- | :--- | :--- |
| `BUILTIN_LED` / `statled` | Status Indicator LED | **GPIO 2** | `HIGH` = ON |
| `MotorA1` | Motor A PWM | **GPIO 32** | Speed control PWM (1kHz) |
| `MotorA2` | Motor A Direction | **GPIO 33** | `LOW` = Forward, `HIGH` = Reverse |
| `MotorB1` | Motor B PWM | **GPIO 25** | Speed control PWM (1kHz) |
| `MotorB2` | Motor B Direction | **GPIO 26** | `LOW` = Forward, `HIGH` = Reverse |
| `servo1Pin` | Servo 1 Signal | **GPIO 27** | PWM Output (50Hz) |
| `servo2Pin` | Servo 2 Signal | **GPIO 14** | PWM Output (50Hz) |
| `Vmod1` | Pulled low or left floating | **GPIO 15** | Used to change the output voltage |
| `Vmod2` | Pulled low or left floating | **GPIO 13** | Used to change the output voltage |
| `pgm` | Recovery Pin | **GPIO 5** | Short to Ground on boot to restore settings |
| `en8v` (Deprecated) | 8V Rail Enable | **GPIO 16** | Pulled from V2/V3 designs (always on) |
| `en5v` (Deprecated) | 5V Rail Enable | **GPIO 17** | Pulled from V2/V3 designs (always on) |

---

## Detailed Version Differences

### V3 Improvements (August 2026)
* **Motor Sleep Control:** Added `dvrsleep` pin control on GPIO 12. If your robot is in standby or charging, you can pull this pin `LOW` to disable the motor driver chip completely, which saves battery and prevents spurious motor vibrations under USB serial loading.
* **Boost Voltage Safety:** Improved separation of the boost voltage regulator to protect servos. On-board markings are enhanced: `gnd` (brown/black), `hv` (red), `servo1` (yellow/white).
* **Enhanced Polarity Silkscreen:** Clearer `+` and `-` labeling on the PCB silkscreen to prevent reverse-polarity battery connection disasters.

### V2 Improvements (May 2026)
* Simplified power architecture by making the 5V and 8V lines direct, removing the need to manage GPIO 16 and 17 to keep the rails alive.
