import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from src.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_extract_endpoint():
    with open("test_invoice.pdf", "rb") as file:
        response = client.post("/api/v1/extract", files={"file": file})
    assert response.status_code == 200
    assert "data" in response.json()

def test_invalid_file():
    response = client.post("/api/v1/extract", files={"file": ("test.txt", b"Invalid content")})
    assert response.status_code == 400

def test_missing_file():
    response = client.post("/api/v1/extract", files={})
    assert response.status_code == 422  # Unprocessable Entity

def test_partial_pdf():
    with open("partial_invoice.pdf", "rb") as file:
        response = client.post("/api/v1/extract", files={"file": file})
    assert response.status_code == 200
    assert "data" in response.json()
