---
title: "Lesson 20: Design Your Own Project"
description: Complete your learning journey by designing, programming, and building your own custom Kijani project.
sidebar_position: 3
---

# Lesson 20: Design Your Own Project

Congratulations! You have reached the final milestone of the Kijani Progressive Course. You have learned how to host custom web interfaces, handle persistent files, make music, drive motors with advanced mixing algorithms, control servos, and read sensors. Now, it's time to build your own invention from scratch!

---

## The Challenge

Your task is to design, wire, program, and build a completely custom physical computing system using Kijani.

### Project Requirements
To successfully complete this course, your project must meet the following four criteria:
1. **Web Interface**: Must use Kijani's webserver to display a custom control page (`.html`) or telemetry view.
2. **At Least One Input**: Must read a physical sensor, switch, button, or bumper.
3. **At Least One Output**: Must control a DC motor, a servo motor, or generate sounds/music.
4. **Persistent Files**: Must store and load at least one file (HTML, CSS, JS, or RTTTL) inside Kijani's LittleFS memory.

---

## Inspiration and Ideas

If you aren't sure what to build, here are some student-favorite project ideas to get you started:

### 1. The Automated Garage/Toll Gate
* **Inputs**: A push button or light sensor representing an approaching toy car.
* **Outputs**: A servo motor operating a barrier arm, and a motor or buzzer playing a chime.
* **Web**: A dashboard displaying a count of cars parked, with manual override "OPEN" and "CLOSE" buttons.

### 2. A Web-Controlled Robotic Crane
* **Outputs**: Two DC motors to reel cable in/out and turn left/right, and a servo motor to open/close a physical claw.
* **Web**: An interactive crane console with direction controls and claw sliders.

### 3. Electronic Reflex Reaction Game
* **Inputs**: A tactile push-button switch.
* **Outputs**: An LED that turns on randomly, and a speaker that plays a victory/defeat RTTTL melody based on performance.
* **Web**: A scoreboard recording and displaying your reaction times in milliseconds.

### 4. Custom Remote-Controlled Antweight Battlebot
* **Inputs**: Digital bumper switches to stop motors upon ring exit.
* **Outputs**: Dual-motor differential drive with Arcade mixing, plus a servo-controlled spinning flipper or crushing jaw weapon.
* **Web**: A virtual dual-joystick gamepad served directly to your phone.

---

## Steps to Success

### Step 1: Sketch and Plan
Before wiring anything, draw your design on paper. Write down:
* What components you need.
* Which pins they will connect to (consult the **[Hardware Reference](../hardware-reference.md)**).
* What your webpage layout will look like.

### Step 2: Wire It Up (Power OFF!)
Assemble your physical chassis and slide Kijani's power switch **OFF** while connecting all components according to the **[Connection Examples](../connection-examples.md)**.

### Step 3: Write and Test Your Code
Create your HTML, CSS, and JS files. Test each small feature individually first:
* Can you control the output from a simple button?
* Does the sensor read correctly in the console?
* Once each piece works, combine them!

### Step 4: Share Your Creation
Connect your friends' or classmates' phones to your Kijani hotspot, open your project page, and let them try out your invention!

---

## Summary of Your Journey

You have successfully transitioned from an apprentice to a fully-fledged creator:
```text
  Lesson 1: Introduction ──> Got to know the hardware.
  Lesson 2-3: Webserver  ──> Controlled outputs over Wi-Fi.
  Lesson 4-6: Storage    ──> Handled persistent files, CSS, and JS.
  Lesson 7-9: Sound      ──> Generated tones, vibration, and full RTTTL songs.
  Lesson 10-12: Motors   ──> Drove dual motors using Tank & Arcade joystick mixing.
  Lesson 13-14: Servos   ──> Positioned steering arms and gates.
  Lesson 15-17: Inputs   ──> Read buttons, bumper switches, and external sensors.
  Lesson 18-20: Projects ──> Integrated everything into working systems!
```

**Good luck, and happy making! Your physical computing journey is only just beginning!**
