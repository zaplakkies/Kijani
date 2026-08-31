---
title: "Lesson 2: Webserver Basics"
description: Connect to Kijani's Wi-Fi network and explore its web interface.
sidebar_position: 2
---

# Lesson 2: Webserver Basics

In this lesson, you will connect your phone or computer to Kijani's local Wi-Fi, open the preloaded web control panel, and send direct HTTP commands to control the board!

---

## What you will learn
* How to connect to Kijani's local Wi-Fi access point.
* How to open Kijani's web interface in your browser.
* How to navigate page files and buttons.
* How Kijani's web API works and how to send simple control commands.

---

## What you need
* **1 × Kijani Controller Board** (powered ON)
* **1 × Phone, Tablet, or Computer with Wi-Fi**
* **1 × Small DC motor** or a speaker (optional, connected to Motor 1)

---

## Background

Kijani is a self-contained web server. When you flip its power switch on, the onboard ESP32 chip creates a local Wi-Fi hotspot. 

Any device connected to this hotspot can open a web page directly hosted by Kijani. When you click buttons or drag sliders on these pages, the web browser sends simple **HTTP GET requests** (API commands) back to Kijani. The firmware parses these requests and changes physical pins, turning motors or playing sounds.

---

## Connect it

1. Ensure your Kijani board is turned **ON**.
2. Open your device's Wi-Fi menu and connect to:
   ```text
   MootBot_xxxxxx
   ```
3. If a popup warning says "No Internet Access", choose **Stay Connected** or **Keep Wi-Fi Connection**.

---

## Try it

### 1. Open the Web Interface
Open your web browser (Chrome, Safari, or Firefox) and navigate to:

<Terminal host="10.10.10.10" lines={[
  { get: 'localhost:10.10.10.10' },
]} />

You should see Kijani's homepage load showing status info, battery levels, and files.

### 2. Drive an Output from the Browser
On the homepage, locate and click **controller.html** or **test.html**. 
* Slide the on-screen motor controls up and down.
* If you have a motor connected to Motor 1, you will see it spin!
* If you have a speaker connected to Motor 1, you will hear a tone that changes in pitch as you move the slider.

### 3. Send Commands Directly
You can bypass the web page entirely and talk directly to Kijani's API! In a new browser tab, type:

`http://10.10.10.10/processcontrol?M1=150`

Hit Enter. The motor connected to Motor 1 will start spinning! To stop it, type:

`http://10.10.10.10/processcontrol?M1=0`

---

## What should happen
* Navigating to `10.10.10.10` opens Kijani's dashboard.
* Moving sliders on the web interface controls the physical motor or speaker.
* Direct HTTP links change motor speeds instantly.

---

## Experiment
Try changing the parameters in the URL:
* Change `M1=150` to `M1=-150`. What happens? (The motor spins in reverse!)
* Try controlling Motor 2 (if connected) by typing `M2=200` in the URL.

---

## Challenge
Write a single HTTP request URL that turns Motor 1 forward at speed 200 AND Motor 2 backward at speed 150 at the same time. 
*(Hint: Use the `&` symbol to separate multiple parameters!)*

---

## Troubleshooting
* **Page won't load?** Verify that you are still connected to the `MootBot_xxxxxx` Wi-Fi and that your browser hasn't redirected you to `https://`.
* **Motor spins briefly then stops?** Your power source may be dropping voltage (brownout). Plug in a charged battery.

---

## Next step
Now that you can send commands, let's learn how to create your own project files and run them on Kijani!

👉 **[Lesson 3: Your First Project](./03-first-project.md)**
