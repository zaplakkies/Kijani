---
title: "Lesson 12: Different Ways of Driving"
description: Master Tank Drive vs. Arcade Drive and implement motor mixing with a virtual joystick.
sidebar_position: 3
---

# Lesson 12: Different Ways of Driving

In this lesson, you will master the physics of robot steering by implementing **Arcade Drive**. You will learn how to write "motor mixing" code that translates 2D joystick coordinates (X and Y) into smooth, intuitive robot controls.

---

## What you will learn
* The difference between Tank Drive and Arcade Drive.
* How to implement Arcade Drive using motor mixing equations.
* How to translate raw joystick coordinates into motor speeds.

---

## Background

### Tank Drive vs. Arcade Drive
* **Tank Drive**: Uses two separate sliders. Left control maps directly to the Left motor; Right control maps to the Right motor.
* **Arcade Drive**: Uses one 2D joystick. Up/down controls **Throttle (Y)**, and left/right controls **Steering (X)**.

### The Motor Mixing Math
To translate X (steering) and Y (throttle) values into Left ($M1$) and Right ($M2$) motor speeds:

$$M1 = Y + X$$
$$M2 = Y - X$$

* **Going straight**: $Y=150, X=0 \implies M1=150, M2=150$ (Both forward).
* **Spinning right**: $Y=0, X=100 \implies M1=100, M2=-100$ (Left forward, Right reverse).

---

## Try it: Build an Arcade Joystick

Let's create a virtual joystick interface.

### Create `joystick.html`
Create `joystick.html` on your computer, paste this code, upload it to Kijani, and open it:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Arcade Joystick</title>
    <style>
        body { font-family: sans-serif; text-align: center; background: #111; color: white; user-select: none; }
        #container { width: 200px; height: 200px; background: #333; border-radius: 50%; margin: 30px auto; position: relative; touch-action: none; }
        #knob { width: 60px; height: 60px; background: #e74c3c; border-radius: 50%; position: absolute; left: 70px; top: 70px; cursor: pointer; }
    </style>
</head>
<body>
    <h1>Arcade Drive</h1>
    <div id="container">
        <div id="knob"></div>
    </div>
    <h3 id="stats">X: 0 | Y: 0 => M1: 0 | M2: 0</h3>
    <script>
        const container = document.getElementById('container');
        const knob = document.getElementById('knob');
        const stats = document.getElementById('stats');
        const maxDist = 70;
        let active = false, startX, startY;
        
        knob.addEventListener('mousedown', start);
        knob.addEventListener('touchstart', start);
        window.addEventListener('mousemove', drag);
        window.addEventListener('touchmove', drag);
        window.addEventListener('mouseup', stop);
        window.addEventListener('touchend', stop);
        
        function start(e) {
            active = true;
            const clientX = e.clientX || e.touches[0].clientX;
            const clientY = e.clientY || e.touches[0].clientY;
            startX = clientX - knob.offsetLeft;
            startY = clientY - knob.offsetTop;
        }
        
        function drag(e) {
            if (!active) return;
            e.preventDefault();
            const clientX = e.clientX || e.touches[0].clientX;
            const clientY = e.clientY || e.touches[0].clientY;
            let dx = clientX - startX - 70;
            let dy = clientY - startY - 70;
            const dist = Math.sqrt(dx*dx + dy*dy);
            if (dist > maxDist) {
                dx = (dx / dist) * maxDist;
                dy = (dy / dist) * maxDist;
            }
            knob.style.left = (70 + dx) + 'px';
            knob.style.top = (70 + dy) + 'px';
            
            const x = Math.round((dx / maxDist) * 255);
            const y = Math.round(-(dy / maxDist) * 255);
            let m1 = Math.max(-255, Math.min(255, y + x));
            let m2 = Math.max(-255, Math.min(255, y - x));
            
            stats.innerText = `X: ${x} | Y: ${y} => M1: ${m1} | M2: ${m2}`;
            sendCmd(m1, m2);
        }
        
        function stop() {
            active = false;
            knob.style.left = '70px'; knob.style.top = '70px';
            stats.innerText = `X: 0 | Y: 0 => M1: 0 | M2: 0`;
            sendCmd(0, 0);
        }
        
        let lastSent = 0;
        function sendCmd(m1, m2) {
            const now = Date.now();
            if (now - lastSent < 60 && m1 !== 0 && m2 !== 0) return;
            lastSent = now;
            fetch(`/processcontrol?M1=${m1}&M2=${m2}`);
        }
    </script>
</body>
</html>
```

---

## What should happen
* Dragging the joystick forward moves both motors forward.
* Dragging it right pivots your robot right.
* Releasing the knob snaps it back to center and stops the robot.

---

## Challenge
Modify `joystick.html` so that the maximum speed is restricted to `150` instead of `255`, creating a "Precision Safe Mode" button.

---

## Troubleshooting
* **Joystick lag?** The code contains a rate limiter (`lastSent` check). If it feels unresponsive, adjust the limit (from 60ms to 80ms) or make sure you are close to the Wi-Fi.

---

## Next step
Wow! Your robot is fully drivable! Next, we will learn about **Servos** and how to add moving arms, steering mechanisms, or camera pans.

👉 **[Lesson 13: Servo Connections](../05-servos/servo-connection.md)**
