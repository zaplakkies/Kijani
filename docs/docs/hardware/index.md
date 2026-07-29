---
id: intro
title: Hardware Overview
---

import { CpuIcon } from '@phosphor-icons/react';

# <CpuIcon /> Hardware Overview

Welcome to the Kijani hardware documentation.

This section covers the PCB design, schematic, and downloadable project files for the robot hardware.

## Main Components

|    Component | Purpose                              |
| -----------: | :----------------------------------- |
|    **ESP32** | Main processor                       |
|    **CH340** | USB serial programming               |
|    **Motor** | Drivers Dual DC motor control        |
|    **Boost** | Regulator Selectable higher voltage  |
|     **LiPo** | Charger Single-cell battery charging |
|    **Servo** | Outputs Servo control                |
| **LittleFS** | Web interface storage                |

## Recommended Hardware

### Recommended Drive Motors

We recommend:
- N20 gear motors
- Micro metal gear motors
- TT motors (lightweight robots only)

**Typical Voltage**: 3V–6V

**Recommended Current**: \<1A continuous per motor

:::danger[Stall Current]

Stall current can be much higher than running current.

_Always test motors before combat use._

:::

### Recommended Servos

We recommend:
- SG90
- MG90S
- Metal gear micro servos

:::danger[Servo Voltage]

The boost converter can raise voltage higher than some servos can tolerate.


Before enabling boost mode, always verify:
- Servo voltage rating
- Regulator voltage settings
- Battery voltage

> Incorrect voltage can permanently damage servos.

:::

### Recommended Batteries

**Recommendation**: 1S LiPo (3.7V nominal)

Typical Sizes:
- 300mAh
- 500mAh
- 850mAh
- 1000mAh

:::caution[Safety]

LiPo batteries can be dangerous if:
- punctured
- overcharged
- short circuited
- physically damaged

Always:
- supervise charging
- use correct polarity
- inspect batteries regularly
- stop using swollen batteries

:::
