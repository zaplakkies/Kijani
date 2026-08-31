---
title: Connection Examples
description: Quick wiring diagrams for motors, servos, speakers, switches, and sensors.
sidebar_position: 4
---

# Connection Examples

This page provides standard wiring configurations and ASCII connection diagrams for Kijani. Use these as a reference when wiring up your robot.

---

## 1. Kijani + Single Motor

Connect a small DC motor (e.g., N20 gear motor) to Motor 1 (Left) or Motor 2 (Right).

```text
    Kijani Motor 1 Header       Motor
    +-------------------+      +-----+
    | Pin A1 [ O ] <=========> | Pin |
    | Pin A2 [ O ] <=========> | Pin |
    +-------------------+      +-----+
```

*Note: DC motor polarity doesn't have a strict positive or negative. Swapping the wires simply reverses the spin direction.*

---

## 2. Kijani + Two Motors (Differential Drive Robot)

Standard dual-motor connection for wheeled robots.

```text
       Kijani Controller Board
    +---------------------------+
    | [ MOTOR 1 ]   [ MOTOR 2 ] |
    |  A1    A2      B1    B2   |
    +---|-----|-------|-----|---+
        |     |       |     |
      +---------+   +---------+
      |  Left   |   |  Right  |
      |  Motor  |   |  Motor  |
      +---------+   +---------+
```

---

## 3. Kijani + Servo Motor

Servos have a 3-pin cable. Pay careful attention to wire colors so you don't connect power backwards.

```text
    Kijani Servo 1 Header     Servo Wire Color      Servo Motor
    +--------------------+    ================      +---------+
    | GND   [ O ] <========== Brown / Black ======> | (GND)   |
    | HV    [ O ] <========== Red ================> | (VCC)   |
    | SIG   [ O ] <========== Yellow / Orange ====> | (Signal)|
    +--------------------+                          +---------+
```

:::danger[Servo Polarity Warning]
Plugging a servo in backwards (connecting Red/Positive to GND) can immediately damage the servo or reset your Kijani board. Ensure the brown/black wire goes to the square pin/GND.
:::

---

## 4. Kijani + Speaker / Piezo Buzzer

Sound is played by vibrating **Motor 1 (Left)**. You can connect a piezo buzzer or a small speaker directly to the Motor 1 output header.

```text
    Kijani Motor 1 Header       Piezo Buzzer / Speaker
    +-------------------+      +---------------------+
    | Pin A1 [ O ] <=========> | Positive (+) / Red  |
    | Pin A2 [ O ] <=========> | Negative (-) / Black|
    +-------------------+      +---------------------+
```

---

## 5. Kijani + Button or Bumper Switch

A simple push button or bumper switch can be connected between a digital input pin and Ground. Kijani's GPIO pins can use internal pull-up resistors, meaning the pin reads `HIGH` (1) normally and `LOW` (0) when pressed.

```text
    Kijani GPIO Pin             Bumper / Button Switch
    +-------------------+      +---------------------+
    | GPIO Pin  [ O ] <======> | Terminal 1 (NO)     |
    | GND       [ O ] <======> | Terminal 2 (COM)    |
    +-------------------+      +---------------------+
```

---

## 6. Kijani + External Analog Sensor (e.g., LDR Light Sensor)

If you are using a sensor, wire it as a voltage divider using a resistor (e.g., 10k ohm) connected to power and ground, and the middle node to an analog input (e.g., GPIO 36 or other free ADC pins).

```text
         3.3V Power
             |
         [ Sensor ] (LDR, etc.)
             |
             +----===> to Kijani ADC Pin (e.g. GPIO 36)
             |
         [ 10k Resistor ]
             |
            GND
```
