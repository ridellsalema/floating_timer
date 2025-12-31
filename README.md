# Floating Timer (CustomTkinter)

A minimal, always-on-top floating stopwatch for Windows, built with Python and CustomTkinter.

This is a small side project I built in my free time.

A clean, distraction-free timer for studying, coding, and screen recording.

---

## Features
Stopwatch in HH:MM:SS format
Borderless floating window
Always on top
Draggable
resume (Space)
Restart (Backspace)
Exit (Esc)

---

## Screenshot
![alt text](assets/preview.png)

---

## Requirements
- Python 3.9+
- `customtkinter`

Install dependencies:
```bash
pip install customtkinter
```

## Building Execuatble(Windows)
```bash
pip install pyinstaller
pyinstaller --onefile --noconsole floating_timer_ctk.py
```
