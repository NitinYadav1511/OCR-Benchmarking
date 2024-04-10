import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image

def image_to_pdf(image_path, output_pdf_folder):
    # Open the image file
    img = Image.open(image_path)
    
    # Get the name of the image file (without extension)
    image_name = os.path.splitext(os.path.basename(image_path))[0]
    
    # Create the output PDF path
    output_pdf_path = os.path.join(output_pdf_folder, f"{image_name}.pdf")
    
    # Create a new PDF
    c = canvas.Canvas(output_pdf_path, pagesize=img.size)
    
    # Draw the image on the PDF
    c.drawImage(image_path, 0, 0)
    
    # Save the PDF
    c.save()

# Folder containing the images
image_folder = 'IMAGES'

# Output PDF folder
output_pdf_folder = 'ADOBE/pdfs'

# Create the output PDF folder if it doesn't exist
os.makedirs(output_pdf_folder, exist_ok=True)

# Iterate over each image file in the folder and convert to PDF
for filename in os.listdir(image_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        image_path = os.path.join(image_folder, filename)
        image_to_pdf(image_path, output_pdf_folder)
print("Images converted successfully!")