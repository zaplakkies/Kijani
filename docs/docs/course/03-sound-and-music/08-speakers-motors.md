---
title: "Lesson 8: Speakers and Motors"
description: Explore the physical science of electromagnetism, speakers, and motors as audio reproducers.
sidebar_position: 2
---

# Lesson 8: Speakers and Motors

In this lesson, we will explore the fascinating crossover between motion and sound. You will learn how electromagnetism allows a standard DC motor to act exactly like a speaker cone, and why different audio devices require different drive circuits.

---

## What you will learn
* How electromagnets are used in both speakers and motors.
* Why a motor can physically play music.
* How Kijani's firmware exploits this to make sounds.
* The electrical differences between speakers, motors, and piezo buzzers.
* Why motors and speakers need different drive circuitry.

---

## What you need
* **1 × Kijani Controller Board** (powered ON)
* **1 × Small DC Motor** (e.g. N20 gear motor)
* **1 × Small 8-Ohm Speaker** (optional, for comparison)

---

## Background

### Electromagnetism: The Common Thread
Both DC motors and audio speakers rely on the same fundamental law of physics: **electromagnetism**.
1. **Speakers**: A coil of wire (voice coil) is attached to a paper cone and placed near a permanent magnet. When alternating electrical current passes through the coil, it creates an alternating magnetic field. The coil is pushed and pulled by the permanent magnet, vibrating the cone and moving air to create sound.
2. **DC Motors**: A coil of wire (rotor coils) is placed inside a permanent magnet casing. When current is applied, magnetic forces push the rotor, causing it to spin.

### The "Motor Speaker" Trick
If you feed a high-frequency alternating signal (like a musical note) to a DC motor, the motor does not have enough time or energy to fully rotate. Instead, its shaft simply vibrates back and forth rapidly at that exact frequency. 

This vibration shakes the motor casing and any chassis it is mounted on, producing an audible acoustic sound wave! Kijani's `playTone` function alternates the H-bridge output on **Motor 1** to achieve this.

---

## Try it

Let's do a side-by-side comparison.

### Step 1: Listen to the Motor
1. Connect your DC motor to **Motor 1**.
2. Run this note URL: `http://10.10.10.10/playtone?freq=440&dur=1000`
3. Listen closely to the motor. Note the volume and the physical vibration you feel in your fingers.

### Step 2: Listen to a Speaker
1. Unplug the motor from **Motor 1**.
2. Connect a small 8-Ohm speaker to the **Motor 1** headers instead.
3. Run the same URL: `http://10.10.10.10/playtone?freq=440&dur=1000`
4. Notice how much clearer and louder the sound is!

---

## Why Drive Circuitry Matters

Different components have different power and drive requirements:

| Component | Drive Circuit | Description |
| :--- | :--- | :--- |
| **Piezo Buzzer** | Standard GPIO pin | Draws very low current (~20mA). Safe to connect directly to standard microchip pins. |
| **8-Ohm Speaker** | Audio Amplifier / H-Bridge | Has very low resistance. Connecting it directly to a microchip pin will draw too much current and burn the chip out. It needs a driver. |
| **DC Motor** | **H-Bridge Driver** (Kijani built-in) | Draws high current (up to 1A) and creates inductive voltage spikes. Must always be driven through a robust driver chip. |

Because Kijani drives Motor 1 through a heavy-duty H-bridge chip, you can safely connect **either** a power-hungry DC motor or a standard speaker directly to those output pins!

---

## What should happen
* The motor vibrates and makes a humming note.
* The speaker reproduces the same note with much higher clarity and volume.
* The on-board driver chip stays cool, keeping the ESP32 protected.

---

## Experiment
Mount your motor tightly to a plastic cup or a cardboard box. Play the note again. Does the volume increase? (Yes! The cardboard acts as a **soundboard**, magnifying the air vibration, just like an acoustic guitar body!).

---

## Challenge
Explain why a piezo buzzer would not work well if connected to Motor 1. 
*(Hint: Piezo buzzers are capacitive and do not like heavy current polarity reversals, whereas DC motors and speakers are inductive coils!)*

---

## Next step
Now that you know how sound is reproduced on different physical components, let's learn how to parse and play entire musical songs and custom ringtones using the RTTTL format!

👉 **[Lesson 9: RTTTL Music Files](./09-rtttl.md)**
