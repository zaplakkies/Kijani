---
title: "Lesson 17: Extra Connections and Sensors"
description: Explore Kijani's expansion headers and connect analog and digital sensors.
sidebar_position: 3
---

# Lesson 17: Extra Connections and Sensors

In this lesson, you will explore the expansion ports on Kijani. We will learn what pins are available, what can safely be connected to them, and how to read analog sensors (like light sensors) and digital sensors (like ultrasonic distance sensors).

---

## What you will learn
* Kijani's expansion header pins and voltage limits.
* How to safely connect external 3.3V or 5V sensors.
* How to read an Analog Light Sensor (LDR).
* How to read an Ultrasonic Distance Sensor.

---

## What you need
* **1 × Kijani Controller Board**
* **1 × Photoresistor (LDR)** and a 10k-Ohm resistor (for analog sensing)
* **1 × HC-SR04 or HC-SR04P Ultrasonic Sensor** (for distance sensing)

---

## Background

### Expansion and Voltage Limits
The ESP32 is a **3.3 Volt microcontroller**. This is highly important:
* **Digital Input Limit**: Any voltage applied to Kijani's input pins must never exceed **3.3V**. Connecting a 5V sensor signal directly to an ESP32 pin can destroy the input circuit.
* **Safe Practice**: Always use 3.3V sensors, or use a voltage divider (resistors) to step 5V signal outputs down to 3.3V before connecting them to Kijani.

### Available Pins for Expansion
Kijani exposes multiple pins that can be repurposed for inputs or outputs:
* **GPIO 27** (Servo 1 Signal pin)
* **GPIO 14** (Servo 2 Signal pin)
* **GPIO 36** (Analog ADC Pin - reads values from `0` to `4095`)

---

## Connection Examples

### 1. Connecting an Analog Light Sensor (LDR)
To read a continuous value (like brightness), connect a photoresistor (LDR) and a 10k-Ohm resistor as a **voltage divider** connected to Kijani's ADC pin (**GPIO 36**).

```text
       3.3V Pin (Power)
            │
       [Photoresistor]
            │
            ├───────> to Kijani GPIO 36 (ADC), A1
            │
       [10k Resistor]
            │
        GND Pin (Ground)
```

**Arduino Code to Read Light Level:**
```cpp
void setup() {
  Serial.begin(115200);
}

void loop() {
  int rawValue = analogRead(36); // Reads 0 to 4095
  float percentage = (rawValue / 4095.0) * 100.0;
  
  Serial.printf("Light level: %.1f%%\n", percentage);
  delay(200);
}
```

---

### 2. Connecting an Ultrasonic Distance Sensor
An ultrasonic sensor measures distance by sending high-frequency sound pulses and timing how long it takes for the echo to bounce back.

```text
    Kijani Header Pins          HC-SR04P Sensor
    +-------------------+      +---------------+
    | 5V / HV   [ O ] <======> | VCC           |
    | GPIO 27,S1[ O ] <======> | Trig (Trigger)|
    | GPIO 14,S2[ O ] <======> | Echo          |
    | GND       [ O ] <======> | GND           |
    +-------------------+      +---------------+
```
*(Note: Ensure you use an HC-SR04P or RC-SR04 model that works safely at 3.3V logic levels).*

**Arduino Code to Measure Distance:**
```cpp
#define TRIG_PIN 27
#define ECHO_PIN 14

void setup() {
  Serial.begin(115200);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

void loop() {
  // Clear the trigger pin
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  
  // Set the trigger pin HIGH for 10 microseconds
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  
  // Measure echo return duration (microseconds)
  long duration = pulseIn(ECHO_PIN, HIGH);
  
  // Calculate distance in centimeters
  float distance = duration * 0.034 / 2;
  
  Serial.printf("Distance: %.1f cm\n", distance);
  delay(100);
}
```

---

## What should happen
* The light sensor prints a low percentage in a dark room and a high percentage when you shine a flashlight on it.
* The distance sensor prints accurate distances in centimeters as you wave your hand closer or further away.

---

## Next step
Incredible! You have mastered all individual aspects of the Kijani platform. It is now time to integrate all of these concepts together in our final **Projects** chapter!

👉 **[Lesson 18: Build a Robot](../07-projects/build-robot.md)**
