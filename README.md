# Invoice Structuring Service

## Overview

The **Invoice Structuring Service** is a RESTful API that processes invoice PDFs and extracts key data such as invoice number, date, billing details, line items, total amount, and more. The extracted data is returned in JSON format, making it easy to integrate with other systems.

The service is built using **FastAPI** and uses **pdfplumber** for PDF parsing. It includes a simple web interface for uploading and testing invoice files.

---

## Features

- Extracts key fields like:
  - Invoice number
  - Date
  - Billing details
  - Line items
  - Total amount
- Handles multiple invoice formats.
- Provides JSON output for easy integration.
- Includes automated tests for reliability.
- Dockerized for easy deployment.

---

## Requirements

- Python 3.11 or later
- pip
- Virtual environment (recommended)
- Docker (optional, for containerized deployment)

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Steby5/invoicePDF.git
cd invoicePDF
```

### 2. Set Up a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application Locally

### Start the FastAPI Server

Run the following command to start the server on port 7000:

```bash
uvicorn src.main:app --port 7000 --reload
```

The server will be available at: [http://127.0.0.1:7000](http://127.0.0.1:7000)

### Test the API

- Visit the Swagger UI documentation: [http://127.0.0.1:7000/docs](http://127.0.0.1:7000/docs)
- Use the `/api/v1/extract` endpoint to upload a PDF and extract data.

### Use the Web Interface

A simple web interface is available at the root URL: [http://127.0.0.1:7000/](http://127.0.0.1:7000/)

---

## Testing the Application

### Run Unit Tests

To run the automated test suite:

```bash
pytest
```

### Run Tests with Coverage

```bash
pytest --cov=src
```

---

## Using Docker

### 1. Build the Docker Image

```bash
docker build -t invoice-structuring-service:latest .
```

### 2. Run the Docker Container

```bash
docker run --rm -p 7000:7000 invoice-structuring-service:latest
```

The service will be available at [http://127.0.0.1:7000](http://127.0.0.1:7000).

---

## File Structure

```plaintext
invoicePDF/
├── src/
│   ├── __init__.py
│   ├── main.py              # Entry point for FastAPI application
│   ├── routers/
│   │   ├── __init__.py
│   │   └── extract.py        # API endpoint for extracting data
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── pdf_processor.py  # Handles PDF parsing
│   │   ├── ocr.py            # Handles OCR for scanned PDFs
│   │   └── data_formatter.py # Formats extracted data into JSON
├── tests/
│   ├── __init__.py
│   ├── test_extract.py       # Unit tests for API endpoint
├── static/                   # Static files (optional)
├── templates/
│   ├── index.html            # Web interface for testing the service
├── requirements.txt          # List of dependencies
├── requirements-dev.txt      # Development dependencies
├── pytest.ini                # Pytest configuration
├── Dockerfile                # Dockerfile for containerizing the service
├── build.sh                  # Shell script to build Docker image
├── build.ps1                 # PowerShell script to build Docker image
└── README.md                 # Project documentation
```

---

## API Endpoints

### **POST** `/api/v1/extract`

#### Request
- Accepts a PDF file via `multipart/form-data`.

#### Response
- Returns a JSON object with the extracted data.

#### Example Request
```bash
curl -X POST "http://127.0.0.1:7000/api/v1/extract" \\
-H "accept: application/json" \\
-H "Content-Type: multipart/form-data" \\
-F "file=@path_to_invoice.pdf"
```

#### Example Response
```json
{
  "data": {
    "invoice_number": "INV12345",
    "date": "2024-12-11",
    "billing_details": "John Doe",
    "line_items": [
      {"description": "Widget A", "quantity": 2, "price": 20.0},
      {"description": "Widget B", "quantity": 1, "price": 10.0}
    ],
    "total_amount": 50.0
  }
}
```

---

## Limitations

- The service may not handle all invoice formats out of the box.
- Scanned PDFs require OCR, which may produce errors in extraction.
- Complex layouts with unusual formatting might need additional customization.

---

## Known Issues

- Ensure the `test_invoice.pdf` file is present in the project root when running tests.
- Missing dependencies or corrupted virtual environments may cause errors. Reinstall dependencies if needed.

---

## License

This project is licensed under the MIT License.

---

## Contact

For questions or issues, please contact the [GitHub repository](https://github.com/Steby5/invoicePDF).
