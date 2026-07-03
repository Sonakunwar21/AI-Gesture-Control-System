# ✋ AI Gesture Volume & Brightness Control System

## 📌 About the System

The AI Gesture Volume & Brightness Control System is a real-time Computer Vision application that enables users to control their Windows system volume and screen brightness using simple hand gestures. By tracking the distance between the thumb and index finger through a webcam, the system provides a touch-free and intuitive way to interact with the computer.

Built using MediaPipe Hand Landmarker and OpenCV, the project demonstrates practical applications of hand tracking, gesture recognition, and human-computer interaction.

---
## 🎯 What This System Can Do

- Detects hand landmarks in real time through a webcam.
- Measures the distance between the thumb and index finger.
- Maps finger distance to Windows system volume.
- Maps finger distance to screen brightness.
- Provides smooth and responsive gesture-based interaction.
- Allows users to switch between Volume and Brightness control modes.

---
## ✨ Key Features

- 🔊 Control Windows system volume using hand gestures
- 💡 Adjust screen brightness in real time
- ✋ Real-time hand landmark detection
- 📏 Thumb–Index finger distance measurement
- 🔄 Switch between Volume and Brightness modes using keyboard shortcuts
- 🎥 Live webcam visualization with detected hand landmarks
- ⚡ Smooth real-time gesture recognition
- 🖥️ User-friendly interface with live feedback

---

## 🛠️ Tech Stack

**Programming Language**
- Python

**Computer Vision**
- OpenCV
- MediaPipe Hand Landmarker

**Libraries**
- NumPy
- PyCAW
- Screen Brightness Control
- Comtypes

**Development Tools**
- VS Code
- Anaconda
- Git & GitHub

---

## 📂 Project Structure

```text
GestureControl/
│
├── .gitignore                 # Ignore unnecessary files
├── README.md                  # Project documentation
├── requirements.txt           # Required Python packages
│
├── hand_detect.py             # Main application for gesture detection
├── volume_control.py          # Controls Windows system volume
├── brightness_control.py      # Controls screen brightness
│
└── models/
    └── hand_landmarker.task   # MediaPipe Hand Landmarker model
---

## 🚀 Future Improvements

- 🎨 Air Canvas for gesture-based drawing
- 🖱️ Virtual Mouse Control
- 📸 Screenshot Capture using gestures
- ✋ Gesture-based mode switching
- 🌐 Interactive desktop GUI
- ⚡ Performance optimization for smoother tracking
- 🤖 Additional custom gesture recognition

---

## 👨‍💻 Author

**Sona Kunwar**

Data Scientist | Computer Vision Enthusiast

If you found this project useful, consider giving it a ⭐ on GitHub.
