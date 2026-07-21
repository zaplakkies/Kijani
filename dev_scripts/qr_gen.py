# Reads ESP32 MAC address & generates QR code based on it in assets/qr/
# Usage: pio run -t qr_gen

# This file both registers the `qr_gen` PlatformIO target and exposes helpers
# for other scripts (e.g. append_qr_to_pdf.py) to reuse.

import os
import re
import subprocess
import shutil
import sys
import time
from pathlib import Path

# Detect SCons / PlatformIO execution environment. Import("env") only when available.
_scons_available = True
try:
    Import  # if NameError -> not running as SCons script
except NameError:
    _scons_available = False

if _scons_available:
    # Import env provided by SCons/PlatformIO into module globals
    Import("env")

# Optional imaging libraries
try:
    from PIL import Image, ImageDraw, ImageFont
except Exception:
    Image = ImageDraw = ImageFont = None

try:
    import qrcode
except Exception:
    qrcode = None

# wifi-qrcode-generator optional (best-effort)
try:
    from wifi_qrcode_generator.generator import wifi_qrcode
except Exception:
    try:
        import wifi_qrcode_generator as _wq
        wifi_qrcode = getattr(_wq, "wifi_qrcode", None)
    except Exception:
        wifi_qrcode = None

OUT_DIR = Path("assets") / "qr"
OUT_DIR.mkdir(parents=True, exist_ok=True)

def run_cmd(cmd, timeout=10):
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=timeout, universal_newlines=True)
        return out
    except Exception:
        return None

# --- Serial port / MAC helpers (unchanged logic, exported) ---
def _is_valid_serial_port(port):
    # Accept: 'COMx', '/dev/tty*', or similar
    if not port or not isinstance(port, str):
        return False
    if re.match(r"^(COM[0-9]+)$", port):  # Windows
        return True
    if re.match(r"^/dev/tty[A-Za-z0-9_.-]+$", port):  # Linux/macOS
        return True
    return False

def detect_serial_port():
    p = os.environ.get("UPLOAD_PORT") or os.environ.get("PIO_UPLOAD_PORT")
    if p:
        if _is_valid_serial_port(p):
            print("Using UPLOAD_PORT from env:", p)
            return p
        else:
            print("Refusing suspicious port value from environment variable:", repr(p))
    try:
        import serial.tools.list_ports as list_ports
        ports = list_ports.comports()
        if ports:
            for port in ports:
                desc = (port.description or "") + " " + (port.manufacturer or "")
                if any(k in desc for k in ("CP210", "CH340", "FTDI", "Silicon", "USB Serial")):
                    print("Auto-detected serial port:", port.device)
                    return port.device
            print("Auto-detected serial port (fallback):", ports[0].device)
            return ports[0].device
    except Exception:
        pass
    pio = shutil.which("pio") or shutil.which("platformio")
    if pio:
        out = run_cmd([pio, "device", "list"])
        if out:
            m = re.search(r'(COM\d+|/dev/tty[A-Za-z0-9_.-]+)', out)
            if m:
                port = m.group(1)
                print("Found port from 'pio device list':", port)
    try:
        import serial.tools.list_ports as list_ports
        ports = list_ports.comports()
        if ports:
            for port in ports:
                desc = (port.description or "") + " " + (port.manufacturer or "")
                if any(k in desc for k in ("CP210", "CH340", "FTDI", "Silicon", "USB Serial")):
                    print("Auto-detected serial port:", port.device)
                    return port.device
            print("Auto-detected serial port (fallback):", ports[0].device)
            return ports[0].device
    except Exception:
        pass
    pio = shutil.which("pio") or shutil.which("platformio")
    if pio:
        out = run_cmd([pio, "device", "list"])
        if out:
            m = re.search(r'(COM\d+|/dev/tty[A-Za-z0-9_.-]+)', out)
            if m:
                port = m.group(1)
                print("Found port from 'pio device list':", port)
                return port
    print("Could not auto-detect serial port. Set environment variable UPLOAD_PORT (e.g. UPLOAD_PORT=COM3).")
    return None

def read_mac_from_device(port, serial_timeout=5):
    def try_esptool_path(path):
        if not path or not os.path.exists(path):
            return None
        if path.lower().endswith(".py"):
            cmd_base = [sys.executable, path]
        else:
            cmd_base = [path]
        variants = [["--port", port, "read_mac"],
                    ["--port", port, "read-mac"],
                    ["--port", port, "read_mac"]]
        for tail in variants:
            cmd = cmd_base + tail
            print("Running:", " ".join(cmd))
            out = run_cmd(cmd, timeout=20)
            if not out:
                continue
            m = re.search(r"MAC[:\s]+([0-9A-Fa-f:]{17})", out)
            if m:
                mac = m.group(1)
                print("Read MAC via esptool:", mac)
                return mac
            m2 = re.search(r"([0-9A-Fa-f]{2}(:[0-9A-Fa-f]{2}){5})", out)
            if m2:
                mac = m2.group(1)
                print("Read MAC via esptool (fallback):", mac)
                return mac
        return None

    pio_esptool = os.path.join(os.path.expanduser("~"), ".platformio", "packages", "tool-esptoolpy", "esptool.py")
    mac = try_esptool_path(pio_esptool)
    if mac:
        return mac
    for candidate in ("esptool.py", "esptool"):
        path = shutil.which(candidate)
        if path:
            mac = try_esptool_path(path)
            if mac:
                return mac

    print("esptool not found / failed to return MAC. Attempting serial fallback...")
    try:
        import serial
    except Exception:
        print("pyserial not installed; cannot use serial fallback.")
        return None

    try:
        ser = serial.Serial(port, baudrate=115200, timeout=0.5)
    except Exception as e:
        print("Failed to open serial port", port, ":", e)
        return None

    try:
        ser.dtr = False
        ser.rts = False
        time.sleep(0.05)
        ser.dtr = True
        ser.rts = True
        time.sleep(0.05)
        ser.reset_input_buffer()
    except Exception:
        pass

    mac_regex = re.compile(r"([0-9A-Fa-f]{2}(:[0-9A-Fa-f]{2}){5})")
    deadline = time.time() + float(serial_timeout)
    buffer = ""
    try:
        while time.time() < deadline:
            chunk = ser.read(256)
            if not chunk:
                continue
            try:
                txt = chunk.decode('utf-8', errors='ignore')
            except Exception:
                txt = repr(chunk)
            buffer += txt
            m = re.search(r"MAC[:\s]+([0-9A-Fa-f:]{17})", buffer)
            if m:
                mac = m.group(1)
                print("Read MAC from serial (MAC: ...):", mac)
                ser.close()
                return mac
            m2 = mac_regex.search(buffer)
            if m2:
                mac = m2.group(1)
                print("Read MAC from serial (generic):", mac)
                ser.close()
                return mac
        print("Serial fallback: no MAC found in output (timeout). Last 200 chars:")
        print(buffer[-200:])
    finally:
        try:
            ser.close()
        except Exception:
            pass

    return None

