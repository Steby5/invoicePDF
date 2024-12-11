import re

def format_data(extracted_data):
    formatted = {
        "invoice_number": None,
        "date": None,
        "billing_details": None,
        "line_items": [],
        "total_amount": None,
    }
    for line in extracted_data:
        if "Invoice" in line:
            formatted["invoice_number"] = re.search(r"Invoice\s+No:\s+(\S+)", line).group(1)
        # Add more parsing rules here
    return formatted
