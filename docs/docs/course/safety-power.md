---
title: Safety and Power Guide
description: Essential guidelines for powering Kijani safely via USB, batteries, and regulators.
sidebar_position: 5
---

# Safety and Power Guide

Working with physical hardware, motors, and rechargeable batteries is incredibly fun, but it requires some basic safety knowledge. Reading this guide will protect both you and your Kijani hardware from accidental damage.

---

## 1. USB Power Limitations

When your Kijani board is connected to a computer via a USB cable, it is powered by the computer's USB port.

* **Current Limits**: Standard computer USB ports can supply a maximum of **500mA (0.5A)**. High-power USB 3.0 or wall adapters can supply **1A to 2A**.
* **Board Resets**: If you run two motors and a servo under heavy load while powered *only* by a computer's USB port, the current draw may exceed 500mA. The computer will limit the current, causing the voltage to drop, which forces the ESP32 to reboot (brownout reset).
* **Safe Practice**: When testing motors or servos, always use a **rechargeable 1S LiPo battery** connected to the board, or use a high-quality USB wall adapter.

---

## 2. Lithium Polymer (LiPo) Battery Safety

Kijani is designed to run on a **1S (single cell) Lithium Polymer battery** (3.7V nominal, 4.2V fully charged). LiPo batteries pack a lot of energy and must be handled with care.

* **Polarity Matters**: Double-check battery connection polarity before plugging it in. Connecting a battery backwards can permanently destroy the charging circuit and microcontroller.
* **Charging**: Kijani has an on-board LiPo charging circuit. When a USB cable is plugged in, it charges the connected battery. The status LED will indicate charging activity.
* **Physical Damage**: Never use a battery that is swollen, dented, punctured, or showing signs of damage. Dispose of it safely according to local environmental rules.
* **Storage**: Do not leave the battery connected to the board for months of inactivity, as it can slowly discharge below its safe minimum threshold (3.0V) and become permanently unusable.

---

## 3. Common Ground Requirements

If you connect external devices (sensors, motor drivers, or controllers) that have their own separate power supplies, you must **connect their Ground (GND) pins to Kijani's GND pin**.

* **Why?** Voltage is relative. To communicate over signal lines (like PWM or Digital I/O), both devices must agree on what `0 Volts` (GND) is.
* **Without Common Ground**: Signals will be noisy, unstable, and might fail to trigger entirely. Worse, floating voltages could damage pins.

---

## 4. Servo & Motor Current

High-torque servos and powerful motors draw significant current, especially when stalled (prevented from rotating).

* **Single Servo Limit**: Kijani is optimized to drive **one servo**. Plugging in two high-power servos simultaneously can overload the regulator, causing thermal shutdown or board resets.
* **Do Not Direct Drive High-Power Motors**: Kijani's onboard H-bridges are designed for small DC motors (such as N20 gear motors) that draw under **1A** at peak stall. Do not connect larger, high-current motors (like standard yellow TT motors or RS-380 motors) directly to the headers; they require an external high-power motor driver.

---

## 5. Wiring Checklist for Safety

Always follow these golden rules:
1. **Power OFF**: Turn off the power switch and unplug the USB cable *before* making or changing any electrical connections on the board.
2. **Double-Check Polarities**: Verify Red (+/VCC) and Black (-/GND) wires before turning power back on.
3. **Avoid Short Circuits**: Ensure exposed wire strands or metal components do not touch other pins or pads on the board while power is connected.
