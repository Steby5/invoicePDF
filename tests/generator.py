from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_sample_invoice(filepath):
    c = canvas.Canvas(filepath, pagesize=letter)
    c.drawString(100, 750, "Invoice No: INV12345")
    c.drawString(100, 730, "Date: 2024-12-11")
    c.drawString(100, 710, "Billing To: John Doe")
    c.drawString(100, 690, "Item: Widget A  Qty: 2  Price: $20.00")
    c.drawString(100, 670, "Item: Widget B  Qty: 1  Price: $10.00")
    c.drawString(100, 650, "Total: $50.00")
    c.save()

generate_sample_invoice("test_invoice.pdf")
