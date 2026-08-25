---
id: architecture
title: Firmware Architecture Deep Dive
sidebar_position: 3
---

# Firmware Architecture Deep Dive

Understanding how the Kijani C++ firmware runs on the dual-core ESP32 is essential for making safe and responsive customizations.

---

## 1. Dual-Core Task Allocation (FreeRTOS)

To ensure that network communication (WiFi and Web Server) does not interfere with critical physical motor controls, the firmware divides work across the ESP32’s dual cores using FreeRTOS.

```text
               ┌──────────────────────────────────────┐
               │              ESP32 CPU               │
               └──────────────────┬───────────────────┘
                                  │
         ┌────────────────────────┴────────────────────────┐
         ▼                                                 ▼
     Core 0 (Task 2: Radio & Server)                 Core 1 (Task 1: Physical Controls)
     - ESPAsyncWebServer (Port 80)                   - Motor PWM generation (ledc)
     - WiFi Access Point management                  - Servo pulse management (50Hz)
     - LittleFS file streaming                       - Battery & NTC Thermal Sensor ADCs
     - OTA firmware upgrades                         - Status LED heartbeat routines
```

This prevents the robot from losing control or locking its motors if a large file is uploaded or many web clients request telemetry simultaneously.

---

## 2. Using Motors as Loudspeakers (RTTTL)

A prominent hardware feature is Kijani's lack of a physical buzzer component. Instead, it plays startup tunes, warning beeps, and factory reset melodies directly through the **DC motor coils**!

### How it works:
1. DC motors spin when low-frequency power is applied. However, if you apply high-frequency PWM vibrations (e.g., between 100Hz and 2000Hz), the motor shaft cannot turn fast enough due to mechanical inertia.
2. Instead, the electrical energy is converted into vibrations in the copper windings and motor case, acting exactly like an electromagnetic loudspeaker.
3. The firmware parses Ring Tone Transfer Language (RTTTL) strings (the standard formatting for old Nokia ringtones) and plays them by driving the PWM frequency (`ledcWriteTone`) on the motor pins.

### Tuning configuration in `main.cpp`:
```cpp
// Startup jingle definition in RTTTL format
String startup = "Jingle:d=4,o=5,b=100:8b,16d6,16c6,8e6";

// Play routine executes non-blocking RTTTL parses
playRTTTL(startup.c_str());
```

:::warning[Coil Heating]
Because the energy is dissipated as vibration and heat in the motor windings, avoid playing long tunes or high-duty tones indefinitely, as it can heat up N20 gear motors.
:::

---

## 3. Configuration & Non-Volatile Storage (NVS)

Kijani uses the ESP32's **Preferences** library to store user-defined configurations across power cycles. This data is written into the ESP32's non-volatile system partition (NVS), meaning settings survive firmware re-flashing!

### Stored Parameters:
* **`AP`**: The SSID string of the access point (Default: `MootBot_<ID>`).
* **`APpass`**: The WPA2 password (Default: empty / open network).
* **`startupTune`**: The RTTTL tune string played on boot.
* **`batteryCalibrationFactor`**: Floating-point value converting raw ADC reads to actual volts (Default: `~0.02352` or `5.02 / 213.0`).
* **`MaxMotor1` / `MaxMotor2`**: Power limits to prevent over-driving specific motors.
* **`SwapMotors`**: Boolean parameter to swap the left/right motor assignments in software.
* **`SwapDirectionMotor1` / `SwapDirectionMotor2`**: Boolean flags to invert forward/reverse logic without physical rewires.

---

## 4. Battery Calibration & Voltmeter

Kijani reads its battery voltage through an on-board resistor divider connected to an ADC pin.
* Due to variations in resistor tolerances and ESP32 ADC non-linearity, the raw reading is multiplied by `batteryCalibrationFactor`.
* You can adjust this value on the **Settings** page so your browser displays an extremely accurate live battery level under the `/quickstatus` endpoint.
