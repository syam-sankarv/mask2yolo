import cv2
import os
import glob

print("\n Mask to YOLOv8 Segmentation Converter ")
input_folder = input("Enter path to the folder containing mask images: ").strip()
output_folder = input("Enter path to save YOLOv8 label files: ").strip()

while True:
    try:
        class_id = int(input("Enter class ID (integer, e.g., 0): ").strip())
        break
    except ValueError:
        print(" Invalid input. Please enter an integer.")

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Get list of images
image_paths = glob.glob(os.path.join(input_folder, "*.png"))

if not image_paths:
    print(f" No PNG images found in '{input_folder}'. Exiting...")
    exit()

for img_path in image_paths:
    # Read image in grayscale
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f" Warning: Could not read image {img_path}")
        continue

    height, width = img.shape[:2]

    # Threshold (ensure binary)
    _, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    label_lines = []

    for contour in contours:
        # Approximate polygon shape
        epsilon = 0.01 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Flatten and normalize points
        points = approx.reshape(-1, 2)
        norm_points = [(x / width, y / height) for x, y in points]

        # Flatten into a single line
        polygon_str = ' '.join([f"{x:.6f} {y:.6f}" for x, y in norm_points])
        line = f"{class_id} {polygon_str}"
        label_lines.append(line)

    # Write to corresponding .txt file
    base_name = os.path.splitext(os.path.basename(img_path))[0]
    output_path = os.path.join(output_folder, f"{base_name}.txt")

    with open(output_path, 'w') as f:
        for line in label_lines:
            f.write(line + "\n")

    print(f" Processed: {base_name}")

print("\n All masks have been converted to YOLOv8 segmentation format.")
