---
title: "Lesson 5: Storing and Managing Files"
description: Learn about persistent storage, naming conventions, and what happens when Kijani reboots.
sidebar_position: 2
---

# Lesson 5: Storing and Managing Files

In this lesson, we will dive deeper into Kijani's persistent storage, file naming rules, and what happens to your files when Kijani loses power or reboots.

---

## What you will learn
* What persistent (non-volatile) storage means.
* Best practices for file names and extensions.
* How to organize multiple projects on the same board.
* What happens to files during and after a reboot.
* The physical limitations of Kijani's storage.

---

## What you need
* **1 × Kijani Controller Board** (powered ON)
* **1 × Computer or Phone** (connected to Kijani's Wi-Fi)

---

## Background

### Persistent Storage
When you turn off your computer or phone, your documents don't disappear. That is because they are saved in **non-volatile memory** (your hard drive or SSD). 

Kijani's LittleFS partition uses the ESP32's internal flash memory, which is also non-volatile. Any file you upload remains safely written on the chip, even if you turn the power switch OFF, unplug the battery, or if the board runs out of power.

---

## Try it

Let's test this behavior.

### Step 1: Upload a Marker File
1. Create a simple text file named `reboottest.txt` with the text: `I survived a reboot!`.
2. Upload this file to your Kijani board.
3. Open your browser to `http://10.10.10.10/reboottest.txt` to confirm it is there.

### Step 2: Reboot the Board
1. Slide Kijani's power switch to **OFF**.
2. Wait 5 seconds.
3. Slide the power switch back to **ON**.
4. Reconnect your computer or phone to Kijani's Wi-Fi network.

### Step 3: Check the File
1. Open your browser and navigate back to `http://10.10.10.10/reboottest.txt`.
2. The page loads and displays `I survived a reboot!`.

---

## Storing Rules & Limitations

To keep your files working perfectly, follow these guidelines:

### 1. File Naming Rules
* **No Spaces**: Never use spaces in file names (use `my_project.html` instead of `my project.html`).
* **Short Names**: Keep names under 31 characters.
* **Lowercase Recommended**: It is best to use lowercase names to avoid typos.

### 2. Organizing Projects
Since Kijani is a flat filesystem (folders are simulated), organize projects by prefixing filenames:
* Project 1 files: `car_index.html`, `car_style.css`, `car_control.js`
* Project 2 files: `piano_index.html`, `piano_style.css`, `piano_sound.js`

### 3. Flash Memory Limitations
* **Capacity**: The entire filesystem partition is **1.4 MB**.
* **Limit Your Images**: High-resolution photos from a smartphone can be 3 MB or more—far too large for Kijani! If you need images on your web pages, shrink them to under **50 KB** before uploading, or use links to external internet images if the client device has an internet connection.

---

## What should happen
* Stored files survive full power-downs and reboots perfectly.
* Storing small files is instant; larger files take a few seconds to upload.

---

## Experiment
Check the status of Kijani's memory on the main dashboard. Try to upload a slightly larger image and see if the upload speed is affected.

---

## Challenge
Find out how to delete a file you no longer need. 
*(Hint: Is there a "Delete", "Trash", or "Bin" icon next to filenames in Kijani's stored files list? Try clicking it on `reboottest.txt`!)*

---

## Troubleshooting
* **File disappeared?** Kijani does not delete files automatically. If a file is missing, it is likely the upload was interrupted before completion, or the file size exceeded the free limit.
* **Storage Full?** Go through your file list and delete any old dummy tests or large files you aren't using anymore.

---

## Next step
Now that you are a master of file management, let's create a complete, well-organized project that coordinates multiple files!

👉 **[Lesson 6: Project Files and Running](./06-project-files.md)**
