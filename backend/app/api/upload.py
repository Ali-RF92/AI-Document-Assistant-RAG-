from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import sys
print(sys.path)
from src.pdf_loader import load_pdf

from src.text_splitter import split_text 

router = APIRouter()

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)




@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files are allowed"}

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    text = load_pdf(str(file_path))
    chunks = split_text(text)

    return {
        "filename": file.filename,
        "saved_to": str(file_path), 
        "characters": len(text),
        "preview": chunks[0],
        "chunks": len(chunks)
    }