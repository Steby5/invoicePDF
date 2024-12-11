from pytesseract import image_to_string
from PIL import Image
import io

def perform_ocr(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    return image_to_string(image)
