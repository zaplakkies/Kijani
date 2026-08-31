---
title: "Lesson 14: Controlling a Servo from the Web"
description: Build a custom web control panel with sliders and button presets to control a servo.
sidebar_position: 2
---

# Lesson 14: Controlling a Servo from the Web

In this lesson, you will build a custom web dashboard featuring an angle slider and quick preset buttons. You will apply this to create a web-controlled gate, barrier, or steering mechanism!

---

## What you will learn
* How to read slider values to update servo positions.
* How to write button presets for quick servo angles.
* How to combine dual-motor driving with servo controls on a single webpage.

---

## What you need
* **1 × Kijani Controller Board**
* **1 × Servo** (connected to Servo 1)
* **2 × Motors** (connected to Motor 1 and Motor 2, optional)

---

## Background

Web inputs like `<input type="range">` are perfect for controlling servos. A range slider can be configured to start at `0` and go to `180`. Every time the slider changes, we fetch Kijani's `/processcontrol?S1=value` endpoint to move the servo in real-time.

Combining this with two-motor driving allows you to build advanced robots, like a forklift with a lifting arm, a sweeper with a moving brush, or a car with front-wheel steering!

---

## Try it

Let's build a dedicated servo dashboard.

### Create `servo.html`
Create `servo.html` on your computer, paste this code, upload it to Kijani, and open it:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Servo Dashboard</title>
    <style>
        body { font-family: sans-serif; text-align: center; background: #2c3e50; color: white; margin-top: 50px; }
        .card { background: #34495e; padding: 30px; border-radius: 10px; width: 350px; margin: 0 auto; box-shadow: 0 4px 10px rgba(0,0,0,0.3); }
        .slider { width: 100%; margin: 25px 0; }
        .btn { padding: 12px 20px; font-size: 16px; border: none; border-radius: 4px; margin: 10px 5px; cursor: pointer; font-weight: bold; }
        .btn-open { background: #2ecc71; color: white; }
        .btn-close { background: #e74c3c; color: white; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Barrier Gate</h1>
        <p>Control the servo angle:</p>
        
        <input type="range" min="0" max="180" value="90" class="slider" id="servoSlider" oninput="setServo(this.value)">
        <h2 id="angleText">Angle: 90°</h2>
        
        <hr>
        
        <h3>Presets</h3>
        <button class="btn btn-close" onclick="setPreset(0)">CLOSE (0°)</button>
        <button class="btn" onclick="setPreset(90)">MID (90°)</button>
        <button class="btn btn-open" onclick="setPreset(180)">OPEN (180°)</button>
    </div>

    <script>
        const slider = document.getElementById('servoSlider');
        const text = document.getElementById('angleText');
        
        function setServo(val) {
            text.innerText = "Angle: " + val + "°";
            fetch('/processcontrol?S1=' + val);
        }
        
        function setPreset(val) {
            slider.value = val;
            setServo(val);
        }
    </script>
</body>
</html>
```

---

## What should happen
* Dragging the slider rotates the servo smoothly back and forth in real-time.
* Clicking **CLOSE (0°)** sweeps the servo completely to one side.
* Clicking **OPEN (180°)** sweeps the servo all the way to the opposite side.

---

## Experiment: Build a Mechanical Gate
Tape a small cardboard strip or craft stick to the servo horn. Place it on your desk. Use your `servo.html` page to open and close your tiny toll-road barrier gate!

---

## Challenge
Add a second slider to the interface to control **Servo 2** (`S2` in the API), allowing you to control a two-jointed robotic arm!

---

## Next step
Incredible job! You've mastered outputs like motors, speakers, and servos. Now, we are going to learn how to read inputs! We'll start with digital inputs like buttons and switches.

👉 **[Lesson 15: Digital Inputs](../06-inputs/digital-inputs.md)**
