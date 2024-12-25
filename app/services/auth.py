from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from passlib.context import CryptContext
from app.models.users import User
from app.db import get_session
from app.schemas.schemas import UserCreate
from app.config import settings
from datetime import datetime, timedelta
import jwt
from loguru import logger


SECRET_KEY = settings.app.app_key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def get_user(db: AsyncSession, username: str) -> User:
    result = await db.execute(select(User).filter(User.username == username))
    return result.scalars().first()


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password) -> str:
    return pwd_context.hash(password)


async def create_user(db: AsyncSession, user: UserCreate) -> User:
    logger.info(f"Создание пользователя: {user.username}")
    try:
        existing_user = await db.execute(select(User).where(User.username == user.username))
        if existing_user.scalar():
            logger.warning(f"Создание пользователя: имя {user.username} уже занято")
            raise HTTPException(status_code=400, detail="Username already registered")

        db_user = User(username=user.username, hashed_password=get_password_hash(user.password))
        db.add(db_user)
        await db.commit()
        await db.refresh(db_user)
        logger.success(f"Создание пользователя: успешно для {user.username}")
        return db_user
    except Exception as e:
        logger.error(f"Создание пользователя: ошибка для {user.username} - {str(e)}")
        raise HTTPException(status_code=500, detail="Ошибка при создании пользователя")


def create_access_token(data: dict, expires_delta=None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def login(db: AsyncSession, form_data: OAuth2PasswordRequestForm):
    user = await get_user(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


async def get_current_user(db: AsyncSession = Depends(get_session), token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception

    user = await get_user(db, username=username)
    if user is None:
        raise credentials_exception
    return user
