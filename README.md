**Mask to YOLOv8 Segmentation Label Converter**

This repository provides a **Python command-line tool** for converting **binary mask images** into the **YOLOv8 segmentation format**.  
The script runs **directly from the terminal** and **prompts you for the input/output folders and class ID**.

---

## Features

- **YOLOv8 Segmentation Ready** – Outputs `.txt` label files that match Ultralytics YOLOv8 segmentation format.
- **Automatic Coordinate Normalization** – Converts polygon coordinates to a normalized 0–1 range.
- **Batch Processing** – Processes all `.png` images in the input folder automatically.
- **Robust Contour Extraction** – Uses OpenCV to find and approximate object boundaries for accurate segmentation polygons.

---

## Working

1. Reads **binary mask images** from the folder you specify.
2. Applies **thresholding** to ensure masks are strictly black and white.
3. Detects **external contours** of objects in the mask.
4. Approximates polygons for each contour to reduce unnecessary points.
5. Normalizes all coordinates to YOLO’s `[0, 1]` range.
6. Saves the segmentation polygons in `.txt` files that YOLOv8 can use directly.

---

## 📜 YOLOv8 Segmentation Label Format

YOLOv8 expects segmentation annotations in the format:

<class_id> x1 y1 x2 y2 ... xn yn

Where:
- `class_id` → The integer label of the object class (e.g., `0` for one class).
- `x`, `y` → Normalized polygon vertex coordinates between 0 and 1.

Example:
0 0.123456 0.234567 0.345678 0.456789

## 🚀 Installation & Usage

### 1️⃣ Install Python and OpenCV
Make sure you have **Python 3.x** installed, then install OpenCV:

pip install opencv-python

### 2️⃣ Run the Script
Navigate to the script’s folder and run:

python convert_masks.py

### 3️⃣ Provide Inputs When Asked
The script will ask for:

Input folder path (where your .png mask images are stored)

Output folder path (where YOLO .txt label files will be saved)

Class ID (integer, e.g., 0)

Example interaction:

 Mask to YOLOv8 Segmentation Converter 
 
Enter path to the folder containing mask images: \dataset\masks
Enter path to save YOLOv8 label files: \dataset\labels
Enter class ID (integer, e.g., 0): 0
Processed: image1
Processed: image2

All masks have been converted to YOLOv8 segmentation format.


