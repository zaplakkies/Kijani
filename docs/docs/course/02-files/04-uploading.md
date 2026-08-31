---
title: "Lesson 4: Uploading Files"
description: Learn how to upload, manage, replace, and run files on Kijani.
sidebar_position: 1
---

# Lesson 4: Uploading Files

In this lesson, you will learn the ins and outs of Kijani's file management system. We will explore how to upload files, replace existing files, and download or view files directly from the web interface.

---

## What you will learn
* What files are used for on Kijani.
* How to upload files using the web interface.
* How to replace or update existing files.
* How to run, download, or view files stored on Kijani.

---

## What you need
* **1 × Kijani Controller Board** (powered ON)
* **1 × Computer or Phone** (connected to Kijani's Wi-Fi)

---

## Background

Kijani uses a filesystem called **LittleFS** to store files inside the ESP32's internal flash memory. It treats this memory exactly like a tiny USB flash drive. 

### What types of files can you store?
* **`.html`**: Webpages (the remote controls, dashboard panels).
* **`.css`**: Style sheets (defining colors, fonts, and layouts of your webpages).
* **`.js`**: JavaScript files (adding custom scripts or complicated control calculations).
* **`.txt` / `.rt`**: Simple text files or custom tunes (including RTTTL ringtone configurations).
* **`.png` / `.jpg` / `.ico`**: Images or icons displayed on your webpages.

---

## Connect it

1. Ensure Kijani is powered **ON**.
2. Connect your computer or phone to Kijani's Wi-Fi.
3. Open your browser to `http://10.10.10.10`.

---

## Try it

### 1. View Files Stored on the Board
Scroll to the bottom of the Kijani homepage dashboard. Under the **File System** or **Files** section, you will see a list of every file currently sitting inside Kijani's memory.

### 2. Uploading a File
1. Create a dummy text file named `test.txt` containing the word `Hello Kijani!`.
2. Locate the **Upload File** input block on the Kijani homepage.
3. Click **Browse** / **Choose File** and select `test.txt`.
4. Click **Upload**.
5. Once the upload finishes, verify that `test.txt` now appears in the file list on the webpage.

### 3. Viewing the File
To view the content of your newly uploaded file, click on its name in the file list, or type its direct path in your browser:

`http://10.10.10.10/test.txt`

The browser will display your text file!

### 4. Replacing an Existing File
If you want to update `test.txt`:
1. Open the file on your computer and edit the text (e.g. change it to `Hello Kijani updated!`).
2. Upload the file again using the same upload tool.
3. Because the filename is exactly the same, Kijani will **automatically overwrite** the old file with the new one. No need to delete the old one first!

---

## What should happen
* Uploaded files appear in the file list.
* Typing the direct file URL displays the file content or runs the HTML/JS file.
* Uploading a file with an identical name overwrites the previous version.

---

## Experiment
Create an image file (less than 50 KB) named `logo.png` or `avatar.png` on your computer. Upload it to Kijani and try loading it directly in your browser: `http://10.10.10.10/avatar.png`.

---

## Challenge
Find out how much space is left on your Kijani board. 
*(Hint: Look closely at the top or bottom of the file system dashboard page—is there a line showing "Free space" or "Total space"?)*

---

## Troubleshooting
* **File doesn't appear?** Make sure your filename has no weird characters or spaces. Stick to simple names like `car.html` or `style.css`.
* **File is too big?** Kijani has limits on storage. If a file is too large (like a high-res photo), the upload will fail.

---

## Next step
Now that you know how to upload files, let's explore persistent storage, limitations, and how Kijani manages files across reboots.

👉 **[Lesson 5: Storing and Managing Files](./05-storing.md)**
