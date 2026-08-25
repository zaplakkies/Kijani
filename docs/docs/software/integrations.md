---
id: integrations
title: Client Integrations & Controls
sidebar_position: 4
---

# Client Integrations & Controls

Because Kijani exposes an open HTTP API, you can control the robot using resources far beyond the standard browser joystick page. You can write custom automation scripts, connect physical gamepads, or integrate with STEM frameworks.

---

## 1. Python Scripts & Automation

You can write Python programs to automate robot movements, or wire them up to computer vision models (e.g., OpenCV ball-tracking) running on a laptop with a camera.

### Example: Remote Square Routine
This script uses the popular `requests` library to make the bot complete a simple path:

```python
import requests
import time

ROBOT_IP = "http://10.10.10.10"

def send_motors(m1, m2):
    try:
        url = f"{ROBOT_IP}/processcontrol?M1={m1}&M2={m2}"
        requests.get(url, timeout=0.15)
    except requests.RequestException:
        print("Communication error")

def stop_robot():
    send_motors(0, 0)

# Run a square routine
try:
    for i in range(4):
        print(f"Segment {i+1}: Driving forward")
        send_motors(200, 200)
        time.sleep(1.0)
        
        print(f"Segment {i+1}: Turning right")
        send_motors(200, -200)
        time.sleep(0.4)
        
    print("Routine completed successfully.")
finally:
    stop_robot()
```

---

## 2. Scratch / Block Coding Integration

For educational environments, Kijani can be programmed using Scratch or block programming blocks.
* Since Scratch 3.0 allows custom HTTP extensions, you can create a block that compiles to basic URL queries.
* **Block Definition Example:**
  - `[Drive Left Motor (speed) Right Motor (speed)]` maps to `/processcontrol?M1=[speed]&M2=[speed]`
  - `[Set Weapon Servo (angle)]` maps to `/processcontrol?S1=[angle]`
  - `[Read Battery Voltage]` parses the JSON output of `/quickstatus` and extracts the `"vIn"` property.
