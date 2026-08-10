from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
import httpx
import os

app = FastAPI()

# Твой локальный бот (или VPS)
LOCAL_BOT_URL = "http://127.0.0.1:8080"  # или IP с открытым портом

# Отдаём фронтенд
FRONTEND_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")

@app.get("/")
async def index():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

@app.get("/static/{path:path}")
async def serve_static(path: str):
    file_path = os.path.join(FRONTEND_DIR, path)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return JSONResponse({"error": "Not found"}, status_code=404)

@app.api_route("/api/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy_to_local_bot(path: str, request: Request):
    """Проксируем все API запросы к локальному боту"""
    try:
        body = await request.body()
        headers = dict(request.headers)
        
        # Убираем host, чтобы не было конфликтов
        headers.pop("host", None)
        
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.request(
                method=request.method,
                url=f"{LOCAL_BOT_URL}/api/{path}",
                content=body,
                headers=headers,
            )
            
        return JSONResponse(
            content=response.json(),
            status_code=response.status_code
        )
    except httpx.ConnectError:
        return JSONResponse(
            status_code=503,
            content={"status": "error", "message": "Local bot is not running"}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": str(e)}
        )

@app.get("/health")
async def health():
    return {"status": "ok", "vercel": True}
