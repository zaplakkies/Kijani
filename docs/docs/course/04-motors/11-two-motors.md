---
title: "Lesson 11: Connecting Two Motors"
description: Control two independent DC motors to drive a two-wheel robot.
sidebar_position: 2
---

# Lesson 11: Connecting Two Motors

In this lesson, you will connect two DC motors to Kijani, control each motor independently, and understand how differential steering allows a two-wheeled robot to turn and pivot.

---

## What you will learn
* The difference between Motor 1 (Left) and Motor 2 (Right) connections.
* How to send independent commands to two motors.
* How differential steering works (turning by changing relative speeds).
* Power considerations when driving two motors simultaneously.

---

## What you need
* **1 × Kijani Controller Board**
* **1 × 1S LiPo Battery** (charged, connected)
* **2 × DC Motors** (N20 gear motors recommended)

---

## Background

### Differential Steering
Most small mobile robots do not use steerable front wheels like a car. Instead, they use **differential steering** (similar to a tank or a wheelchair):
* **Drive Straight**: Spin both motors forward at the same speed.
* **Turn Left**: Spin the right motor forward and the left motor backward (or stop the left motor).
* **Turn Right**: Spin the left motor forward and the right motor backward (or stop the right motor).
* **Spin in Place (Pivot)**: Spin one motor forward and the other backward at the same speed.

---

## Connect it

1. Ensure Kijani is powered **OFF**.
2. Connect your Left motor to the **Motor 1** header.
3. Connect your Right motor to the **Motor 2** header.
4. Plug in the battery and slide the switch to **ON**.

---

## Try it

Let's try steering your dual-motor setup.

### Step 1: Drive Forward
In your browser address bar, enter:

`http://10.10.10.10/processcontrol?M1=180&M2=180`

Both motors spin forward.

### Step 2: Spin in Place (Pivot Left)
Now enter:

`http://10.10.10.10/processcontrol?M1=-180&M2=180`

Motor 1 (Left) reverses while Motor 2 (Right) goes forward. This spins the robot in place!

### Step 3: Create a Robot Controller Panel
Create a file named `robot.html` with this code, upload it to Kijani, and open it:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Robot Control</title>
    <style>
        body { font-family: sans-serif; text-align: center; background: #222; color: white; margin-top: 50px; }
        .grid { display: grid; grid-template-columns: 80px 80px 80px; gap: 15px; justify-content: center; margin: 30px auto; width: fit-content; }
        .btn { padding: 20px; font-size: 18px; border-radius: 8px; border: none; cursor: pointer; font-weight: bold; }
        .btn-dir { background: #3498db; color: white; }
        .btn-stop { background: #e74c3c; color: white; grid-column: span 3; }
    </style>
</head>
<body>
    <h1>Robot Steering Pad</h1>
    
    <div class="grid">
        <button class="btn"></button>
        <button class="btn btn-dir" onclick="move(180, 180)">▲</button>
        <button class="btn"></button>
        
        <button class="btn btn-dir" onclick="move(-180, 180)">◀</button>
        <button class="btn btn-stop" onclick="move(0, 0)">STOP</button>
        <button class="btn btn-dir" onclick="move(180, -180)">▶</button>
        
        <button class="btn"></button>
        <button class="btn btn-dir" onclick="move(-180, -180)">▼</button>
        <button class="btn"></button>
    </div>

    <script>
        function move(m1, m2) {
            fetch(`/processcontrol?M1=${m1}&M2=${m2}`);
        }
    </script>
</body>
</html>
```

---

## What should happen
* Clicking **▲** drives both wheels forward.
* Clicking **◀** spins the robot left.
* Clicking **▶** spins the robot right.
* Clicking **▼** drives both wheels backward.
* Clicking **STOP** halts both motors instantly.

---

## Experiment
Does one wheel spin slightly faster than the other, making your robot veer off to one side? This is common with small DC motors due to slight manufacturing variances. You can compensate for this in Kijani's built-in settings page (`settings.html`) by adjusting the max motor percentages for each side!

---

## Challenge
Modify the `move` speeds inside `robot.html` to create a "slow turn left" and "slow turn right" button instead of a sharp spin in place. 
*(Hint: Make one motor spin at speed 180 and the other at speed 80!)*

---

## Troubleshooting
* **Motors spin in the opposite direction than expected?** 
  * You can physically swap the motor wires around on the header pins.
  * Or, navigate to `http://10.10.10.10/settings.html` and check the **Swap Direction** checkbox for that motor, then save!

---

## Next step
Great job! You have built a steerable mobile robot platform. Next, we will explore advanced driving modes, like mixing throttle and steering into Arcade Drive using joysticks!

👉 **[Lesson 12: Different Ways of Driving](./12-driving-modes.md)**
