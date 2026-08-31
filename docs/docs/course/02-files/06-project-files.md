---
title: "Lesson 6: Project Files and Running"
description: Build a multi-file project combining HTML, CSS, and JavaScript.
sidebar_position: 3
---

# Lesson 6: Project Files and Running

In this lesson, we will build a complete web control application. Instead of keeping everything in one file, we will split our design into separate files: an HTML structure file, a CSS stylesheet for styling, and a JavaScript file for the control logic.

---

## What you will learn
* How to link multiple files together on Kijani.
* How to write a separate CSS file for professional layouts.
* How to write a separate JS file for clean communication logic.
* How to upload and test a multi-file project.

---

## What you need
* **1 × Kijani Controller Board** (powered ON)
* **1 × Computer** (connected to Kijani's Wi-Fi)
* **1 × DC Motor** or speaker (connected to Motor 1)

---

## Background

In professional web development, we never mix content, style, and code in a single file. Instead, we use:
1. **`.html`** for **Content** (buttons, sliders, headers).
2. **`.css`** for **Style** (colors, backgrounds, sizing, rounding).
3. **`.js`** for **Behavior** (what happens when buttons are clicked).

Because Kijani acts as a standard webserver, when you request an HTML file, the browser will read the HTML and automatically request any linked CSS and JS files from Kijani as well!

---

## Connect it

1. Ensure Kijani is powered **ON** and connected to your computer's Wi-Fi.
2. Connect a motor to **Motor 1**.

---

## Try it

Let's create and upload three separate files to make a unified control project.

### File 1: `control.html` (The Content)
Create this file and save it as `control.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Sleek Control</title>
    <!-- Link to our separate stylesheet -->
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="card">
        <h1>Sleek Controller</h1>
        <p>Motor 1 Speed Control</p>
        
        <div class="button-row">
            <button class="btn btn-forward" onclick="drive(200)">FORWARD</button>
            <button class="btn btn-reverse" onclick="drive(-200)">REVERSE</button>
        </div>
        
        <button class="btn btn-stop" onclick="drive(0)">STOP</button>
    </div>

    <!-- Link to our separate script -->
    <script src="logic.js"></script>
</body>
</html>
```

---

### File 2: `style.css` (The Style)
Create this file and save it as `style.css`:

```css
body {
    background-color: #1a252c;
    color: #eef;
    font-family: Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}

.card {
    background-color: #24343f;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    text-align: center;
}

.button-row {
    margin: 20px 0;
}

.btn {
    border: none;
    padding: 15px 25px;
    font-size: 16px;
    font-weight: bold;
    border-radius: 6px;
    margin: 10px;
    cursor: pointer;
    transition: background 0.2s;
}

.btn-forward { background-color: #2ecc71; color: white; }
.btn-forward:hover { background-color: #27ae60; }

.btn-reverse { background-color: #f1c40f; color: black; }
.btn-reverse:hover { background-color: #f39c12; }

.btn-stop { background-color: #e74c3c; color: white; width: 85%; }
.btn-stop:hover { background-color: #c0392b; }
```

---

### File 3: `logic.js` (The Code)
Create this file and save it as `logic.js`:

```javascript
function drive(speed) {
    console.log("Requesting speed:", speed);
    
    // Send standard HTTP GET request to Kijani
    fetch('/processcontrol?M1=' + speed)
        .then(response => {
            if (response.ok) {
                console.log("Command executed successfully.");
            } else {
                console.warn("Failed to contact Kijani.");
            }
        })
        .catch(err => console.error("Communication error:", err));
}
```

---

### Upload and Run
1. Go to `http://10.10.10.10` in your browser.
2. Upload all three files: `control.html`, `style.css`, and `logic.js`.
3. Open `http://10.10.10.10/control.html` in your browser.

---

## What should happen
* Your browser displays a beautiful, dark-themed dashboard card with styled green, yellow, and red buttons.
* Clicking **FORWARD** spins Motor 1 forward.
* Clicking **REVERSE** spins Motor 1 backward.
* Clicking **STOP** halts the motor instantly.

---

## Experiment
* Try editing the hover colors or button sizes in `style.css` on your computer.
* Re-upload `style.css` and refresh `control.html` in your browser to see your design changes instantly!

---

## Challenge
Add a second row of buttons to control **Motor 2** (Left/Right) in `control.html`, styles for those buttons in `style.css`, and update `logic.js` to handle driving Motor 2 using parameters.

---

## Troubleshooting
* **File doesn't look styled?** Ensure your `link` tag in `control.html` is exactly `<link rel="stylesheet" href="style.css">` and that the file is uploaded as `style.css`.
* **Buttons don't do anything?** Open the browser Developer Console (F12) to see if there is a 404 error fetching `logic.js`.

---

## Next step
Incredible! You are now a full-fledged Kijani web programmer. Next, we will learn how to make noise, play melodies, and understand how the Kijani board can sing!

👉 **[Lesson 7: Making Sound](../03-sound-and-music/sound.md)**
