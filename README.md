# YOLO Object Detection Demo (Ultralytics YOLOv8)

This is a **simple, educational demo** of object detection using the public
[Ultralytics YOLO](https://docs.ultralytics.com) Python package.

- ✅ Uses only **public, off-the-shelf YOLO models**
- ✅ No proprietary code
- ✅ Easy to run locally in a virtual environment
- ✅ Great as a portfolio example for AI/ML + Computer Vision

---

## 🧱 Project Structure

```text
yolo-object-detection-demo/
├── README.md
├── requirements.txt
├── detect.py
├── .gitignore
└── data/
    └── bus.jpg
```

## 🚀 How to Run

### 1. Create and activate a virtual environment

```
python3 -m venv .venv
source .venv/bin/activate      # Linux / macOS
# .venv\Scripts\activate       # Windows (PowerShell / CMD)
```

### 2. Install dependencies

```
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Make sure you have a test image

This repo includes a sample image:
```
data/bus.jpg
```
If you need to (re)download it:
```
mkdir -p data
wget https://ultralytics.com/images/bus.jpg -O data/bus.jpg
```

### 4. Run object detection

```
python detect.py --source data/bus.jpg
```
The predictions (with bounding boxes) will be saved under a directory like:
```
runs/detect/predict/
```
Open the saved image to view the detections.

## 📝 Notes

- This project is purely educational.
- It uses only the public `ultralytics` Python package and public YOLOv8 models.
- No employer or proprietary code is used in this repository.
