# CS2 Input Lag Analysis

My attempt at comparing CS:GO and CS2 input lag.

## Setup

- Monitor: BenQ ZOWIE XL2540K @ 240 Hz (DyAc off)
- OS: Windows 10 Enterprise LTSC 2021 (21H2)
- CPU: Intel i7 8700k @ 4.8 GHz
- GPU: NVIDIA GTX 1080 Ti
- RAM: Corsair VENGEANCE DDR4 (2x8GB) @ 3200 MHz

## Notes

- All other monitors are disabled
- Everything in the NVIDIA control panel is set to default (except for the frame limiter that I'll be using)
- Lowest possible graphics settings in both games at 1080p
- Resolution scaling in CS2 is disabled
- No browser/Discord/Spotify were running in the background

## Apparatus

It's just an Arduino Pro Micro that acts as a mouse with a photoresistor soldered onto it. 
The photoresistor is enclosed to minimize other lights affecting the measurements.

![circuit](images/circuit.png)

## Logic ([code](missing))

### Calibrate

Calibration happens every 250 samples.

1. Aim at a spot that's dark
1. Read out and average measurements for 1 second (reduce noise) 
1. Aim at a spot that's bright
1. Read out and average measurements for 1 second (reduce noise)
1. The baseline for dark is at 5% between dark and bright measurements
1. The baseline for bright is at 20% between dark and bright measurements

### Measure one sample

1. Aim at a spot that's dark
1. Wait till the measurement goes below the baseline for dark
1. Delay for a random amount of time
1. Start measuring time
1. Aim at a spot that's bright
1. Wait till the measurement is above the baseline for bright
1. Stop measuring time

## Graphs

![csgo_inferno_160fps](graphs/csgo_inferno_160fps.png)
![cs2_inferno_lowlatency-disabled_160fps](graphs/cs2_inferno_lowlatency-disabled_160fps.png)
![cs2_inferno_lowlatency-enabled_160fps](graphs/cs2_inferno_lowlatency-enabled_160fps.png)
![cs2_inferno_lowlatency-boost_160fps](graphs/cs2_inferno_lowlatency-boost_160fps.png)

---
---
---

![csgo_inferno_240fps](graphs/csgo_inferno_240fps.png)
![cs2_inferno_lowlatency-disabled_240fps](graphs/cs2_inferno_lowlatency-disabled_240fps.png)
![cs2_inferno_lowlatency-enabled_240fps](graphs/cs2_inferno_lowlatency-enabled_240fps.png)
![cs2_inferno_lowlatency-boost_240fps](graphs/cs2_inferno_lowlatency-boost_240fps.png)

---
---
---

![csgo_inferno_300fps](graphs/csgo_inferno_300fps.png)
![cs2_inferno_lowlatency-disabled_300fps](graphs/cs2_inferno_lowlatency-disabled_300fps.png)
![cs2_inferno_lowlatency-enabled_300fps](graphs/cs2_inferno_lowlatency-enabled_300fps.png)
![cs2_inferno_lowlatency-boost_300fps](graphs/cs2_inferno_lowlatency-boost_300fps.png)

---
---
---

CS:GO unlocked fps was at 550fps.

CS2 unlocked fps was pretty much glued to 400fps.

![csgo_inferno_400fps](graphs/csgo_inferno_400fps.png)
![csgo_inferno_unlocked-fps](graphs/csgo_inferno_unlocked-fps.png)
![cs2_inferno_lowlatency-disabled_unlocked-fps](graphs/cs2_inferno_lowlatency-disabled_unlocked-fps.png)
![cs2_inferno_lowlatency-enabled_unlocked-fps](graphs/cs2_inferno_lowlatency-enabled_unlocked-fps.png)
![cs2_inferno_lowlatency-boost_unlocked-fps](graphs/cs2_inferno_lowlatency-boost_unlocked-fps.png)

---
---
---
---
---
---

![csgo_emptymap_160fps](graphs/csgo_emptymap_160fps.png)
![cs2_emptymap_lowlatency-disabled_160fps](graphs/cs2_emptymap_lowlatency-disabled_160fps.png)
![cs2_emptymap_lowlatency-enabled_160fps](graphs/cs2_emptymap_lowlatency-enabled_160fps.png)
![cs2_emptymap_lowlatency-boost_160fps](graphs/cs2_emptymap_lowlatency-boost_160fps.png)

---
---
---

![csgo_emptymap_240fps](graphs/csgo_emptymap_240fps.png)
![cs2_emptymap_lowlatency-disabled_240fps](graphs/cs2_emptymap_lowlatency-disabled_240fps.png)
![cs2_emptymap_lowlatency-enabled_240fps](graphs/cs2_emptymap_lowlatency-enabled_240fps.png)
![cs2_emptymap_lowlatency-boost_240fps](graphs/cs2_emptymap_lowlatency-boost_240fps.png)

---
---
---

![csgo_emptymap_300fps](graphs/csgo_emptymap_300fps.png)
![cs2_emptymap_lowlatency-disabled_300fps](graphs/cs2_emptymap_lowlatency-disabled_300fps.png)
![cs2_emptymap_lowlatency-enabled_300fps](graphs/cs2_emptymap_lowlatency-enabled_300fps.png)
![cs2_emptymap_lowlatency-boost_300fps](graphs/cs2_emptymap_lowlatency-boost_300fps.png)

---
---
---

![csgo_emptymap_480fps](graphs/csgo_emptymap_480fps.png)
![cs2_emptymap_lowlatency-disabled_480fps](graphs/cs2_emptymap_lowlatency-disabled_480fps.png)
![cs2_emptymap_lowlatency-enabled_480fps](graphs/cs2_emptymap_lowlatency-enabled_480fps.png)
![cs2_emptymap_lowlatency-boost_480fps](graphs/cs2_emptymap_lowlatency-boost_480fps.png)

---
---
---

![csgo_emptymap_720fps](graphs/csgo_emptymap_720fps.png)
![cs2_emptymap_lowlatency-disabled_720fps](graphs/cs2_emptymap_lowlatency-disabled_720fps.png)
![cs2_emptymap_lowlatency-enabled_720fps](graphs/cs2_emptymap_lowlatency-enabled_720fps.png)
![cs2_emptymap_lowlatency-boost_720fps](graphs/cs2_emptymap_lowlatency-boost_720fps.png)

## Tear Free Graphs

### GSYNC

![csgo_emptymap_236fps_gsync](graphs/csgo_emptymap_236fps_gsync.png)
![cs2_emptymap_lowlatency-disabled_236fps_gsync](graphs/cs2_emptymap_lowlatency-disabled_236fps_gsync.png)
![cs2_emptymap_lowlatency-enabled_236fps_gsync](graphs/cs2_emptymap_lowlatency-enabled_236fps_gsync.png)
![cs2_emptymap_lowlatency-boost_236fps_gsync](graphs/cs2_emptymap_lowlatency-boost_236fps_gsync.png)

---
---
---

![csgo_inferno_236fps_gsync](graphs/csgo_inferno_236fps_gsync.png)
![cs2_inferno_lowlatency-enabled_236fps_gsync](graphs/cs2_inferno_lowlatency-enabled_236fps_gsync.png)
![cs2_inferno_lowlatency-disabled_236fps_gsync](graphs/cs2_inferno_lowlatency-disabled_236fps_gsync.png)
![cs2_inferno_lowlatency-boost_236fps_gsync](graphs/cs2_inferno_lowlatency-boost_236fps_gsync.png)

### VSYNC

![csgo_inferno_vsync-doublebuffer](graphs/csgo_inferno_vsync-doublebuffer.png)
![csgo_inferno_vsync-triplebuffer](graphs/csgo_inferno_vsync-triplebuffer.png)
![cs2_inferno_lowlatency-enabled_vsync](graphs/cs2_inferno_lowlatency-enabled_vsync.png)

### Fullscreen Windowed

![csgo_inferno_300fps_windowed-fullscreen](graphs/csgo_inferno_300fps_windowed-fullscreen.png)

WARNING: CS2 Fullscreen Windowed is not actually tear free!
![cs2_inferno_lowlatency-enabled_300fps_fullscreen-windowed](graphs/cs2_inferno_lowlatency-enabled_300fps_fullscreen-windowed.png)

---
---
---

![samuel](images/samuel.png)
