# 🦾 AI Object Detection GUI (YOLOv8 + PyQt5)

A desktop application for real-time object detection using your webcam, powered by YOLOv8, OpenCV, PyQt5, and text-to-speech audio feedback!

---

## ✨ Features

- **Live webcam feed with object detection** (YOLOv8)
- **Confidence threshold adjustment** with clickable buttons
- **Text-to-speech audio announcements** for detected objects
- **Simple PyQt5 GUI:** Announce objects, see detection labels and confidence, quit easily
- **No cloud required:** Runs on your computer

---

## 🚀 Quick Start
Clone the repository:
  git clone https://github.com/Rivu5555/object-whisperer.git
  cd object-whisperer

Install required packages:
  pip install -r requirements.txt

Run from Jupyter Notebook
  Launch Jupyter:
    jupyter notebook
    or
    jupyter lab
    
## 🖥️ Requirements

- Python 3.8 or newer
- A working webcam
- Internet connection (for downloading YOLOv8 weights and gTTS speech generation)
- Windows, Linux, or Mac

- ## 📦 Dependencies

- PyQt5 — for GUI
- opencv-python — for image capture and processing
- ultralytics — for YOLOv8 object detection
- gTTS — for text-to-speech
- pygame — for audio playback
- numpy — for array operations

- ## 📝 How It Works

- The app starts your webcam and displays the feed.
- YOLOv8 detects objects and shows bounding boxes/labels with confidence scores.
- Detected object names and confidence thresholds are shown under the video.
- Click `Announce` to hear detected objects via TTS.
- Adjust detection confidence threshold (increase/decrease) with buttons.

- 🧰 Troubleshooting Tips
Webcam Won’t Start:
  Ensure no other apps are using the webcam.
  Restart your computer if the webcam stays black.
  Check that your webcam driver is installed and enabled.
PyQt Errors ("Could not load the Qt platform plugin"):
  Run your script with: python object_detector_gui.py
If using Anaconda: make sure you have the pyqt package installed (conda install pyqt).
"NameError: name 'null' is not defined" (when running .ipynb):
  Don’t run .ipynb notebooks with python filename.ipynb.
  Always run notebooks using Jupyter Notebook/Lab.
  You can convert .ipynb to .py first:
    jupyter nbconvert --to script Prism2.ipynb
    python Prism2.py
YOLO or torch errors:
  Make sure you’re online the first time (weights will auto-download).
  Update ultralytics with pip install --upgrade ultralytics if you get model errors.
No speech/sound:
  Make sure your speakers are on.
  Check that pygame is installed.
  Confirm audio (MP3) files can be played outside Python.
Permission Errors on Windows:
  Try running the command prompt as Administrator.
  Avoid saving files to protected folders like C:\Program Files.
Other Dependency Issues:
  Delete your virtual environment and create a new one to avoid conflicts.
  Try using python -m pip install ... to ensure correct Python version.

- ## 📚 Acknowledgements

- [YOLO](https://github.com/ultralytics/ultralytics)
- [PyQt5](https://www.riverbankcomputing.com/software/pyqt/)
- [OpenCV](https://opencv.org/)
- [gTTS](https://github.com/pndurette/gTTS)
- [pygame](https://www.pygame.org/news)

- ## 💡 Author

Protyay Saha ([protyaysahawork@gmail.com](protyaysahawork@gmail.com))
