from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from app.auth import get_usuario_opcional

app = FastAPI(title=" Adega Premium")

@app.get("/")
def tela_inicial(
    request: Request,
    usurio
)