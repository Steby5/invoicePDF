from fastapi import APIRouter, UploadFile
from src.utils.pdf_processor import process_pdf
from src.utils.data_formatter import format_data

router = APIRouter(prefix="/api/v1", tags=["Invoice Extraction"])

@router.post("/extract")
async def extract_invoice(file: UploadFile):
    content = await file.read()
    extracted_data = process_pdf(content)
    formatted_data = format_data(extracted_data)
    return {"data": formatted_data}
