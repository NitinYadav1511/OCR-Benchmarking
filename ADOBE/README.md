# Adobe PDF Extract API

This project demonstrates how to use the Adobe PDF Services API for OCR (Optical Character Recognition) to extract text from PDF files or images using Python.

## Prerequisites

1. Python 3.6 or later
2. Adobe API Credentials

### Obtaining Adobe API Credentials

1. Visit the [Adobe PDF Services API Integration Creation App](https://documentservices.adobe.com/dc-integration-creation-app-cdn/main.html?api=pdf-services-api) to get your API credentials.
2. Download the "PDFServicesSDK-Python (Extract, Auto-Tag)Samples.zip" file.
3. Extract the downloaded zip file and locate the JSON file containing the API credentials.

### Setting Environment Variables

#### Windows

```
set PDF_SERVICES_CLIENT_ID=<YOUR CLIENT ID>
set PDF_SERVICES_CLIENT_SECRET=<YOUR CLIENT SECRET>
```

#### MacOS/Linux

```
export PDF_SERVICES_CLIENT_ID=<YOUR CLIENT ID>
export PDF_SERVICES_CLIENT_SECRET=<YOUR CLIENT SECRET>
```

## Installation

1. Install the required Python packages by running:

```
pip install -r pdfservices-python-sdk-samples-main/requirements.txt
```

2. Verify the download authenticity by running:

```
pip hash <download_dir>/pdfservices-sdk-2.3.1.tar.gz
```

The output should match the following hash code:

```
08d1c40995658e380c7e5d2fec4cebfbfc22b246582719c5451ae708a28b6a09
```

## Usage

1. Run `img2pdf.py` to convert input images to a PDF file:

```
python img2pdf.py
```

2. Run `extract_txt_from_pdf.py` (located in the `extractpdf` folder under `src`) to perform OCR on the PDF file and extract the text:

```
python src/extractpdf/extract_txt_from_pdf.py
```

## Documentation

For more information on using the Adobe PDF Extract API, refer to the [Adobe PDF Extract API Documentation](https://developer.adobe.com/document-services/apis/pdf-extract/).


