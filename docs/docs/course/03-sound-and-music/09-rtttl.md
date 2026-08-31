---
title: "Lesson 9: RTTTL Music Files"
description: Learn the classic Ring Tone Text Transfer Language (RTTTL) format and play full songs.
sidebar_position: 3
---

# Lesson 9: RTTTL Music Files

In this lesson, you will learn about **RTTTL (Ring Tone Text Transfer Language)**, a vintage file format used by old Nokia cell phones to play monophonic ringtones. You will understand how to write music in text, upload song files, and play full melodies on your robot!

---

## What you will learn
* What RTTTL is and how the file format is structured.
* How to read notes, durations, octaves, and tempos.
* How to create or edit your own RTTTL tunes.
* How to play RTTTL ringtones from Kijani's interface or API.

---

## What you need
* **1 × Kijani Controller Board** (powered ON)
* **1 × Motor** or speaker (connected to Motor 1)
* **1 × Computer or Phone**

---

## Background

### What is RTTTL?
In the late 1990s, phones couldn't play MP3 files. Instead, they played simple monophonic (one note at a time) beeps. **RTTTL** was created as a standard text format to write down these songs.

An RTTTL string is divided into three sections separated by colons (`:`):

```text
Name : Settings : Notes
```

Let's look at an example:
```text
Scale:d=4,o=5,b=120:c,d,e,f,g,a,b,c6
```

### 1. Name Section
* `Scale`: The name of the song (up to 10 characters).

### 2. Settings Section
* `d=4`: Default note duration (4 = quarter note, 8 = eighth note, 16 = sixteenth note, etc.).
* `o=5`: Default octave (usually ranges from 4 to 7).
* `b=120`: Tempo in Beats Per Minute (BPM). Faster tempo = faster song!

### 3. Notes Section
A list of notes separated by commas.
* Notes are letters: `c, d, e, f, g, a, b`. A rest (silence) is `p`.
* Sharps are written with `#` (e.g. `f#`).
* To override the default duration or octave for a single note, put the duration before the note and the octave after (e.g. `8g6` means an eighth note G in octave 6).
* A dot `.` increases the note duration by 50% (e.g., `8c.` is a dotted eighth note).

---

## Try it

Let's play a song!

### Step 1: Use the Web RTTTL Player
1. Open Kijani's web interface at `http://10.10.10.10`.
2. Locate and open the **RTTTL Player** (`rtttl.html`).
3. Click on any of the preloaded example songs (like *Mario* or *Star Wars*).
4. Click **Play on Bot**. Kijani will instantly parse the text and play the full song through Motor 1!

### Step 2: Use the Direct API
You can play any RTTTL string by calling the `/playrtttl` API. Try entering this URL in your browser:

`http://10.10.10.10/playrtttl?tune=Nokia:d=4,o=5,b=180:8e6,8d6,f#,g#,8b,8a,c#,e,8b,8a,c#,e,2a`

The classic Nokia theme will play instantly on your board!

---

## What should happen
* The RTTTL text is successfully sent to Kijani.
* The onboard synthesizer plays notes of varying pitches, speeds, and pauses sequentially.
* Motor 1 hums the melody physically.

---

## Experiment
Let's edit a song. Go to the RTTTL text editor on `rtttl.html`:
* Find the `b=180` setting. Change it to `b=300`. Click Play. The song will play extremely fast!
* Change it to `b=80`. The song will play slow and dramatic.

---

## Challenge: Build a Doorbell Sound Effect
Create a short RTTTL string that plays a standard two-tone "Ding-Dong" doorbell sound. 
*(Hint: You only need two notes, with the second note lower than the first, and a slightly longer duration. Try `DingDong:d=4,o=5,b=100:e,c` or similar!)*

---

## Troubleshooting
* **Song starts but stops immediately?** Check for typos or special characters in your RTTTL string. The string must use valid notes, and settings must be separated by colons.
* **Sound is out of tune?** Some very high octaves (octave 7 or 8) might vibrate the motor too fast to be clearly heard. Stick to octaves 5 and 6 for the best results on motor-vibration setups.

---

## Next step
Fantastic work making music! Now, we are ready to move on to high-power mechanical movement. Let's learn how to drive and control DC motors!

👉 **[Lesson 10: Connecting One Motor](../04-motors/one-motor.md)**
