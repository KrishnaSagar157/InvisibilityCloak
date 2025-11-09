# 🧥 Invisibility Cloak using OpenCV

This project recreates the famous **"Invisibility Cloak"** effect from *Harry Potter* using **Python** and **OpenCV**.  
It detects a red-colored cloth in the video feed and replaces it with the background — making the cloth (and the person behind it) appear invisible in real time! ✨


## 🚀 Features
✅ Real-time webcam video processing  
✅ Manual background capture (press **`b`**)  
✅ Adjustable HSV color range (easy to modify)  
✅ Smooth invisibility effect using morphological operations  
✅ Works on any system with a webcam  


## 🧠 How It Works
1. Capture a **background image** (without you in the frame).  
2. Detect the **red cloak** in each frame using HSV color space.  
3. Create a mask that isolates the cloak.  
4. Replace the cloak area with the saved background image.  
5. Combine both to produce the invisibility illusion!  


## 🧰 Requirements
Install the dependencies before running:
```bash
pip install opencv-python numpy
