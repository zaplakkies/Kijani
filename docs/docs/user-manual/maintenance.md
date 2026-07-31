---
title: Maintenance
description: Update the firmware and perform a factory reset.
sidebar_position: 5
---

# Maintenance

## Firmware updates

The current firmware version is shown on the home page. To update:

1. Download the latest `.bin` file from the [GitHub releases](https://github.com/zaplakkies/kijani/releases).
2. Open the **Firmware Update** page on the robot.
3. Upload the `.bin` file.
4. Wait for the update to complete — the controller restarts automatically.

:::warning
Make sure the battery is fully charged before starting a firmware update. A power loss mid-flash can brick the board until you re-flash over USB.
:::

## Factory reset

If you forget the WiFi password:

1. Turn the controller **OFF**.
2. Short the **PGM** pins together (use a jumper wire or tweezers).
3. Turn the controller **ON**.
4. Wait for the factory reset tune.

This restores the default SSID and password but does **not** restore deleted files. If system files are missing or damaged, reconnect the board to a computer and re-upload the filesystem image via PlatformIO.

Something not working? Head to [Troubleshooting](./troubleshooting.md).
