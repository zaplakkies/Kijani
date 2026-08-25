# Kijani Battle Bot — Web & Communication API Specification

This document provides a comprehensive and technical guide to the communication API of the **Kijani Battle Bot Platform**. 

The Kijani robot is built around an ESP32 microcontroller hosting an asynchronous web server. All client interfaces (e.g., custom browser control panels, mobile apps, dashboard pages) interact with the bot using this HTTP API.

---

## 1. Network & Base Address

When the robot boots up, it starts in **WiFi Access Point (AP) Mode** by default.

- **SSID (AP Name):** `MootBot_XXXX` (where `XXXX` represents a unique identifier for the bot, customizable via settings).
- **IP Address:** `10.10.10.10`
- **Base URL:** `http://10.10.10.10/`

All API endpoints are hosted relative to this Base URL.

---

## 2. API Endpoint Directory

| Endpoint | HTTP Method | Content Type | Description |
| :--- | :--- | :--- | :--- |
| [`/processcontrol`](#21-robot-control-api-processcontrol) | `GET` | `text/html` | Controls DC motors and servo positions. |
| [`/quickstatus`](#22-telemetry-api-quickstatus) | `GET` / `ANY` | `application/json` | Retrieves live battery voltage and core temperature. |
| [`/getsettings`](#23-retrieve-setting-getsettings) | `GET` / `ANY` | `application/json` | Reads a stored setting from non-volatile storage (NVS). |
| [`/updatesettings`](#24-update-setting-updatesettings) | `GET` / `ANY` | `text/plain` | Saves a new setting value into non-volatile storage (NVS). |
| [`/playrtttl`](#25-buzzer-melody-api-playrtttl) | `GET` | `text/plain` | Plays an RTTTL music string using motor coil vibration / buzzer. |
| [`/files`](#26-list-files-files) | `GET` | `application/json` | Lists all files and disk usage stats on LittleFS. |
| [`/upload`](#27-upload-file-upload) | `POST` | `text/html` | Uploads a static file to the LittleFS filesystem. |
| [`/delete`](#28-delete-file-delete) | `GET` | `text/plain` | Deletes a file from the LittleFS filesystem. |
| [`/systeminfo`](#29-system-information-systeminfo) | `GET` | `text/html` | Returns detailed diagnostic info inside a styled HTML table. |
| [`/getver`](#210-firmware-version-getver) | `GET` | `text/html` | Returns the current firmware version string. |
| [`/updatefirmware`](#211-ota-firmware-update-updatefirmware) | `POST` | `text/plain` | Performs an Over-the-Air (OTA) firmware `.bin` flash. |
| [`/reset`](#212-factory-reset-reset) | `GET` / `ANY` | `text/html` | Erases user configurations and reboots to default database settings. |

---

## 3. Endpoint Specifications

### 2.1. Robot Control API: `/processcontrol`
Updates motor speeds/directions and configures the positions of standard hobby servos. 

- **Method:** `GET`
- **Query Parameters:**
  - `M1` (optional): Motor 1 speed & direction (Range: `-255` to `255`).
  - `M2` (optional): Motor 2 speed & direction (Range: `-255` to `255`).
  - `S1` (optional): Servo 1 position (Range: `0` to `180` degrees).
  - `S2` (optional): Servo 2 position (Range: `0` to `180` degrees).

#### Motor Mapping & Scaling Rules
1. **Deadband Filter:** Values between `-5` and `5` are filtered and treated as exactly `0` (stop).
2. **Settings Scaling:** Motor speed inputs are automatically scaled by the configured maximum motor speed percentages (`MaxMotor1` and `MaxMotor2`).
   $$\text{Final Speed} = \frac{\text{Input Speed} \times \text{MaxMotorPercentage}}{100}$$
3. **Direction Inversion:** If `SwapDMotor1` or `SwapDMotor2` is enabled (`true`), the polarity of that motor's speed input is inverted ($speed = speed \times -1$).
4. **Output Swapping:** If `SwapMotors` is enabled (`true`), the physical outputs of Motor 1 and Motor 2 are swapped.

#### HTTP Response
- **Status:** `200 OK`
- **Body:** `done`

#### Example Requests
- **Drive Forward Full Speed:** `/processcontrol?M1=255&M2=255`
- **Sharp Left Turn:** `/processcontrol?M1=-255&M2=255`
- **Position Servos at 90°:** `/processcontrol?S1=90&S2=90`
- **Stop All Outputs:** `/processcontrol?M1=0&M2=0`

---

### 2.2. Telemetry API: `/quickstatus`
Fetches live power and diagnostic measurements.

- **Method:** `GET` (or `ANY`)
- **Query Parameters:** None
- **Response Format:** JSON
- **Response Fields:**
  - `result`: `"pass"`
  - `vIn`: Battery voltage in Volts (float).
  - `temperature`: ESP32 internal chip temperature in °C (float).

#### Example Response
```json
{
  "result": "pass",
  "vIn": 4.82,
  "temperature": 31.25
}
```

*Note: If `vIn > 4.5V`, the onboard battery is considered to be connected to USB charging power.*

---

### 2.3. Retrieve Setting: `/getsettings`
Retrieves a persistent configuration value from the ESP32 NVS (Non-Volatile Storage) database.

- **Method:** `GET` (or `ANY`)
- **Query Parameters:**
  - `key` (required): The setting variable key to fetch.
- **Response Format:** JSON

#### Example Request
`/getsettings?key=AP`

#### Example Success Response
```json
{
  "result": "pass",
  "key": "AP",
  "value": "MootBot_v3"
}
```

#### Example Error Response (missing `key` parameter)
```json
{
  "result": "fail"
}
```

---

### 2.4. Update Setting: `/updatesettings`
Saves or overwrites a configuration key-value pair inside the NVS database. Custom keys are accepted if you want to do some saves that are unrelated to the system workings. Like high score for a game.

- **Method:** `GET` (or `ANY`)
- **Query Parameters:**
  - `key` (required): The setting variable key to update.
  - `value` (required): The value string to store.
- **Response Format:** Plain text
- **Responses:**
  - Success: `Updated successfully` (`200 OK`)
  - Failure: `Updated failed` (`200 OK` with internal logs outputted to hardware Serial)

#### Example Request
`/updatesettings?key=SwapMotors&value=true`

---

### 2.5. Buzzer / Melody API: `/playrtttl`
Plays an RTTTL (Ring Tone Transfer Language) formatted ringtone. If a dedicated buzzer pin is not active, Kijani can play sounds by vibrating the motor coils at the specified frequencies!

- **Method:** `GET`
- **Query Parameters:**
  - `tune` (required): RTTTL-formatted song string.
- **Response Format:** Plain text

#### Example Request
`/playrtttl?tune=Jingle:d=4,o=5,b=100:8b,16d6,16c6,8e6`

#### Responses
- Success: `Playing` (`200 OK`)
- Failure: `Missing tune parameter` (`400 Bad Request`)

---

### 2.6. List Files: `/files`
Lists all static web assets saved in the ESP32's LittleFS flash storage.

- **Method:** `GET`
- **Query Parameters:** None
- **Response Format:** JSON
- **Response Fields:**
  - `used`: Used filesystem space in bytes (integer).
  - `total`: Total filesystem capacity in bytes (integer).
  - `files`: Array of file objects containing `id`, `name` (string), and `size` in bytes (integer).

#### Example Response
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
      "name": "styles.css",
      "size": 2048
    }
  ]
}
```

---

### 2.7. Upload File: `/upload`
Streams a file over standard multipart HTTP upload and writes it into LittleFS.

- **Method:** `POST`
- **Content Type:** `multipart/form-data`
- **Payload:** File field containing the binary or text file to upload.
- **Rules:** Files uploaded with the exact same name as an existing file will silently overwrite the existing file.
- **Response Format:** HTML/Plain
- **Response:** Status `200 OK` (Empty response or standard browser redirection).

---

### 2.8. Delete File: `/delete`
Removes a file from LittleFS storage.

- **Method:** `GET`
- **Query Parameters:**
  - `file` (required): The exact file name to delete (e.g., `test.html`).
- **Response Format:** Plain text

#### Responses
- Success: `Deleted` (`200 OK`)
- Missing parameter: `Missing file` (`400 Bad Request`)
- Deletion error: `Delete failed` (`500 Internal Server Error`)

---

### 2.9. System Information: `/systeminfo`
Returns a pre-formatted and styled HTML summary table listing full diagnostics.

- **Method:** `GET`
- **Query Parameters:** None
- **Response Format:** HTML (`text/html`)

#### Diagnostic Fields Rendered:
- Free RAM (RAM heap space in bytes)
- Filesystem (Used space / total space in bytes)
- MAC Address (Hardware ID with colons removed)
- Uptime (in seconds)
- Flash Chip Size (in Megabytes)
- Firmware Version compilation date
- Battery Voltage (converted from raw analog values)
- ESP32 Internal Die Temperature (in °C)

---

### 2.10. Firmware Version: `/getver`
Retrieves the firmware's compilation tag.

- **Method:** `GET`
- **Response Format:** HTML (`text/html`)
- **Example Response:** `ver: kijaniv303b`

---

### 2.11. OTA Firmware Update: `/updatefirmware`
Performs an Over-the-Air (OTA) flashing of the ESP32 application partition.

- **Method:** `POST`
- **Payload:** Uploaded compiled binary file (`firmware.bin`).
- **Safety Interlock:** Automatically cuts power to both DC motors (`M1` and `M2` set to `0`) as soon as the firmware stream starts.
- **Response:** `Update complete. Rebooting...` (`200 OK`)
- **Side Effect:** Automatically reboots the robot after a 500ms delay to boot into the newly flashed firmware partition.

---

### 2.12. Factory Reset: `/reset`
Resets the non-volatile database and restarts the robot.

- **Method:** `GET` (or `ANY`)
- **Query Parameters:**
  - `factory_reset` (optional): If provided, triggers the factory reset.
- **Response:** HTML page advising that settings have been reset, accompanied by a 10-second browser redirect back to `/index.html`.

#### Examples
- **Perform Reset:** `/reset?factory_reset=1`
- **Cancel / View Instructions:** `/reset` (triggers an error notification page and reboots without wiping settings).


---

## 4. Persistent Settings Directory

All persistent configs are loaded during startup inside the NVS namespace `"settings"`. 

These values can be fetched and modified dynamically via the `/getsettings` and `/updatesettings` endpoints.

| Settings Key | Type | Default Value | Description |
| :--- | :--- | :--- | :--- |
| `AP` | String | (Hardware unique) | SSID (name) of the hosted WiFi Access Point. |
| `APpass` | String | `""` (Open AP) | Password to secure the hosted AP. If empty, the network is unprotected. |
| `startupTune` | String | `Jingle:...` | Melody to play when the robot successfully boots up (RTTTL syntax). |
| `batteryCalibrationFactor` | Float (as String) | `"0.02352"` | Calibration factor scaling raw analog battery inputs to Millivolts. |
| `MaxMotor1` | Integer (0-100) | `"100"` | Max power output percentage for Motor 1. |
| `MaxMotor2` | Integer (0-100) | `"100"` | Max power output percentage for Motor 2. |
| `SwapMotors` | Boolean String | `"false"` | Swaps Motor A and Motor B physical outputs (checked for starting character `'t'` or `'T'`). |
| `SwapDMotor1` | Boolean String | `"false"` | Inverts rotational polarity of Motor 1 (checked for starting character `'t'` or `'T'`). |
| `SwapDMotor2` | Boolean String | `"false"` | Inverts rotational polarity of Motor 2 (checked for starting character `'t'` or `'T'`). |
| `BoostLevel` | Integer (1-4) | `"1"` | Configures the physical output voltage booster regulator (see configurations below). |

### 4.1. Boost Regulator Modes
The Kijani hardware features an adjustable boost regulator mapped directly to two output configuration pins: `Vmod1` and `Vmod2`. This enables high-performance motors or power-hungry servos to receive stable, stepped-up voltage.

- **Level 1 (5V Boost Output):** `Vmod1` (INPUT), `Vmod2` (INPUT)
- **Level 2 (6V Boost Output):** `Vmod1` (OUTPUT LOW), `Vmod2` (INPUT)
- **Level 3 (8V Boost Output):** `Vmod1` (INPUT), `Vmod2` (OUTPUT LOW)
- **Level 4 (9V Boost Output):** `Vmod1` (OUTPUT LOW), `Vmod2` (OUTPUT LOW)

> ⚠️ **Warning:** Always verify the voltage tolerances of connected servos before changing `BoostLevel`. Enabling levels higher than `5V` (Level 1) can permanently damage and burn out non-high-voltage hobby servos.

---

## 5. Web Hosting & Fallbacks

In addition to programmatic API endpoints, Kijani serves static HTML/CSS/JS assets stored in the LittleFS filesystem:

- **Static Root Path:** `/` is mapped directly to LittleFS.
- **Default Document:** `index.html`. If you browse to `http://10.10.10.10/`, Kijani automatically serves `/index.html`.
- **404 Routing Fallback:** If a requested URL is not found on the filesystem, Kijani logs the request and issues a `302 Temporary Redirect` back to `/` (`index.html`).

---

## 6. Client Integration & Polling Guidelines

To prevent overloading the lightweight ESP32 server during intense battle sessions or remote operations, use the following recommendations when building custom web or mobile frontends:

### Polling / Rate Limits
- **Robot Control (`/processcontrol`):** Target **10 Hz to 20 Hz** (an update every 50ms - 100ms) for high-performance responsive virtual joysticks or keyboards.
- **Diagnostics & Status (`/quickstatus`):** Polling every **500ms to 1000ms** (1 Hz to 2 Hz) is sufficient for reading battery health and core temperature without lag.

### JavaScript Fetch Example
Below is a simple JavaScript helper class showing how to integrate with Kijani:

```javascript
class KijaniClient {
  constructor(baseIp = '10.10.10.10') {
    this.baseUrl = `http://${baseIp}`;
  }

  /**
   * Control Motor speeds (-255 to 255) and Servos (0 to 180)
   */
  async sendControl(m1, m2, s1 = null, s2 = null) {
    let params = `M1=${m1}&M2=${m2}`;
    if (s1 !== null) params += `&S1=${s1}`;
    if (s2 !== null) params += `&S2=${s2}`;

    try {
      const response = await fetch(`${this.baseUrl}/processcontrol?${params}`);
      return await response.text();
    } catch (err) {
      console.error("Failed to send control commands:", err);
    }
  }

  /**
   * Fetch battery voltage and system temperature
   */
  async getTelemetry() {
    try {
      const response = await fetch(`${this.baseUrl}/quickstatus`);
      return await response.json();
    } catch (err) {
      console.error("Failed to fetch telemetry:", err);
    }
  }
}
```

