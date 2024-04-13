import json
import zipfile
import os

def extract_and_format_json(zip_file_path, output_file_path):
    # Open the ZIP file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Find the JSON file in the archive
        json_file = [file for file in zip_ref.namelist() if file.endswith('.json')]

        if not json_file:
            print("No JSON file found in the ZIP archive.")
            return

        # Extract the JSON file content
        json_content = zip_ref.read(json_file[0])

        # Decode the content from bytes to string
        json_string = json_content.decode('utf-8')

        # Parse the JSON string
        json_data = json.loads(json_string)

        # Write the JSON data to a new well-structured JSON file
        with open(output_file_path, 'w') as output_file:
            json.dump(json_data, output_file, indent=4)

        print(f"Formatted JSON file saved successfully to: {output_file_path}")

# Example usage
zip_file_path = "ADOBE/pdfservices-python-sdk-samples-main/output/ExtractTextInfoFromPDF.zip"  # Adjust path to your ZIP file
output_file_path = 'ADOBE/pdfservices-python-sdk-samples-main/output/FormattedData.json'  # Adjust path for formatted JSON output

extract_and_format_json(zip_file_path, output_file_path)
