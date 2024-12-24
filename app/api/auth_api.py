from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import Response
from starlette.requests import Request
from starlette.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from app.db import get_session
from app.services import auth
from app.models.user_model import User


auth_router = APIRouter(tags=['auth'])


@auth_router.get("/profile")
def profile(request: Request):
    print(request.body())
    return "OK"


@auth_router.post("/register")
def register(request: Request):
    print(request)
    return Response(status_code=HTTP_200_OK)


@auth_router.post("/login")
def login_user():
    return {"message": "User not found"}


