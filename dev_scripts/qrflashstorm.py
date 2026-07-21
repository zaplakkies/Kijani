#  - Watches serial ports for new device connections (poll loop).
#  - For each new device it runs:
#      pio run -t deploy
#      pio run -t append_qr_to_pdf
#    with UPLOAD_PORT / PIO_UPLOAD_PORT set to the detected device.
#  - Runs until interrupted (Ctrl+C).

# Usage: pio run -t qrflashstorm

# Tip:  Write an index starting at 1 on each board you connect.
#       This will make it much easier to identify which QR code
#       belongs to which board after flashing & printing the PDF.

# ===== WARNING =====
# Due to the way PlatformIO/SCons runs custom targets, Ctrl+C may not
# reliably stop this process when running:
#     pio run -t qrflashstorm

# You must manually terminate the process if Ctrl+C fails.

# Manually terminating the process:
#   Windows (PowerShell):
#       1. Find the PID of the Python process running the watcher:
#           Get-Process | Where-Object { $_.ProcessName -match 'pio|platformio|python' } | Format-Table Id, ProcessName, Path -AutoSize
#       2. Kill the process by PID (replace <PID> with actual number):
#           Stop-Process -Id <PID> -Force
#   Windows (Command Prompt):
#       1. List Python processes:
#           tasklist | findstr python
#       2. Kill by PID (replace <PID>):
#           taskkill /PID <PID> /F
#   macOS/Linux:
#       1. Find the PID of the Python process:
#           ps aux | grep qrflashstorm
#       2. Kill by PID (replace <PID>):
#           kill -9 <PID>

# This affects only the PlatformIO target watcher; child processes
# spawned for 'deploy' and 'append_qr_to_pdf' are also terminated
# automatically when you kill the watcher process.
# ===== WARNING =====

# ===== IMPORTANT ====
# TODO: Fix KeyboardInterrupt handling since it currently doesn't work
# ====================

from __future__ import annotations
Import("env")

import signal
import os
import sys
import time
import shutil
import subprocess
from datetime import datetime

# Prefer using pyserial's list_ports if available for robust detection.
try:
    import serial.tools.list_ports as list_ports
except Exception:
    list_ports = None

# Keywords to filter which serial ports to consider "boards"
SERIAL_KEYWORDS = ("CP210", "CH340", "FTDI", "Silicon", "USB Serial", "Arduino", "ESP32", "Silicon Labs")
POLL_INTERVAL = 1.0  # seconds


def _log(*parts):
    print(f"[qrflashstorm {datetime.now().isoformat(timespec='seconds')}] ", *parts)


def _find_pio_executable():
    for name in ("pio", "platformio"):
        path = shutil.which(name)
        if path:
            return path
    return None

def _list_serial_ports(filter_keywords=True):
    """
    Return a set of device names (e.g. '/dev/ttyUSB0' or 'COM3') corresponding to microcontroller boards.
    Filters out unrelated USB-serial devices like keyboards, mice, etc.
    """
    ports_set = set()

    if list_ports:
        for p in list_ports.comports():
            desc = (p.description or "") + " " + (p.manufacturer or "")
            device = p.device

            # Optional: skip devices with no VID/PID (likely not a dev board)
            if p.vid is None or p.pid is None:
                continue

            if filter_keywords:
                lowered = desc.lower()
                if any(k.lower() in lowered for k in SERIAL_KEYWORDS):
                    ports_set.add(device)
            else:
                ports_set.add(device)
        return ports_set

    # Fallback to PlatformIO's device list if pyserial not available
    pio = _find_pio_executable()
    if pio:
        try:
            out = subprocess.check_output([pio, "device", "list"], universal_newlines=True, stderr=subprocess.STDOUT, timeout=5)
            for line in out.splitlines():
                tokens = line.split()
                for t in tokens:
                    if t.startswith("/dev/") or t.upper().startswith("COM"):
                        ports_set.add(t)
        except Exception:
            pass

    return ports_set

# keep track of the currently-running child so signal handler can access it
_current_child_proc = None

def terminate_proc(proc):
    """Try to gracefully stop proc, then force-kill if needed."""
    if not proc:
        return
    try:
        if os.name == "nt":
            # send CTRL_BREAK to the process group so the whole group can see it (if available)
            try:
                if hasattr(signal, "CTRL_BREAK_EVENT"):
                    proc.send_signal(signal.CTRL_BREAK_EVENT)
            except Exception:
                pass
            # allow some time then terminate/kill as fallback
            time.sleep(0.5)
            if proc.poll() is None:
                try:
                    proc.terminate()
                except Exception:
                    pass
            time.sleep(0.3)
            if proc.poll() is None:
                try:
                    proc.kill()
                except Exception:
                    pass
        else:
            # POSIX: send SIGTERM to the process group
            try:
                os.killpg(proc.pid, signal.SIGTERM)
            except Exception:
                # fallback: try terminate single process
                try:
                    proc.terminate()
                except Exception:
                    pass
            time.sleep(0.5)
            if proc.poll() is None:
                try:
                    os.killpg(proc.pid, signal.SIGKILL)
                except Exception:
                    try:
                        proc.kill()
                    except Exception:
                        pass
    except Exception:
        pass


