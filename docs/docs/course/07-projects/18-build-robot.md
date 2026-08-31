---
title: "Lesson 18: Build a Robot"
description: Combine web control, dual motors, and mechanical bumper safety into a complete robot project.
sidebar_position: 1
---

# Lesson 18: Build a Robot

In this lesson, you will combine multiple concepts you have learned—motors, driving algorithms, web interfaces, and bumper switches—into a single, highly capable robot. 

---

## What you will learn
* How to integrate manual web controls with autonomous physical sensors.
* How to implement a safety override in code.
* Building a complete, interactive, web-controlled battlebot with active safety brakes.

---

## What you need
* **1 × Kijani Controller Board** (battery connected)
* **1 × Wheeled Robot Chassis** (with two DC motors connected)
* **1 × Bumper Switch** (mounted to the front of the robot)

---

## Background: The Safety Override Concept
In this project, we want a robot that is driven manually by a user on a phone using a virtual joystick, but with **automatic active braking**. 

If the robot is driving forward and runs into a wall, the physical bumper switch will trigger. The robot should immediately override the user's manual speed commands and stop or reverse, preventing the motors from stalling and burning out.

```text
               [ Joystick Web Command ]
                          │
                          ▼
            === Is Bumper Pressed? ===
                 /              \
            No  /                \ Yes (OVERRIDE!)
               ▼                  ▼
       [ Drive at User Speed ]   [ Force Stop / Brake ]
```

---

## Connect it

1. Connect the Left motor to **Motor 1** and the Right motor to **Motor 2**.
2. Connect your front bumper switch between **GPIO 14** (Servo 2 Signal) and **GND**.

---

## Try it: Write the Integration Firmware

To allow Kijani's web server to interact with the bumper, we modify Kijani's firmware or write a unified script:

```cpp
#define BUMPER_PIN 14
#define MotorA1 32
#define MotorA2 33
#define MotorB1 25
#define MotorB2 26

volatile int userSpeedM1 = 0;
volatile int userSpeedM2 = 0;

void handleWebCommand(int speed1, int speed2) {
  userSpeedM1 = speed1;
  userSpeedM2 = speed2;
}

void setup() {
  pinMode(BUMPER_PIN, INPUT_PULLUP);
  
  pinMode(MotorA1, OUTPUT);
  pinMode(MotorA2, OUTPUT);
  pinMode(MotorB1, OUTPUT);
  pinMode(MotorB2, OUTPUT);
}

void driveMotors(int s1, int s2) {
  // Drive Motor A
  if (s1 >= 0) {
    digitalWrite(MotorA2, LOW);
    analogWrite(MotorA1, s1);
  } else {
    digitalWrite(MotorA2, HIGH);
    analogWrite(MotorA1, 255 + s1);
  }
  
  // Drive Motor B
  if (s2 >= 0) {
    digitalWrite(MotorB2, LOW);
    analogWrite(MotorB1, s2);
  } else {
    digitalWrite(MotorB2, HIGH);
    analogWrite(MotorB1, 255 + s2);
  }
}

void loop() {
  // Read physical bumper
  int hit = digitalRead(BUMPER_PIN);
  
  if (hit == LOW) {
    // Override: Force immediate stop if user tries to drive forward
    int safeM1 = min(0, userSpeedM1);
    int safeM2 = min(0, userSpeedM2);
    driveMotors(safeM1, safeM2);
  } else {
    // Normal operation: follow joystick commands
    driveMotors(userSpeedM1, userSpeedM2);
  }
  delay(20);
}
```

---

## What should happen
* You can connect to Kijani and drive your robot around the room normally using your custom `joystick.html` page.
* While driving forward, if the robot collides with a table leg and presses the bumper switch, the robot halts immediately, ignoring any further forward joystick commands.
* If you drag the joystick backward, the safety override permits reversing, allowing you to back away from the wall safely!

---

## Challenge: Autonomous Back-up and Release
Modify the override section of the loop so that when the bumper is hit, the robot doesn't just stop—it automatically backs up for half a second and spins 45 degrees, then hands manual control back to the joystick!

---

## Next step
Wow, what an incredible robot you have built! Next, we will switch gears and build a smart **Connected Alarm System** that plays music when security thresholds are breached!

👉 **[Lesson 19: Build an Alarm](./19-build-alarm.md)**
