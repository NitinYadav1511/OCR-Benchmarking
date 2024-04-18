# OCR-Benchmarking

This repository contains code and resources for benchmarking various Optical Character Recognition (OCR) engines and APIs, including Adobe, Surya, and Tesseract.

## OCR APIs

The following OCR APIs are included in this repository:

1. **Adobe**
2. **Surya**
3. **Tesseract**

## File System

The repository has the following file structure:

```
OCR-Benchmarking/
├── ADOBE/
│   ├── pdfservices-python-sdk-samples-main/
│   ├── img2pdf.py
|   └── README.md
├── IMAGES/
├── OUTPUT/
|   ├── ADOBE/
│   ├── SURYA/
|   └── TESSERACT/
├── SURYA/
|   ├── temp.py
│   └── README.md
├── TESSERACT/
|   ├── temp.py
│   └── README.md
├── README.md
└── ...
```

- `ADOBE/`: Contains the setup and source code for the Adobe API.
- `IMAGES/`: Contains the input images for testing the different OCR APIs.
- `OUTPUT/`: The output generated by the OCR APIs will be stored in this directory.
- `SURYA/`: Contains the source code for the Surya API.
- `TESSERACT/`: Contains the source code for the Tesseract API.

## Getting Started

### Prerequisites

- Python 3.6 or later
- Required Python packages (listed in `requirements.txt`)

### Installation

1. Clone the repository:

```
git clone https://github.com/NitinYadav1511/OCR-Benchmarking.git
```

2. Install the required Python packages:

```
pip install -r requirements.txt
```

### Usage

1. Add your test images to the `IMAGES` directory.
2. Run the respective scripts for each OCR API you want to test:
   - Adobe: `python ADOBE/pdfservices-python-sdk-samples-main/src/extractpdf/extract_txt_from_pdf.py`
   - Surya: `python SURYA/temp.py`
   - Tesseract: `python TESSERACT/temp.py`

The output generated by each OCR API will be stored in the `OUTPUT` directory.

## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Contributors
Nitin Yadav

## Acknowledgments

This benchmark suite utilizes the following OCR APIs and libraries:

- Adobe PDF Services API
- Surya OCR API
- Tesseract OCR Engine

Special thanks to the contributors and maintainers of these projects.
