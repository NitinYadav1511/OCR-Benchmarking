import os
import json
from PIL import Image, ImageDraw
from surya.ocr import run_ocr
from surya.model.detection.segformer import load_model as load_det_model, load_processor as load_det_processor
from surya.model.recognition.model import load_model as load_rec_model
from surya.model.recognition.processor import load_processor as load_rec_processor

# Function to perform OCR on a single image
def perform_ocr(image_path, det_model, det_processor, rec_model, rec_processor, languages):
    image = Image.open(image_path)
    predictions = run_ocr([image], [languages], det_model, det_processor, rec_model, rec_processor)
    return image, predictions[0]  # Return image and predictions for the single image

# Directory containing images
images_directory = 'IMAGES'

# Output directory to save JSON files
output_directory = 'OUTPUT/SURYA'

# Ensure output directory exists
os.makedirs(output_directory, exist_ok=True)
os.makedirs(os.path.join(output_directory, 'IMAGES'), exist_ok=True)

# Languages for OCR
languages = ["hi", "kn", "en"]  # Replace with the languages you need

# Load detection and recognition models and processors
det_model = load_det_model()
det_processor = load_det_processor()
rec_model = load_rec_model()
rec_processor = load_rec_processor()

# Process each image in the directory
for filename in os.listdir(images_directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(images_directory, filename)
        
        # Perform OCR on the image
        image, predictions = perform_ocr(image_path, det_model, det_processor, rec_model, rec_processor, languages)
        
        # Extract bounding box coordinates
        bounding_boxes = [text_line.bbox for text_line in predictions.text_lines]

        # Draw bounding boxes on the image
        draw = ImageDraw.Draw(image)
        for bbox in bounding_boxes:
            draw.rectangle(bbox, outline="red")

        # Save image with bounding boxes
        output_image_path = os.path.join(output_directory, 'IMAGES', filename)
        image.save(output_image_path)

        print(f"Processed: {filename} -> Image with bounding boxes saved to {output_image_path}")

        # Create JSON filename based on image filename
        json_filename = os.path.splitext(filename)[0] + ".json"
        json_filepath = os.path.join(output_directory, json_filename)

        # Save bounding box coordinates to JSON file
        with open(json_filepath, 'w') as json_file:
            json.dump(bounding_boxes, json_file)

        print(f"Bounding box coordinates saved to {json_filepath}")
