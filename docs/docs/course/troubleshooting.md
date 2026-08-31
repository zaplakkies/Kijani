---
title: Troubleshooting Guide
description: Solutions for common problems with connections, power, motors, and file storage.
sidebar_position: 6
---

# Troubleshooting Guide

Are things not behaving as expected? Don't worry! This guide covers the most common issues encountered when working with Kijani and how to fix them quickly.

---

## 1. Connection & Webserver Issues

### "I cannot see the MootBot_xxxxxx Wi-Fi network"
* **Check Power**: Ensure the power switch is flipped to **ON** and the status LED is blinking.
* **Low Battery**: If the battery voltage is too low, the Wi-Fi module will shut down first to save power. Plug in a USB cable to charge.
* **Scan Time**: Some devices take up to 30 seconds to refresh their Wi-Fi lists. Toggle your device's Wi-Fi off and back on.

### "I connected to the Wi-Fi, but 10.10.10.10 won't load"
* **No Internet Warning**: Your phone/laptop might have disconnected automatically because Kijani has no internet access. Check your device's connection status and select "Stay Connected anyway".
* **Browser Redirect**: Some modern browsers try to force an `https://` connection. Ensure you type exactly `http://10.10.10.10` in the address bar (HTTP, not HTTPS).
* **IP Conflicts**: If you are connected to multiple networks (e.g., mobile data + Wi-Fi), turn off mobile data temporarily.

---

## 2. Motor & Motion Issues

### "The motor does not move"
* **External Power**: Motors cannot run on low USB power. Ensure a charged LiPo battery is connected and the power switch is ON.
* **Check Wiring**: Ensure the motor pins are securely pushed onto the headers.
* **Inverted Code**: Check if the motor controls on the web page are set to 0.

### "The board resets as soon as the motor starts"
* **Classic Brownout**: The starting current of the motor is drawing too much power, causing the ESP32 voltage to drop below its reset threshold.
* **Solution**:
  1. Charge your LiPo battery.
  2. Avoid powering motors solely through a computer's USB port.
  3. Check for any physical binds or blocks preventing the wheels from spinning.

---

## 3. Servo Issues

### "The servo does not move, or hums loudly"
* **Wrong Polarity**: Ensure the brown or black wire of the servo is aligned with the square pin (GND).
* **High Load**: If the mechanism connected to the servo is jammed, the servo cannot rotate and will hum. Free the mechanical link.
* **Low Power**: Servos require stable power. Make sure your battery is charged or use a 5V USB wall adapter instead of a computer USB port.

---

## 4. Sound & RTTTL Issues

### "The speaker is too quiet, or there's only a buzzing sound"
* **Motor Vibration**: Remember, Kijani plays sound by vibrating Motor 1 (Left Motor). If no motor or speaker is connected to Motor 1, you won't hear anything!
* **Low Volume**: Sound level depends on the physical resonance of your robot's body. Mounting the motor to a plastic chassis helps amplify the sound.

---

## 5. File & Storage Issues

### "Uploaded file does not run / changes disappear after reboot"
* **Persistent Storage**: LittleFS files are stored persistently, but if you do not hit save or reload correctly, they won't execute.
* **File Naming**: Check your file extensions. Ensure your main landing page is exactly `index.html` or `control.html` so the webserver knows what to serve.
* **Storage Limit**: Kijani has about **1.4 MB** of flash storage for files. Check your file sizes (especially images) and compress them if needed.
