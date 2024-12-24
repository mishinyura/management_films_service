# from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.future import select
# from passlib.context import CryptContext
# from app.models.user_model import User
# from app.config import settings
# from datetime import datetime, timedelta
# import jwt
# import uuid
#
#
# SECRET_KEY = settings.app.app_key
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 60
#
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
#
#
# async def get_user(db: AsyncSession, username: str) -> User:
#     result = await db.execute(select(User).filter(User.username == username))
#     return result.scalars().first()
#
#
# def verify_password(plain_password, hashed_password) -> bool:
#     return pwd_context.verify(plain_password, hashed_password)
#
#
# def get_password_hash(password) -> str:
#     return pwd_context.hash(password)
#
#
# async def create_user(db: AsyncSession, user: UserCreate) -> User:
#     db_user = User(username=user.username, hashed_password=get_password_hash(user.password))
#     db.add(db_user)
#     await db.commit()
#     await db.refresh(db_user)
#     return db_user
#
#
# def create_access_token(data: dict, expires_delta=None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt
#
#
# async def login(db: AsyncSession, form_data: OAuth2PasswordRequestForm):
#     user = await get_user(db, form_data.username)
#     if not user or not verify_password(form_data.password, user.hashed_password):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token = create_access_token(data={"sub": user.username})
#     return {"access_token": access_token, "token_type": "bearer"}
#
# def get_user_id_from_token():
#     pass