# --- QR creation helpers (exported both as on-disk saver and in-memory creator) ---
def make_wifi_qr_image_try_library(ssid):
    if wifi_qrcode is None:
        return None
    call_variants = [
        (ssid, False, "", None),
        (ssid, False, None, None),
        (ssid,),
        (ssid, False),
    ]
    for args in call_variants:
        try:
            qrobj = wifi_qrcode(*args)
            if hasattr(qrobj, "make_image"):
                img = qrobj.make_image()
                return img.convert("RGB")
            if Image and isinstance(qrobj, Image.Image):
                return qrobj.convert("RGB")
        except TypeError:
            continue
        except Exception:
            return None
    return None

def make_wifi_qr_image_manual_open(ssid, box_size=8, border=4):
    if qrcode is None:
        return None
    payload = f'WIFI:T:nopass;S:{ssid};;'
    qr = qrcode.QRCode(box_size=box_size, border=border)
    qr.add_data(payload)
    qr.make(fit=True)
    img = qr.make_image()
    return img.convert("RGB")

def make_sticker_image_obj(ssid, dashboard_url=None):
    """
    Return a PIL.Image object that is the sticker (QR + SSID text).
    Does NOT save to disk. If Pillow or qrcode is unavailable, returns None.
    """
    if Image is None or qrcode is None:
        print("Pillow or qrcode not available; cannot create in-memory sticker image.")
        return None

    qr_wifi = make_wifi_qr_image_try_library(ssid)
    if qr_wifi is None:
        qr_wifi = make_wifi_qr_image_manual_open(ssid, box_size=4, border=1)
    if qr_wifi is None:
        print("Could not create Wi-Fi QR image (missing libs).")
        return None

    padding_qr = 2
    padding_below_text = 5

    draw = ImageDraw.Draw(qr_wifi)
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 10)
    except Exception:
        font = ImageFont.load_default()

    text = f"{ssid}"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    W = qr_wifi.width + padding_qr * 2
    H = qr_wifi.height + text_h + padding_qr + padding_below_text

    canvas_img = Image.new("RGB", (W, H), "white")
    canvas_img.paste(qr_wifi, (padding_qr, padding_qr))

    draw = ImageDraw.Draw(canvas_img)
    text_x = (W - text_w) // 2
    text_y = qr_wifi.height + padding_qr
    draw.text((text_x, text_y), text, font=font, fill=(0, 0, 0))

    return canvas_img

def create_qr_for_attached_device(save_png=True, out_dir=OUT_DIR):
    """
    Detect the serial-attached device, read MAC, produce a sticker.
    If save_png is True: saves PNG to out_dir and returns (Path_to_png, ssid).
    If save_png is False: returns (PIL.Image, ssid).
    """
    port = detect_serial_port()
    if not port:
        print("No serial port found.")
        return (None, None)

    mac = read_mac_from_device(port)
    if not mac:
        print("Failed to read MAC from device.")
        return (None, None)

    ssid = f"Palooka_{mac.upper()}"
    dashboard = "http://192.168.4.1/"

    img_obj = make_sticker_image_obj(ssid, dashboard)
    if img_obj is None:
        # fallback: just return ssid string so caller can handle
        return (None, ssid)

    if save_png:
        ssid_filename = ssid.replace(":", "-")
        out_png = out_dir / f"{ssid_filename}.png"
        out_png.parent.mkdir(parents=True, exist_ok=True)
        img_obj.save(out_png)
        return (out_png, ssid)
    else:
        return (img_obj, ssid)

def qr_action(target, source, env):
    print("==== qr-gen: generate QR/sticker for attached device ====")
    path_or_obj, ssid = create_qr_for_attached_device(save_png=True)
    if path_or_obj:
        print("Saved sticker PNG:", path_or_obj)
        return 0
    else:
        print("Failed to create sticker PNG. SSID payload (if MAC read):", ssid)
        return 1

if _scons_available:
    env.AddCustomTarget(
        "qr_gen",
        None,
        qr_action,
        title="QR / sticker generator",
        description="Detects attached board, reads MAC, and generates Wi-Fi (open) QR sticker (PNG)"
    )
