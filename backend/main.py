from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API Mercado Livre rodando 🚀"}

# 🔹 Callback do Mercado Livre (Redirect URI)
@app.get("/callback")
def callback(code: str = None, error: str = None):
    if error:
        return {"error": error}
    if code:
        # Aqui você salva o `code` e depois troca por access_token
        return {"authorization_code": code}
    return {"message": "Nenhum código recebido"}
