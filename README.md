# Hand Gesture-Based Zoom with OpenCV

This project demonstrates an interactive zoom effect controlled by hand gestures using OpenCV and `cvzone.HandTrackingModule`. Users can resize an image in real-time by moving their hands in front of a webcam. The zoom gesture is detected when both hands are visible, and specific finger combinations are used.

---

## Features
- **Real-Time Hand Detection**: Detects and tracks hand movements using a webcam.
- **Dynamic Scaling**: Zooms in and out of an image based on the distance between index fingers.
- **Responsive Placement**: The image dynamically updates its size and position to follow hand gestures.
- **Cross-Platform**: Works on Windows, macOS, and Linux systems with a compatible webcam.

---

## How It Works
1. The program uses OpenCV to capture live video from the webcam.
2. The `cvzone.HandTrackingModule` identifies hands and tracks finger positions.
3. When two hands are detected with the index and middle fingers extended on both hands, the distance between their index fingertips is measured.
4. The change in distance is used to scale the size of the displayed image dynamically.
5. The scaled image is centered between the hands.

---

## Requirements
- Python 3.x
- OpenCV
- cvzone

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/opencv-zoom-gesture.git
