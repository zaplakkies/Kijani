---
title: "Lesson 7: Making Sound and Vibration"
description: Understand sound generation, frequencies, PWM, and how to program different buzzer tones.
sidebar_position: 1
---

# Lesson 7: Making Sound and Vibration

In this lesson, you will learn the science behind electronic sound, explore Pulse Width Modulation (PWM), and create a custom sound effect page to play different buzzer tones!

---

## What you will learn
* How microcontrollers make sound.
* Basics of Frequency and Pitch.
* Basics of PWM (Pulse Width Modulation) and Volume.
* Why motors and speakers may need different drive circuitry.
* How to play custom tones using Kijani's sound API.

---

## What you need
* **1 × Kijani Controller Board** (powered ON)
* **1 × Small Speaker** or piezo buzzer connected to Motor 1 output (or simply use a connected Motor 1!).

---

## Background

### How Electronic Sound Works
Sound is a pressure wave that travels through the air. To create an electronic sound, we must physically vibrate something—like a speaker cone, a piezo disc, or even a motor's internal coils!

We vibrate them by turning a pin **ON** and **OFF** very rapidly. The speed at which we toggle the pin is called the **Frequency**, measured in **Hertz (Hz)**.
* **Low Frequency** (e.g., 100 Hz) = Low, bassy sound (vibrates 100 times per second).
* **High Frequency** (e.g., 2000 Hz) = High-pitched squeak (vibrates 2,000 times per second).

### PWM and Volume
To control volume or power, we adjust the **Duty Cycle**—the percentage of time the signal is HIGH versus LOW. A 50% duty cycle (equal parts ON and OFF) produces the clearest and loudest square-wave sound.

---

## Connect it

1. Make sure Kijani is powered ON and connected to Wi-Fi.
2. Connect a small speaker or a standard DC motor to **Motor 1** (Left Motor). Yes, a motor works as a speaker too!

---

## Try it

Kijani has a special API endpoint designed to play single tones at specified frequencies and durations.

### Step 1: Play a Low Tone
In your browser address bar, enter this URL:

`http://10.10.10.10/playtone?freq=262&dur=500`

Hit Enter. You will hear a middle C note (262 Hz) play for half a second (500 milliseconds)!

### Step 2: Play a High Tone
Now try:

`http://10.10.10.10/playtone?freq=1000&dur=300`

This plays a higher-pitched 1 kHz tone for 300 milliseconds.

### Step 3: Create a Siren Effect
Create a file named `sound.html` with this code, upload it, and open it:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Sound Board</title>
    <style>
        body { font-family: sans-serif; text-align: center; margin-top: 50px; background: #222; color: white; }
        button { font-size: 20px; padding: 15px 25px; margin: 10px; border-radius: 6px; cursor: pointer; }
    </style>
</head>
<body>
    <h1>Kijani Sound Board</h1>
    <button onclick="play(262, 200)">Low Note (C)</button>
    <button onclick="play(440, 200)">Concert A (440Hz)</button>
    <button onclick="play(880, 200)">High Note (A5)</button>
    <button onclick="playSiren()">🚨 Siren Effect</button>

    <script>
        function play(freq, dur) {
            fetch(`/playtone?freq=${freq}&dur=${dur}`);
        }
        
        async function playSiren() {
            for (let f = 400; f < 1000; f += 50) {
                play(f, 50);
                await new Promise(r => setTimeout(r, 60));
            }
            for (let f = 1000; f > 400; f -= 50) {
                play(f, 50);
                await new Promise(r => setTimeout(r, 60));
            }
        }
    </script>
</body>
</html>
```

---

## What should happen
* Clicking the single note buttons plays brief, distinct musical pitches.
* Clicking the **Siren Effect** creates a smooth, rising and falling alarm sound.
* Motor 1 vibrates physically at each note's specific frequency.

---

## Experiment
Open `sound.html` and change the frequencies. Look up the frequencies of standard piano notes (e.g., C4 is 261.63 Hz, E4 is 329.63 Hz, G4 is 392.00 Hz) and try playing a simple triad chord sequentially.

---

## Challenge
Create a "Laser Gun" sound effect. It should start at a high frequency (e.g., 1500 Hz) and sweep down rapidly to a low frequency (e.g., 200 Hz).

---

## Troubleshooting
* **No Sound?** Sound is played specifically through **Motor 1 (Left Motor)** pins. Ensure your speaker or motor is plugged into Motor 1, not Motor 2.
* **Sound is clicking or stuttering?** Sending too many fetch requests per second can overload the web server queue. Ensure your timeouts in the loop allow each tone to finish playing.

---

## Next step
Now that you know how to generate sound, let's explore why both speaker cones and motors work as speakers, and the physical limits of their circuitry.

👉 **[Lesson 8: Speakers and Motors](./08-speakers-motors.md)**
