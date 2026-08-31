---
title: Hardware Reference Guide
description: Physical layout, pins, connectors, and specifications of the Kijani controller.
sidebar_position: 3
---

# Hardware Reference Guide

This reference guide documents the physical layout, connector labels, and pin numbers of the Kijani ESP32 Controller Board. It is your go-to reference when wiring up lessons or building custom projects.

---

## Board Layout & Connectors

Below is an overview of the main components and pin connections on the Kijani board.

![board image](../../../../hardware/v3/mootbotv3header.png)

---

## ESP32 Pin Allocation Table

| Function | ESP32 GPIO Pin | Description |
| :--- | :--- | :--- |
| **Motor A1** | GPIO 32 | Motor 1 (Left Motor) Control Pin 1 |
| **Motor A2** | GPIO 33 | Motor 1 (Left Motor) Control Pin 2 |
| **Motor B1** | GPIO 25 | Motor 2 (Right Motor) Control Pin 1 |
| **Motor B2** | GPIO 26 | Motor 2 (Right Motor) Control Pin 2 |
| **Servo 1** | GPIO 27 | Servo Channel 1 PWM Signal |
| **Servo 2** | GPIO 14 | Servo Channel 2 PWM Signal |
| **Status LED** | GPIO 2 | Blue On-board LED (Blinks for Wi-Fi status, heartbeat, errors) |
| **PGM Button** | GPIO 5 | Pin used for Factory Reset / Boot Control |
| **Battery Level** | GPIO 36 (ADC1_CH0) | Analog Input measuring battery level via a voltage divider |
| **Voltage Boost 1 (Vmod1)** | GPIO 15 | Adjusts voltage output for servos/motors |
| **Voltage Boost 2 (Vmod2)** | GPIO 13 | Adjusts voltage output for servos/motors |
| **A1** | GPIO36 | used externally as analog input or gpio|
| **A3** | GPIO35 | used externally as analog input or gpio|
| **X** | GPIO4 | used externally as gpio|

---

## Power and Voltage Configurations

The Kijani board features an on-board boost converter that can step up voltage for motors and servos. The boost level is controlled dynamically via settings stored in the preferences or selected through the web interface.

| Boost Level | Target Voltage | Control State | Description |
| :---: | :---: | :--- | :--- |
| **Level 1** | **5.0 V** | Vmod1: INPUT, Vmod2: INPUT | Safe default level for USB or standard setups. |
| **Level 2** | **6.0 V** | Vmod1: LOW (Output), Vmod2: INPUT | Better speed and torque for standard servos and N20 motors. |
| **Level 3** | **8.0 V** | Vmod1: INPUT, Vmod2: LOW (Output) | High speed for motors. Monitor motor temperature! |
| **Level 4** | **9.0 V** | Vmod1: LOW, Vmod2: LOW | Maximum power boost. Use with caution to avoid burning components. |

---

## Board Revisions

* **Version 3.0+**: Current production board. Standardizes on an on-board boost converter controlled via `Vmod1` and `Vmod2`. Includes dual servo and motor headers, USB-C, and robust battery charging.
* **Version 2.0**: Relied on external power regulators or passive voltage lines. Ensure you know your board version before turning boost settings too high!
