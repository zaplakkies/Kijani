---
title: "Lesson 15: Digital Inputs"
description: Understand digital logic, HIGH and LOW states, and internal pull-up/pull-down resistors.
sidebar_position: 1
---

# Lesson 15: Digital Inputs

In this lesson, you will step beyond outputs and learn how microcontrollers read information from the physical world. We will explore digital inputs, the concept of HIGH and LOW states, and how internal pull-up resistors work.

---

## What you will learn
* What digital inputs are and how they measure states.
* The difference between `HIGH` (3.3V) and `LOW` (0V/GND).
* Why a "floating" pin is bad and how pull-up/pull-down resistors solve it.
* How to write basic Arduino/C++ firmware code to read a physical button.

---

## What you need
* **1 × Kijani Controller Board**
* **1 × Tactile push button** or a simple slide switch
* **Jumper wires**

---

## Background

### What is a Digital Input?
While outputs (like motors and speakers) *do* things, inputs *sense* things. A **digital input** is binary—it can only ever see two states:
1. **`HIGH`**: Voltage is present (3.3 Volts on the ESP32). Represents `1`, `True`, or `ON`.
2. **`LOW`**: Voltage is absent (0 Volts / Ground). Represents `0`, `False`, or `OFF`.

### The "Floating" Pin Problem
If you connect an ESP32 pin to a button, and the other side of the button to 3.3V:
* When the button is **pressed**, the pin is connected to 3.3V and reads **HIGH**.
* When the button is **released**, the pin is connected to *nothing*.

A pin connected to nothing is **floating**. It acts like a tiny antenna, picking up static electricity from the air. The microcontroller will rapidly fluctuate between HIGH and LOW, causing erratic behavior.

### The Solution: Pull-up Resistors
To prevent floating, we use a resistor to "pull" the pin's voltage to a known state when the button is open.
* **Internal Pull-up**: The ESP32 has built-in resistors that connect the input pin to 3.3V. The pin reads `HIGH` by default. When you press the button, it connects the pin directly to **Ground (GND)**, pulling the voltage down to `LOW`. 
* Therefore, with a pull-up: **Unpressed = HIGH (1)** and **Pressed = LOW (0)**.

---

## Connect it

Let's connect a temporary button to one of Kijani's GPIO pins (for example, Servo 2's Signal pin, which is **GPIO 14**).

```text
    Kijani GPIO 14 (SIG)        Tactile Button
    +-------------------+      +--------------+
    | Pin 14    [ O ] <======> | Terminal A   |
    | GND       [ O ] <======> | Terminal B   |
    +-------------------+      +--------------+
```

---

## Try it

To read this button, you would write a simple Arduino/C++ sketch or modify Kijani's firmware main loop:

```cpp
#define BUTTON_PIN 14 // Servo 2 Signal is GPIO 14
#define STATUS_LED 2

void setup() {
  Serial.begin(115200);
  
  // Configure pin with the internal pull-up resistor active
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(STATUS_LED, OUTPUT);
}

void loop() {
  // Read the state of the button
  int buttonState = digitalRead(BUTTON_PIN);
  
  if (buttonState == LOW) {
    // Button is pressed (connected to GND)
    digitalWrite(STATUS_LED, HIGH); // Turn ON LED
    Serial.println("Button Pressed!");
  } else {
    // Button is unpressed (pulled HIGH internally)
    digitalWrite(STATUS_LED, LOW);  // Turn OFF LED
  }
  delay(50); // Small debounce delay
}
```

---

## What should happen
* Normally, the status LED on Kijani is off.
* Pressing your physical button connects GPIO 14 to Ground, turning the blue status LED ON and printing "Button Pressed!" to the Serial Monitor.
* Releasing the button pulls the pin back to 3.3V, turning the status LED OFF.

---

## Experiment
Try disconnecting the button wire from GND and leaving it open in the air. Tap the bare wire with your finger. You might see the LED flicker or turn on—this is the physical illustration of a "floating" pin picking up charge from your body!

---

## Challenge
Write a small algorithm in pseudocode or C++ where pressing the button once **toggles** the LED (turns it ON if it was OFF, and OFF if it was ON) and keeps that state even after you let go of the button.

---

## Troubleshooting
* **LED is always ON?** Make sure you configured the pin as `INPUT_PULLUP` rather than standard `INPUT`. Without the pull-up, the pin floats and can read LOW randomly.
* **Nothing happens?** Verify that you are connecting the button to Kijani's GND pin, not the VCC/HV pin.

---

## Next step
Now that you understand the theory of digital inputs, let's look at how to apply this to robotics by using **bumper switches** to detect wall collisions and steer automatically!

👉 **[Lesson 16: Buttons and Bumpers](./16-buttons-bumpers.md)**
