---
title: "Lesson 10: Connecting One Motor"
description: Control a single DC motor's speed and direction using Kijani.
sidebar_position: 1
---

# Lesson 10: Connecting One Motor

In this lesson, you will connect your first DC motor to Kijani, understand how microcontrollers regulate speed and direction, and build a web-controlled motor slider!

---

## What you will learn
* How DC motors work.
* How H-bridges control motor speed and direction.
* The difference between positive (+) and negative (-) motor speeds.
* Why external battery power is critical for driving motors.

---

## What you need
* **1 × Kijani Controller Board**
* **1 × 1S LiPo Battery** (charged, connected)
* **1 × DC Motor** (N20 gear motor recommended)

---

## Background

### How Motor Control Works
DC motors spin when electric current passes through them. If you swap the positive and negative wires, the motor spins in the opposite direction. 

A microcontroller cannot directly connect to a motor because a motor draws too much current. Kijani contains an **H-Bridge** motor driver chip. The H-bridge acts like a smart set of high-speed electronic switches that can redirect current flowing to the motor, allowing us to:
1. **Change Direction**: By reversing current flow.
2. **Control Speed**: By pulsing the power ON and OFF extremely fast. This is called **PWM (Pulse Width Modulation)**. If the pulse is ON 50% of the time, the motor spins at half speed. If it is ON 100% of the time, it spins at full speed.

### Kijani Speed Ranges
In Kijani's API, motor speeds range from **`-255` to `255`**:
* **`255`**: Full Speed Forward.
* **`0`**: Stopped (Off).
* **`-255`**: Full Speed Reverse.

---

## Connect it

1. Ensure Kijani is powered **OFF**.
2. Connect your DC motor to the **Motor 1** header pins.
3. Connect your 1S LiPo battery to the battery connector.
4. Flip the power switch to **ON**.

---

## Try it

Let's use a web slider to control the motor.

### Step 1: Control from URL
Open your browser and enter:

`http://10.10.10.10/processcontrol?M1=150`

The motor spins forward! To spin in reverse:

`http://10.10.10.10/processcontrol?M1=-150`

Stop the motor:

`http://10.10.10.10/processcontrol?M1=0`

### Step 2: Build a Custom Slider Page
Create a file named `motor.html` with this code, upload it, and open it:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Motor Slider</title>
    <style>
        body { font-family: sans-serif; text-align: center; margin-top: 50px; background: #eef; }
        .slider { width: 300px; margin: 30px; }
        h2 { font-size: 32px; color: #333; }
    </style>
</head>
<body>
    <h1>Motor Speed Control</h1>
    <input type="range" min="-255" max="255" value="0" class="slider" id="speedSlider" oninput="updateSpeed(this.value)">
    <h2 id="speedVal">Speed: 0</h2>

    <script>
        function updateSpeed(val) {
            document.getElementById("speedVal").innerText = "Speed: " + val;
            // Send request to Kijani
            fetch('/processcontrol?M1=' + val);
        }
    </script>
</body>
</html>
```

---

## What should happen
* Moving the slider to the right spins the motor forward (increasing speed up to 255).
* Moving the slider to the left spins the motor backward.
* Leaving the slider in the center (0) stops the motor completely.

---

## Experiment
Move the slider very slowly from 0 toward 50. Notice that the motor doesn't start spinning immediately—it might just buzz! This is normal. Small DC motors require a minimum amount of voltage (known as **starting friction** or **stiction**) before they can physically overcome internal gear resistance and spin.

---

## Challenge
Add a "Quick Stop" button to `motor.html` that instantly resets the slider to `0` and halts the motor immediately when clicked.

---

## Troubleshooting
* **Motor doesn't move but buzzes?** Increase the speed slider value or ensure your battery is fully charged.
* **Board shuts off or blinks red?** You are trying to run the motor off low USB power. Plug in a charged LiPo battery.

---

## Next step
Now that you can drive a single motor, let's connect a second motor and build a simple two-wheeled steering chassis!

👉 **[Lesson 11: Connecting Two Motors](./11-two-motors.md)**
