---
title: Quick Start Guide
description: Get up and running with your Kijani board in under five minutes.
sidebar_position: 2
---

# Quick Start Guide

Just took your Kijani controller out of the box? Follow these five quick steps to get connected and test your board immediately.

---

## Step 1: Connect Power
* If you have a **1S LiPo battery**, plug it into the battery port (paying attention to polarity). Slide the power switch to **ON**.
* Alternatively, plug a **USB-C cable** from your computer or a 5V phone charger into the USB port.
* You should hear a short startup chime and see a status LED blink.

---

## Step 2: Join the Kijani Wi-Fi Network
Open the Wi-Fi settings on your phone, tablet, or laptop and search for new networks.

* Select the network named:
  ```text
  MootBot_xxxxxx
  ```
  *(where `xxxxxx` is a unique code for your specific board)*.
* If your board has a **QR code sticker**, scan it with your phone to connect automatically.
* If prompted that the network has "No Internet Access", click **Stay Connected** or **Keep Connection**.

---

## Step 3: Open the Web Control Panel
Open your web browser (Safari, Chrome, Firefox, or Edge) and navigate to:

<Terminal host="10.10.10.10" lines={[
  { get: 'localhost:10.10.10.10' },
]} />

You should see the friendly Kijani dashboard load instantly.

---

## Step 4: Run a Quick Test
* Click on **controller.html** on the home page.
* Slide the on-screen motor controls or click a button to test.
* If you have a speaker or motor connected, you should see or hear it respond!

---

## Step 5: What Next?
Now that you know your board is working and you can connect to it, you're ready to start programming!

👉 Head over to **[Lesson 1: Introduction to Kijani](./01-getting-started/intro.md)** to understand how Kijani works.
