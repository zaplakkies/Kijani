---
title: "Lesson 13: Servo Connections"
description: Learn how RC servos work and how to safely connect them to Kijani.
sidebar_position: 1
---

# Lesson 13: Servo Connections

In this lesson, you will learn what an RC servo motor is, how it differs from a standard DC motor, and how to safely wire it to Kijani without causing board resets.

---

## What you will learn
* What a servo motor is and how it works.
* How a microcontroller controls servo position.
* Why servo wiring polarity is absolutely critical.
* Why servos can cause power resets if connected incorrectly.

---

## What you need
* **1 × Kijani Controller Board**
* **1 × 1S LiPo Battery** (charged, connected)
* **1 × Standard RC Servo** (e.g. SG90 micro-servo)

---

## Background

### What is a Servo Motor?
Unlike a standard DC motor that spins continuously, a **Servo Motor** is a smart positioning device. Inside the tiny plastic casing, it contains:
1. A small DC motor.
2. A feedback potentiometer (sensor) to measure the shaft's angle.
3. A control circuit.
4. Reduction gears to increase torque.

When you send a target angle (typically **`0` to `180` degrees**) to the servo, its internal brain compares the target angle to its current angle and drives its motor until they match.

### Position Control via Pulses
Microcontrollers control servos by sending a repeating pulse. The **width** of this pulse (ranging from 1 millisecond to 2 milliseconds) tells the servo where to go:
* **1.0 ms pulse**: Move to `0` degrees.
* **1.5 ms pulse**: Move to `90` degrees (center).
* **2.0 ms pulse**: Move to `180` degrees.

Kijani's firmware manages this pulsing automatically behind the scenes.

---

## Connect it

:::danger[Polarity Check]
Servo connectors are standard 3-pin plugs, but they can easily be plugged in backwards. Reversing a servo connector can instantly burn out the servo or force the Kijani board to reset!
:::

1. Ensure Kijani is powered **OFF**.
2. Identify your servo's wire colors:
   * **Brown / Black**: Ground (GND)
   * **Red**: Positive Power (VCC / HV)
   * **Yellow / Orange / White**: Signal (SIG)
3. Locate the **Servo 1** header on Kijani.
4. Align the **Brown/Black** wire with Kijani's **GND** pin (the square pin).
5. Plug the connector firmly onto the header.

---

## Try it

Let's command the servo directly.

### Step 1: Position to Center (90 degrees)
Open your browser and enter:

`http://10.10.10.10/processcontrol?S1=90`

The servo shaft will move to its exact center position!

### Step 2: Position to Minimum (0 degrees)
Now enter:

`http://10.10.10.10/processcontrol?S1=0`

The servo rotates to its limit.

### Step 3: Position to Maximum (180 degrees)
Try:

`http://10.10.10.10/processcontrol?S1=180`

The servo rotates all the way to its other limit.

---

## What should happen
* Sending values between `0` and `180` forces the servo horn to pivot instantly to that exact angular position.
* The servo holds its position firmly—it will physically resist if you try to turn the horn with your fingers.

---

## Experiment
Try sending intermediate angles, like `45` or `135` degrees, and observe the resulting angular position of the servo horn.

---

## Troubleshooting
* **Servo hums but doesn't move?** The servo might be trying to rotate beyond its physical stops. Do not drive it past its limits (standard micro-servos can occasionally jam if driven below 5 or above 175 degrees).
* **Board resets when servo moves?** Servos draw a sudden burst of current when starting. If your battery is low, this will trigger a brownout reset. Charge your battery or use a robust external power source.

---

## Next step
Now that your servo is wired and working, let's build a beautiful web dashboard with sliders and preset buttons to control the servo dynamically!

👉 **[Lesson 14: Controlling a Servo from the Web](./14-web-servo.md)**
