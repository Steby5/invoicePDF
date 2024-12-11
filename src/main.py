from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from src.routers import extract

app = FastAPI(title="Invoice Structuring Service")

# Include API router
app.include_router(extract.router)

# Serve static files (if needed)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve the homepage
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("templates/index.html") as f:
        return HTMLResponse(content=f.read())
