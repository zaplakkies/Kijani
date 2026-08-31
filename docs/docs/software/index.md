---
id: intro
sidebar_position: 1
title: Battle Bot ESP32 API Guide
---

# Battle Bot ESP32 API Guide

The Battle Bot ESP32 exposes an HTTP API through its built-in web server. The API can be used to control motors and servos, monitor telemetry, manage settings, and interact with the ESP32 filesystem.

## Base Address

All API routes are hosted on the ESP32 web server.

Example:

```text
http://10.10.10.10/
````

---

# Control API

## `/processcontrol`

Controls motors and servos.

**Method:** `GET`

### Parameters

| Parameter | Range           | Description                 |
| --------- | --------------- | --------------------------- |
| `M1`      | `-255` to `255` | Motor 1 speed and direction |
| `M2`      | `-255` to `255` | Motor 2 speed and direction |
| `S1`      | `0` to `180`    | Servo 1 position            |
| `S2`      | `0` to `180`    | Servo 2 position            |

### Motor Direction

| Value    | Action  |
| -------- | ------- |
| Positive | Forward |
| Negative | Reverse |
| `0`      | Stop    |

Values between `-5` and `5` are treated as zero.

### Examples

#### Drive Forward

```text
/processcontrol?M1=255&M2=255
```

#### Turn Left

```text
/processcontrol?M1=-255&M2=255
```

#### Stop Motors

```text
/processcontrol?M1=0&M2=0
```

#### Move Servo

```text
/processcontrol?S1=90
```

#### Combined Request

```text
/processcontrol?M1=120&M2=120&S1=45
```

### Response

```text
done
```

---

# Telemetry API

## `/quickstatus`

Returns live battery voltage and internal temperature.

**Method:** `GET`

### Response

```json
{
  "result": "pass",
  "vIn": 4.82,
  "temperature": 31.25
}
```

## Battery Charging Detection

If:

```text
vIn > 4.5V
```

then the unit is considered to be charging.

---

# Settings API

There are some setting that the unit uses like AP or APpassword. you can however use any setting key you like to save in your javascript.

## `/getsettings`

Returns a stored setting value.

**Method:** `GET`

### Parameters

| Parameter | Description |
| --------- | ----------- |
| `key`     | Setting key |

### Example

```text
/getsettings?key=AP
```

### Response

```json
{
  "result": "pass",
  "key": "AP",
  "value": "BattleBot"
}
```

---

# Update Settings API

## `/updatesettings`

Updates a stored setting.

**Method:** `GET`

### Parameters

| Parameter | Description |
| --------- | ----------- |
| `key`     | Setting key |
| `value`   | New value   |

### Example

```text
/updatesettings?key=AP&value=BattleBot
```

### Response

```text
Updated successfully
```

---

# File System API

## `/files`

Returns all files stored on the ESP32 filesystem.

**Method:** `GET`

### Response

```json
{
  "used": 123456,
  "total": 1048576,
  "files": [
    {
      "id": 0,
      "name": "index.html",
      "size": 1024
    },
    {
      "id": 1,
      "name": "control.html",
      "size": 4096
    }
  ]
}
```

### Response Fields

| Field   | Description                              |
| ------- | ---------------------------------------- |
| `used`  | Filesystem space currently used in bytes |
| `total` | Total filesystem size in bytes           |
| `files` | Array containing the stored files        |
| `id`    | File ID                                  |
| `name`  | Filename                                 |
| `size`  | File size in bytes                       |

---

# Upload API

## `/upload`

Uploads a file to the ESP32 filesystem.

**Method:** `POST`

The file must be uploaded using a multipart form field named:

```text
file
```

### Example HTML

```html
<form action="/upload" method="POST" enctype="multipart/form-data">
  <input type="file" name="file">
  <button type="submit">Upload</button>
</form>
```

---

# Delete File API

## `/delete`

Deletes a file from the filesystem.

**Method:** `GET`

### Parameters

| Parameter | Description |
| --------- | ----------- |
| `file`    | Filename    |

### Example

```text
/delete?file=index.html
```

### Response

```text
Deleted
```

---

# System Information API

## `/systeminfo`

Returns system information as an HTML page.

**Method:** `GET`

### Information Included

* Free RAM
* Filesystem usage
* MAC address
* Uptime
* Flash size
* Firmware version
* Battery voltage
* Temperature

### Example

```text
/systeminfo
```

---

# Version API

## `/getver`

Returns the firmware version string.

**Method:** `GET`

### Example Response

```text
ver:kijaniv1
```

---

# Factory Reset API

## `/reset`

Factory resets the unit.

**Method:** `GET`

### Parameters

| Parameter       | Description |
| --------------- | ----------- |
| `factory_reset` | Required    |

### Example

```text
/reset?factory_reset=1
```

---

# Static File Hosting

The ESP32 serves all files stored in LittleFS.

Examples:

```text
/index.html
/control.html
/loading.gif
/style.css
```

A file such as:

```text
/index.html
```

can be accessed using:

```text
http://10.10.10.10/index.html
```

---

# Recommended Frontend Design

Custom interfaces can be built using standard web technologies:

* HTML
* CSS
* JavaScript
* Fetch API

Mobile-friendly interfaces can also use:

* Touch controls
* Virtual joysticks
* Large buttons
* Responsive layouts

## Example JavaScript

The API can be accessed directly from JavaScript using the Fetch API.

```javascript
fetch('/processcontrol?M1=255&M2=255')
  .then(response => response.text())
  .then(data => {
    console.log(data);
  });
```

## Recommended Update Rates

| API               | Recommended Rate |
| ----------------- | ---------------- |
| `/processcontrol` | 10–20 Hz         |
| `/quickstatus`    | 1–2 Hz           |

Motor control should normally be updated at approximately 10–20 times per second.

Telemetry such as battery voltage and temperature only needs to be updated approximately 1–2 times per second.

---

# Example Frontends

The Battle Bot filesystem contains example frontend files that can be used when developing custom interfaces.

Examples include:

```text
/control.html
/test.html
```

These files can be viewed as examples of how to communicate with the Battle Bot API from a web interface.

---

# API Summary

| Endpoint          | Method | Purpose                              |
| ----------------- | ------ | ------------------------------------ |
| `/processcontrol` | GET    | Control motors and servos            |
| `/quickstatus`    | GET    | Read battery voltage and temperature |
| `/getsettings`    | GET    | Read a stored setting                |
| `/updatesettings` | GET    | Update a stored setting              |
| `/files`          | GET    | List filesystem files                |
| `/upload`         | POST   | Upload a file                        |
| `/delete`         | GET    | Delete a file                        |
| `/systeminfo`     | GET    | Display system information           |
| `/getver`         | GET    | Get firmware version                 |
| `/reset`          | GET    | Factory reset the unit               |

```
```

