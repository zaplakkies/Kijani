---
title: "Lesson 16: Buttons and Bumpers"
description: Connect collision bumpers and program autonomous escape maneuvers.
sidebar_position: 2
---

# Lesson 16: Buttons and Bumpers

In this lesson, you will connect mechanical bumper switches to your robot and program an autonomous collision-avoidance routine. Your robot will drive forward until it hits a wall, then automatically stop, back up, turn, and continue driving!

---

## What you will learn
* How to wire bumper switches to a mobile robot chassis.
* How to detect physical collisions using digital inputs.
* How to write autonomous "rebound and steer" logic in C++/Arduino.
* Designing state-based code loops for autonomous behaviors.

---

## What you need
* **1 × Kijani Controller Board** (with battery)
* **2 × DC Motors** (on a wheeled robot chassis)
* **1 × Bumper Switch** (micro-switch with a lever arm)

---

## Background

### Collision Detection in Robotics
A **bumper switch** is a simple mechanical switch mounted to the front bumper of a robot. When the robot runs into an obstacle, the lever is physically pressed, closing the switch.

By reading this switch inside the main execution loop, our code can instantly override any manual or autonomous drive commands and execute a safety maneuver.

```text
  Collision Loop State Machine:
  
  [ State: DRIVE FWD ] ───────> (Bumper Pressed?)
           ▲                           │ Yes
           │                           ▼
  [ State: TURN ] <────── [ State: REVERSE / BACK UP ]
```

---

## Connect it

1. Mount a micro-switch to the front-left or center bumper of your robot.
2. Connect the switch's **COM (Common)** pin to Kijani's **GND** pin.
3. Connect the switch's **NO (Normally Open)** pin to **GPIO 14** (Servo 2 Signal).

```text
    Kijani Pin 14 (SIG)         Bumper Switch
    +-------------------+      +-------------------+
    | Pin 14    [ O ] <======> | NO (Normally Open)|
    | GND       [ O ] <======> | COM (Common)      |
    +-------------------+      +-------------------+
```

---

## Try it

Upload or run this code on Kijani to make it autonomously react to walls:

```cpp
#define BUMPER_PIN 14
#define MotorA1 32
#define MotorA2 33
#define MotorB1 25
#define MotorB2 26

void setup() {
  pinMode(BUMPER_PIN, INPUT_PULLUP);
  
  pinMode(MotorA1, OUTPUT);
  pinMode(MotorA2, OUTPUT);
  pinMode(MotorB1, OUTPUT);
  pinMode(MotorB2, OUTPUT);
}

void driveForward() {
  // Drive both motors forward
  digitalWrite(MotorA2, LOW);
  analogWrite(MotorA1, 150);
  digitalWrite(MotorB2, LOW);
  analogWrite(MotorB1, 150);
}

void driveReverse() {
  // Drive both motors backward
  digitalWrite(MotorA2, HIGH);
  analogWrite(MotorA1, 255 - 150); // PWM inverse
  digitalWrite(MotorB2, HIGH);
  analogWrite(MotorB1, 255 - 150);
}

void turnRight() {
  // Spin left wheel forward, right wheel backward
  digitalWrite(MotorA2, LOW);
  analogWrite(MotorA1, 150);
  digitalWrite(MotorB2, HIGH);
  analogWrite(MotorB1, 255 - 150);
}

void stopRobot() {
  digitalWrite(MotorA1, LOW);
  digitalWrite(MotorA2, LOW);
  digitalWrite(MotorB1, LOW);
  digitalWrite(MotorB2, LOW);
}

void loop() {
  // Read the bumper
  int hit = digitalRead(BUMPER_PIN);
  
  if (hit == LOW) {
    // Collision detected!
    stopRobot();
    delay(200); // Brief pause
    
    // Step 1: Back up for 1 second
    driveReverse();
    delay(1000);
    
    // Step 2: Spin turn right for half a second
    turnRight();
    delay(500);
    
    // Step 3: Stop before checking again
    stopRobot();
    delay(200);
  } else {
    // Path is clear, drive forward
    driveForward();
  }
  delay(20); // Loop pacing
}
```

---

## What should happen
* The robot immediately starts driving forward.
* When you press the front bumper switch (or when the robot hits a wall), the robot stops, reverses for 1 second, spins to the right, and then continues driving forward in a new direction.

---

## Experiment
Try changing the turn duration (`delay(500)` in `turnRight()`) to `1000`. Does the robot execute a wider pivot? (Yes, increasing the turn delay increases the angle of escape).

---

## Challenge
Add a second bumper switch on **GPIO 27** (Servo 1 Signal) for the right side. Modify your loop logic:
* If the **Left Bumper** is hit, reverse and turn **Right**.
* If the **Right Bumper** is hit, reverse and turn **Left**.

---

## Troubleshooting
* **Robot immediately goes into reverse and turn loop?** 
  * Ensure your switch is wired to the **Normally Open (NO)** terminal, not the *Normally Closed (NC)* terminal.
  * Check that your bumper wire is connected securely to the correct pin.

---

## Next step
Fantastic work building an autonomous robot behavior! Next, we will explore Kijani's expansion capabilities and learn how to connect other analog and digital sensors like light and ultrasonic distance sensors.

👉 **[Lesson 17: Extra Connections and Sensors](./17-extra-connections.md)**
