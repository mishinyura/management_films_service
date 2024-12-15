from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_session
from app.schemas.schemas import UserCreate, UserOut
from app.services import auth


router = APIRouter(tags=['login'])


@router.post("/register", response_model=UserOut)
async def register(user: UserCreate, db: AsyncSession = Depends(get_session)):
    return await auth.create_user(db, user)


@router.post("/login")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_session)):
    return await auth.login(db, form_data)
