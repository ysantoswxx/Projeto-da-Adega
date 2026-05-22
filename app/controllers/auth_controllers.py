from fastapi import APIRouter, Request, Depends,Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import  Jinja2Templates
from sqlalchemy.orm import Session


from app.database import get_db

from
