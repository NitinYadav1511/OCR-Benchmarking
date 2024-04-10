import os
import json
from PIL import Image, ImageDraw
import pytesseract

# Function to perform OCR on a single image using pytesseract
def perform_ocr(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return image, text

# Function to create bounding boxes around text lines in an image
def create_bounding_boxes(image, text):
    boxes = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
    draw = ImageDraw.Draw(image)
    bounding_boxes = []
    for i in range(len(boxes['text'])):
        if int(boxes['conf'][i]) > 0:
            (x, y, w, h) = (boxes['left'][i], boxes['top'][i], boxes['width'][i], boxes['height'][i])
            draw.rectangle([x, y, x + w, y + h], outline="red", width=2)
            bounding_boxes.append([x, y, x + w, y + h, boxes['text'][i]])  # Save bounding box coordinates and text
    return image, bounding_boxes

# Directory containing images
images_directory = 'IMAGES'

# Output directory to save JSON files and images with bounding boxes
output_directory = 'OUTPUT/TESSERACT'
os.makedirs(output_directory, exist_ok=True)

# Process each image in the directory
for filename in os.listdir(images_directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(images_directory, filename)

        # Perform OCR on the image
        image, text = perform_ocr(image_path)

        # Create bounding boxes around text lines
        image_with_boxes, bounding_boxes = create_bounding_boxes(image, text)

        # Save image with bounding boxes
        output_image_path = os.path.join(output_directory, filename)
        image_with_boxes.save(output_image_path)
        print(f"Processed: {filename} -> Image with bounding boxes saved to {output_image_path}")

        # Save bounding box coordinates to JSON file
        json_filename = os.path.splitext(filename)[0] + ".json"
        json_filepath = os.path.join(output_directory, json_filename)
        with open(json_filepath, 'w') as json_file:
            json.dump(bounding_boxes, json_file)
        print(f"Bounding box coordinates saved to {json_filepath}")
