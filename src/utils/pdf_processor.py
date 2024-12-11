import pdfplumber
from io import BytesIO

def process_pdf(pdf_content):
    # Wrap the bytes object in a BytesIO file-like object
    pdf_file = BytesIO(pdf_content)
    with pdfplumber.open(pdf_file) as pdf:
        extracted_data = []
        for page in pdf.pages:
            extracted_data.append(page.extract_text())
    return extracted_data