def _run_pio_target(pio_exec, target, upload_port, workdir):
    """
    Start the pio command in its own process-group/session so we can stop it.
    Return True on success (exit code 0), False otherwise.
    """
    global _current_child_proc
    proc = None

    env = os.environ.copy()
    env["UPLOAD_PORT"] = upload_port
    env["PIO_UPLOAD_PORT"] = upload_port

    cmd = [pio_exec, "run", "-t", target]
    _log("Running:", " ".join(cmd), "(UPLOAD_PORT=" + upload_port + ")")

    # Start child in a new process group / session
    popen_kwargs = dict(cwd=workdir, env=env)
    if os.name == "nt":
        # CREATE_NEW_PROCESS_GROUP allows sending CTRL_BREAK_EVENT to this group
        popen_kwargs["creationflags"] = getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0)
    else:
        # start a new session so the child is leader of its own process group
        popen_kwargs["start_new_session"] = True

    try:
        proc = subprocess.Popen(cmd, **popen_kwargs)
        _current_child_proc = proc

        # Wait while being interruptible; poll frequently so KeyboardInterrupt can be caught
        while True:
            ret = proc.poll()
            if ret is not None:
                break
            time.sleep(0.05)

        _current_child_proc = None
        return (ret == 0)
    except KeyboardInterrupt:
        _log("KeyboardInterrupt received: terminating child process...")
        try:
            terminate_proc(proc)
            raise
        except Exception:
            pass
        try:
            if proc:
                proc.wait(timeout=5)
        except Exception:
            pass
        _current_child_proc = None
        return False
    except Exception as e:
        _log("Error running target:", e)
        _current_child_proc = None
        # ensure any partially-started proc is cleaned up
        try:
            terminate_proc(proc)
        except Exception:
            pass
        return False

def watch_action(target, source, env):
    """
    This function is called by PlatformIO when you run:
        pio run -t qrflashstorm
    """
    # Try to get project dir from PlatformIO env, otherwise fallback to cwd
    repo_root = None
    try:
        # env is an SCons construction environment; platformio exposes PROJECT_DIR
        if "PROJECT_DIR" in env:
            repo_root = env["PROJECT_DIR"]
        else:
            # Some env variants offer a helper method
            repo_root = env.GetProjectDir()
    except Exception:
        repo_root = None

    if not repo_root:
        # last fallback
        repo_root = os.getcwd()

    repo_root = os.path.abspath(repo_root)

    pio_exec = _find_pio_executable()
    if not pio_exec:
        _log("Could not find 'pio' or 'platformio' in PATH. Make sure PlatformIO CLI is installed and in PATH.")
        return 1

    _log("Starting qrflashstorm in repo:", repo_root)
    _log("Press Ctrl+C to stop.")
    prev_ports = set()

    try:
        while True:
            current_ports = _list_serial_ports(filter_keywords=True)
            new_ports = current_ports - prev_ports
            removed = prev_ports - current_ports

            if new_ports:
                for dev in sorted(new_ports):
                    _log("Detected new serial device:", dev)
                    # small settle delay
                    time.sleep(0.2)

                    # Run deploy then append_qr_to_pdf
                    ok = _run_pio_target(pio_exec, "deploy", dev, repo_root)
                    if not ok:
                        _log("deploy failed for", dev, "; skipping append_qr_to_pdf")
                    else:
                        ok2 = _run_pio_target(pio_exec, "append_qr_to_pdf", dev, repo_root)
                        if not ok2:
                            _log("append_qr_to_pdf failed for", dev)
                        else:
                            _log("Completed deploy + append_qr_to_pdf for", dev)

                # update known ports after handling new ones
                prev_ports = _list_serial_ports(filter_keywords=True)

            elif removed:
                _log("Device(s) removed:", ", ".join(sorted(removed)))
                prev_ports = current_ports

            time.sleep(POLL_INTERVAL)

    except KeyboardInterrupt:
        _log("Watcher interrupted by user (Ctrl+C). Cleaning up...")
        if _current_child_proc:
            terminate_proc(_current_child_proc)
        sys.exit(0)
    except Exception as e:
        _log("Unexpected error in watcher:", e)
        return 1


# Register the custom target with PlatformIO/SCons
env.AddCustomTarget(
    "qrflashstorm",
    None,
    watch_action,
    title="Watch serial ports and deploy on connect",
    description="Listen for connection of serial devices and run 'pio run -t deploy' and 'pio run -t append_qr_to_pdf' each time a device is connected."
)
