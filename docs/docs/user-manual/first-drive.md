---
title: First Drive
description: Join the robot's WiFi access point and drive it from your browser.
sidebar_position: 3
---

# First Drive

## Connecting to the robot

<Refdes id="AP">Step 1 — Power on</Refdes>

Flip the switch to **ON**. You should hear a startup tune played through the motors — that confirms the firmware is running.

<Refdes id="WiFi">Step 2 — Join the network</Refdes>

On your phone, tablet or laptop, connect to the WiFi network named:

```
MootBot_xxxxxx
```

where `xxxxxx` is a unique identifier for your board.

Your device may warn that the network has no internet access. Choose **Stay Connected** or **Use This Network Anyway** — the robot is a local access point, not an internet gateway.

<Refdes id="HTTP">Step 3 — Open the browser</Refdes>

In your browser, navigate to:

<Terminal host="10.10.10.10" lines={[
  { get: 'localhost:10.10.10.10' },
]} />

<br />

You should see the robot's home page:

![Kijani home page served from the ESP32](./img/main1.jpeg)

## Driving the robot

From the home page, open **controller.html**. The default control interface lets you drive both motors and move the servo.

![Default control interface](./img/control1.jpeg)

That's it — you're driving. Steer with the on-screen controls, check that both motors respond, and confirm the servo swings.

Want to build your own controls? See [Customisation](./customisation.md).
