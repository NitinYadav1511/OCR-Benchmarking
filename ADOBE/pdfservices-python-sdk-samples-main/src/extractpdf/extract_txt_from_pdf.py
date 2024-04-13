import logging
import os
import shutil
import zipfile
import json

from adobe.pdfservices.operation.auth.credentials import Credentials
from adobe.pdfservices.operation.exception.exceptions import ServiceApiException, ServiceUsageException, SdkException
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_pdf_options import ExtractPDFOptions
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_element_type import ExtractElementType
from adobe.pdfservices.operation.execution_context import ExecutionContext
from adobe.pdfservices.operation.io.file_ref import FileRef
from adobe.pdfservices.operation.pdfops.extract_pdf_operation import ExtractPDFOperation

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

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

try:
    # get base path.
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # Input and output directories
    input_directory = os.path.join(base_path, "resources")
    output_directory = "OUTPUT\ADOBE"

    # Create output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Initial setup, create credentials instance.
    credentials = Credentials.service_principal_credentials_builder(). \
        with_client_id("YOUR ADOBE API CLIENT ID"). \
        with_client_secret("YOUR ADOBE API CLIENT SECRET"). \
        build()

    # Create an ExecutionContext using credentials.
    execution_context = ExecutionContext.create(credentials)

    # Iterate through each PDF file in the input directory
    for pdf_file in os.listdir(input_directory):
        if pdf_file.endswith(".pdf"):
            pdf_file_path = os.path.join(input_directory, pdf_file)

            print("FILE:", pdf_file, "is being processed")

            # Create a new operation instance for each PDF file
            extract_pdf_operation = ExtractPDFOperation.create_new()

            # Set operation input from the current PDF file.
            source = FileRef.create_from_local_file(pdf_file_path)
            extract_pdf_operation.set_input(source)

            # Build ExtractPDF options and set them into the operation
            extract_pdf_options: ExtractPDFOptions = ExtractPDFOptions.builder() \
                .with_element_to_extract(ExtractElementType.TEXT) \
                .build()
            extract_pdf_operation.set_options(extract_pdf_options)

            # Execute the operation.
            result: FileRef = extract_pdf_operation.execute(execution_context)

            # Get the temporary file path.
            temp_file_path = result._file_path

            # Define the target file path in the output directory.
            output_file_name = os.path.splitext(pdf_file)[0] + "_ExtractedText.zip"
            output_file_path = os.path.join(output_directory, output_file_name)

            # Copy the file to the output directory.
            shutil.copy(temp_file_path, output_file_path)

            # Now, extract and format the JSON file from the ZIP
            formatted_json_file_path = os.path.join(output_directory, os.path.splitext(pdf_file)[0] + "_FormattedData.json")
            extract_and_format_json(output_file_path, formatted_json_file_path)

except (ServiceApiException, ServiceUsageException, SdkException) as e:
    logging.exception("Exception encountered while executing operation")
