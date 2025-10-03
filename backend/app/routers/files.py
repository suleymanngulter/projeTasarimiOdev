from fastapi import APIRouter, UploadFile, File
from typing import Dict

router = APIRouter(prefix="/files", tags=["files"])

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)) -> Dict:
    # Şimdilik sadece meta döndürelim (ileride kaydedip işleme alacağız)
    if file.content_type != "application/pdf":
        return {"ok": False, "message": "Lütfen PDF yükleyin."}
    content = await file.read()
    size_kb = round(len(content)/1024, 2)
    return {"ok": True, "filename": file.filename, "size_kb": size_kb}
