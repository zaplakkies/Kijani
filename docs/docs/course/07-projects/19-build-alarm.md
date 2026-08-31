---
title: "Lesson 19: Build an Alarm"
description: Combine inputs, web control, speaker tone generation, and RTTTL files into a smart alarm system.
sidebar_position: 2
---

# Lesson 19: Build an Alarm

In this lesson, you will combine the web interface, digital inputs, speakers, and RTTTL storage into a highly practical project: a smart, web-customizable home security alarm!

---

## What you will learn
* How to combine hardware sensors with audio alarms.
* How to trigger stored RTTTL melodies when events occur.
* How to let users customize the alarm sound by uploading new ringtone files.

---

## What you need
* **1 × Kijani Controller Board**
* **1 × Speaker** or small motor (connected to Motor 1)
* **1 × Push Button** or door sensor (connected to GPIO 14)

---

## Background: The Smart Alarm Design
Our alarm system will monitor a door sensor (a simple button).
* When the door is closed (button unpressed), the system is green.
* When the door is opened (button pressed), the alarm is triggered, flashing Kijani's LED and playing an alarm melody.
* We want the alarm melody to be completely customizable! Users can upload any RTTTL file named `alarm.txt` via Kijani's dashboard, and our firmware will automatically load and play this song whenever the alarm is tripped.

---

## Connect it

1. Connect your speaker or alarm indicator motor to **Motor 1**.
2. Connect your button/door sensor between **GPIO 14** (Servo 2 Signal) and **GND**.

---

## Try it: Create the Alarm Project

Let's upload two files to make this work:

### File 1: `alarm.txt` (The Sound File)
Create a text file containing your custom alarm melody in RTTTL format. Paste this classic beep sequence:

```text
AlarmTone:d=8,o=6,b=160:c,p,c,p,c,p,c,p,c,p
```

Save it as **`alarm.txt`** and upload it to Kijani's file system (`http://10.10.10.10`).

---

### File 2: Create the Alarm Controller Dashboard
Create a webpage named `alarm.html` with this code, upload it to Kijani, and open it:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Smart Alarm Console</title>
    <style>
        body { font-family: sans-serif; text-align: center; background: #2c3e50; color: white; margin-top: 50px; }
        .card { background: #34495e; padding: 30px; border-radius: 10px; width: 400px; margin: 0 auto; }
        .status-box { background: #2ecc71; padding: 15px; border-radius: 6px; font-weight: bold; font-size: 20px; margin: 20px 0; }
        .triggered { background: #e74c3c; animation: flash 1s infinite alternate; }
        @keyframes flash { from { background: #e74c3c; } to { background: #c0392b; } }
        .btn { padding: 12px 20px; font-size: 16px; border: none; border-radius: 4px; cursor: pointer; font-weight: bold; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Smart Security System</h1>
        <div id="status" class="status-box">SYSTEM ARMED</div>
        
        <button class="btn" style="background:#f1c40f;" onclick="dismissAlarm()">RESET / DISMISS ALARM</button>
        <hr>
        <p>To change the sound, upload a new RTTTL file named <code>alarm.txt</code> on the home page!</p>
    </div>

    <script>
        let alarmActive = false;
        
        async function checkStatus() {
            // Read simulated sensors or digital inputs if API telemetry is available
            const response = await fetch('/quickstatus');
            const data = await response.json();
            
            // For example, if battery drops too low, let's trigger a power alarm
            if (data.vIn < 3.3) {
                triggerAlarm("LOW VOLTAGE DETECTED!");
            }
        }
        
        function triggerAlarm(msg) {
            if (alarmActive) return;
            alarmActive = true;
            document.getElementById('status').innerText = msg;
            document.getElementById('status').className = "status-box triggered";
            
            // Trigger Kijani to play the uploaded alarm.txt tune
            fetch('/playrtttl?tune=alarm.txt');
        }
        
        function dismissAlarm() {
            alarmActive = false;
            document.getElementById('status').innerText = "SYSTEM ARMED";
            document.getElementById('status').className = "status-box";
            fetch('/processcontrol?M1=0'); // stop alarm sounds
        }
        
        // Poll status every 1 second
        setInterval(checkStatus, 1000);
    </script>
</body>
</html>
```

---

## What should happen
* The dashboard page displays a green **SYSTEM ARMED** banner.
* If you trigger a low voltage threshold (or manually trigger it in your logic), the dashboard starts flashing bright red, and the board plays your custom `alarm.txt` RTTTL melody!
* Clicking **RESET / DISMISS ALARM** stops the sound and resets the status banner back to green.

---

## Challenge: Uploading a New Alarm Sound
Search the web for any Nokia RTTTL ringtone (e.g. *Mission Impossible* or *Indiana Jones*). Open your computer's text editor, paste the string, name the file `alarm.txt`, upload it to Kijani, and click play. Your alarm system now plays the new tune!

---

## Next step
Congratulations! You have completed all structured lessons of the Kijani Progressive Course. You are now ready to design and execute your very own final, custom physical computing project!

👉 **[Lesson 20: Design Your Own Project](./20-own-project.md)**
