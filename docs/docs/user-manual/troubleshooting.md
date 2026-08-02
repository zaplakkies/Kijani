---
title: Troubleshooting
description: Common problems and how to fix them.
sidebar_position: 6
---

# Troubleshooting

<FeatureGrid>
  <FeatureCard refdes="WiFi" title="Can't see the WiFi network">
    Check that the battery is connected and the switch is ON. Listen for the startup tune. If there's no tune, the battery may be flat — charge it over USB and try again.
  </FeatureCard>
  <FeatureCard refdes="M1" title="Robot drives backwards">
    Swap the two wires on the affected motor, or invert the direction in the settings page.
  </FeatureCard>
  <FeatureCard refdes="S1" title="Servo doesn't move">
    Check the servo header orientation (brown/black wire to the square pad), confirm the battery is charged, and verify the servo is plugged into the header your control page addresses (S1 or S2).
  </FeatureCard>
  <FeatureCard refdes="BT1" title="Board restarts under load">
    Usually a low battery. Charge fully and retry. If it persists, check for short circuits on the motor wiring.
  </FeatureCard>
  <FeatureCard refdes="PGM" title="Forgot the WiFi password">
    Perform a system recovery (short the PGM pins, power cycle, wait for the tune).
  </FeatureCard>
  <FeatureCard refdes="FS" title="Deleted an important file">
    Reconnect the board to a computer via USB and re-upload the LittleFS filesystem image through PlatformIO. There is a backup index.html on by default so if you broke the origional you can try connect to 10.10.10.10/indexbak.html
  </FeatureCard>
</FeatureGrid>
