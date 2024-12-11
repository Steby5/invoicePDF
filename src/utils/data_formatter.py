import re
from transformers import pipeline

# Load an NLP model (pre-trained or fine-tuned)
nlp = pipeline("ner", model="dslim/bert-base-NER")

def format_data(text):
    """Format extracted text into structured JSON."""
    formatted = {
        "invoice_number": None,
        "date": None,
        "billing_details": None,
        "line_items": [],
        "total_amount": None,
    }

    # Extract fields using regex
    invoice_number = re.search(r"Invoice No:\s*(\S+)", text)
    if invoice_number:
        formatted["invoice_number"] = invoice_number.group(1)

    date = re.search(r"Date:\s*([\d-]+)", text)
    if date:
        formatted["date"] = date.group(1)

    billing_details = re.search(r"Billing To:\s*(.+)", text)
    if billing_details:
        formatted["billing_details"] = billing_details.group(1)

    # Use NLP to find named entities like money amounts
    entities = nlp(text)
    for entity in entities:
        if entity["entity"] == "MONEY":
            if not formatted["total_amount"]:
                formatted["total_amount"] = entity["word"]

    # Extract line items using regex
    line_items = re.findall(r"Item:\s*(.+)\s*Qty:\s*(\d+)\s*Price:\s*\$(\d+\.\d+)", text)
    for item in line_items:
        formatted["line_items"].append({
            "description": item[0].strip(),
            "quantity": int(item[1]),
            "price": float(item[2]),
        })

    return formatted
