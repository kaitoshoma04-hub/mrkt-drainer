from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
import os
import json
from pathlib import Path

app = FastAPI()

# Путь к фронтенду
BASE_DIR = Path(__file__).parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

@app.get("/")
async def index():
    return FileResponse(str(FRONTEND_DIR / "index.html"))

@app.get("/static/{path:path}")
async def serve_static(path: str):
    file_path = FRONTEND_DIR / path
    if file_path.exists():
        return FileResponse(str(file_path))
    return JSONResponse({"error": "Not found"}, status_code=404)

@app.post("/api/request-phone")
async def request_phone(request: Request):
    try:
        data = await request.json()
        return {"status": "success", "message": "Phone received", "data": data}
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": str(e)}
        )

@app.post("/api/verify-code")
async def verify_code(request: Request):
    try:
        data = await request.json()
        return {"status": "success", "message": "Code verified", "data": data}
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": str(e)}
        )

@app.get("/health")
async def health():
    return {"status": "ok", "platform": "vercel"}

# Если путь не найден — отдаём индекс
@app.get("/{path:path}")
async def catch_all(path: str):
    return FileResponse(str(FRONTEND_DIR / "index.html"))
