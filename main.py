import os
import uvicorn
import json
import shutil
from datetime import datetime
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

import logic_lock
import admin_sovereign
import handshake

app = FastAPI(title="CYBEROUS_SEC_SOVEREIGN_ENGINE_v1.0")

SYSTEM_ACTIVE = True
app.mount("/static", StaticFiles(directory="."), name="static")

def archive_vault():
    if not os.path.exists("backups"):
        os.makedirs("backups")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    if os.path.exists("harvest_vault.log"):
        shutil.copy("harvest_vault.log", f"backups/vault_backup_{timestamp}.log")

@app.get("/", response_class=HTMLResponse)
async def get_index():
    if not SYSTEM_ACTIVE:
        return HTMLResponse(content="<body style='background:#000;color:#555;display:flex;justify-content:center;align-items:center;height:100vh;font-family:monospace;'>[SYSTEM_OFFLINE_BY_OPERATOR]</body>")
    try:
        with open("index.html", "r") as f:
            return f.read()
    except FileNotFoundError:
        return HTMLResponse(content="INDEX_MISSING", status_code=500)

@app.get("/admin", response_class=HTMLResponse)
async def serve_admin(request: Request):
    key = request.query_params.get("key")
    if key == admin_sovereign.MASTER_KEY:
        with open("admin.html", "r") as f:
            return f.read()
    logic_lock.harvest_metadata("UNAUTHORIZED_ADMIN_ACCESS", "CRITICAL")
    return HTMLResponse(content="<h1>404 Not Found</h1>", status_code=404)

@app.get("/api/harvest")
async def get_harvest_data(key: str):
    if key != admin_sovereign.MASTER_KEY:
        return []
    logs = []
    if os.path.exists("harvest_vault.log"):
        with open("harvest_vault.log", "r") as f:
            for line in f:
                if line.strip(): logs.append(json.loads(line))
    return logs

@app.post("/api/toggle-system")
async def toggle_sys(request: Request):
    global SYSTEM_ACTIVE
    data = await request.json()
    if data.get("key") == admin_sovereign.MASTER_KEY:
        SYSTEM_ACTIVE = not SYSTEM_ACTIVE
        archive_vault()
        return {"status": "SUCCESS", "new_state": "ONLINE" if SYSTEM_ACTIVE else "OFFLINE"}
    return JSONResponse(content={"error": "403"}, status_code=403)

@app.post("/api/terminal")
async def handle_input(request: Request):
    if not SYSTEM_ACTIVE:
        return {"status": "LOCKED", "message": "SYSTEM OFFLINE."}
    payload = await request.json()
    cmd = payload.get("input", "").strip()
    if admin_sovereign.verify_operator(cmd):
        return {"status": "MASTER", "message": "OPERATOR VERIFIED."}
    result = logic_lock.analyze_vector(cmd)
    if result.get("status") == "LOCKED":
        archive_vault()
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)