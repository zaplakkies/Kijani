---
title: "Lesson 3: Your First Project"
description: Build, upload, and test your very first web-controlled project.
sidebar_position: 3
---

# Lesson 3: Your First Project

In this lesson, we will build a custom "Hello Kijani" project. You will create a simple web page with buttons on your computer, upload it to Kijani, and use it to turn a motor on and off!

---

## What you will learn
* How Kijani project files work.
* How to write basic HTML to send commands to Kijani.
* How to upload files to Kijani's flash memory.
* How to run and test your custom controls.

---

## What you need
* **1 × Kijani Controller Board** (powered ON)
* **1 × Computer or Tablet** with a text editor (Notepad, TextEdit, VS Code)
* **1 × Small DC motor** (connected to Motor 1)

---

## Background

To make a custom remote control interface, all you need is a simple text file with the extension `.html`. Inside, you write standard HTML to display buttons, and some lightweight JavaScript to trigger an API command when a button is clicked.

Once uploaded to Kijani, the board serves this file over Wi-Fi, turning any connected device into a custom remote controller!

---

## Connect it

1. Make sure your Kijani board is powered ON.
2. Connect a DC motor to the **Motor 1** headers.
3. Connect your computer to Kijani's Wi-Fi network.

---

## Try it

### Step 1: Create the HTML File
On your computer, open a text editor (like Notepad or VS Code) and create a new file. Paste the following HTML code into it:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Hello Kijani</title>
    <style>
        body { font-family: sans-serif; text-align: center; margin-top: 50px; background: #eef; }
        button { font-size: 24px; padding: 15px 30px; margin: 10px; border-radius: 8px; cursor: pointer; }
        .on { background: #4CAF50; color: white; }
        .off { background: #f44336; color: white; }
    </style>
</head>
<body>
    <h1>Hello Kijani!</h1>
    <p>Control your motor from this page:</p>
    
    <button class="on" onclick="sendCmd(150)">Motor ON</button>
    <button class="off" onclick="sendCmd(0)">Motor OFF</button>

    <script>
        function sendCmd(speed) {
            // Send request to Kijani API
            fetch('/processcontrol?M1=' + speed)
                .then(response => console.log("Sent speed: " + speed))
                .catch(err => console.error("Error sending: " + err));
        }
    </script>
</body>
</html>
```

Save the file on your computer as exactly **`hello.html`**.

### Step 2: Upload to Kijani
1. Open your web browser and go to `http://10.10.10.10`.
2. Locate the **File Upload** utility on Kijani's dashboard.
3. Click "Choose File", select your `hello.html` file, and click **Upload**.
4. Once completed, you should see `hello.html` listed in Kijani's stored files list.

### Step 3: Run the Project
In your browser address bar, navigate to:

`http://10.10.10.10/hello.html`

Your custom page will load! Click **Motor ON** and **Motor OFF**. 

---

## What should happen
* Clicking **Motor ON** turns the motor on at a steady pace.
* Clicking **Motor OFF** stops the motor.
* Your custom HTML page is served directly from Kijani's flash memory.

---

## Experiment
* Open your `hello.html` file in your editor again.
* Try changing the speed in `sendCmd(150)` to `sendCmd(-150)` to run the motor backward when the button is pressed.
* Save, upload, and test!

---

## Challenge
Add a third button to your HTML file labeled "Half Speed" that turns Motor 1 on at speed `80`.

---

## Troubleshooting
* **Error "File not found"?** Make sure the file you uploaded is named exactly `hello.html` (all lowercase, no spaces).
* **Button does nothing?** Check the console in your browser (F12) to see if there are any JavaScript typos or connection errors.

---

## Next step
Excellent job! You've built and run your first custom project. Now, let's explore how Kijani stores files persistently and how to organize them.

👉 **[Lesson 4: Uploading Files](../02-files/uploading.md)**
