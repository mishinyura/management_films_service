from fastapi import APIRouter, Depends
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import Response
from starlette.requests import Request
from starlette.status import HTTP_404_NOT_FOUND, HTTP_201_CREATED, HTTP_409_CONFLICT, HTTP_200_OK

from app.core.db import get_session
from app.core.auth import create_user, login
from app.services.user_service import user_service
from app.schemas.user_schema import UserSchema
from app.core.exceptions import DuplicateException

auth_router = APIRouter(tags=["authentication"])


@auth_router.get("/profile")
async def profile(session: AsyncSession = Depends(get_session)):
    user = await user_service.get_user(session)
    return {'message': user}


@auth_router.post("/register")
async def registration(request: UserSchema, session: AsyncSession = Depends(get_session)):
    try:
        await user_service.add_user(request=request, session=session)
    except DuplicateException:
        return Response(status_code=HTTP_409_CONFLICT, content='This user is already registered')
    return Response(status_code=HTTP_201_CREATED, content='Registration is successful')


@auth_router.post("/login")
async def login(request: UserSchema, session: AsyncSession = Depends(get_session)):
    try:
        await user_service.get_user(request=request, session=session)
    except DuplicateException:
        return Response(status_code=HTTP_409_CONFLICT, content='NONE')
    return Response(status_code=HTTP_200_OK, content='Login is successful')




#Misha
templates = Jinja2Templates(directory="frontend/templates")
login_router = APIRouter(tags=['login'])


@login_router.post("/register", response_model=UserSchema)
async def register(user: UserSchema, db: AsyncSession = Depends(get_session)):
    return await create_user(db, user)


@login_router.get("/register")
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@login_router.get("/login")
async def register(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@login_router.post("/login")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_session)):
    return await login(db, form_data)