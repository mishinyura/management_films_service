from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_session
from app.schemas.schemas import UserCreate, UserOut
from app.services import auth
from fastapi import Request

templates = Jinja2Templates(directory="app/templates")
login_router = APIRouter(tags=['login'])


@login_router.post("/register", response_model=UserOut)
async def register(user: UserCreate, db: AsyncSession = Depends(get_session)):
    return await auth.create_user(db, user)


@login_router.get("/register")
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@login_router.get("/login")
async def register(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@login_router.post("/login")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_session)):
    return await auth.login(db, form_data)
