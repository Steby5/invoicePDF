import pdfplumber
from io import BytesIO
from pytesseract import image_to_string
from PIL import Image
import io

def extract_text_from_pdf(pdf_content):
    """Extract text from PDF using pdfplumber."""
    pdf_file = BytesIO(pdf_content)
    extracted_data = []
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                extracted_data.append(text)
    return "\n".join(extracted_data)

def extract_text_from_image(image_bytes):
    """Extract text from scanned images using OCR (pytesseract)."""
    image = Image.open(io.BytesIO(image_bytes))
    return image_to_string(image)

def process_pdf(pdf_content):
    """Hybrid text extraction: PDFs first, then OCR for images."""
    text = extract_text_from_pdf(pdf_content)
    if not text.strip():
        text = extract_text_from_image(pdf_content)  # Fallback to OCR
    return text
