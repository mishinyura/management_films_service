from fastapi import FastAPI
import uvicorn
from .logger import setup_logger

app = FastAPI()
setup_logger()  # Вызываем функцию настройки логгера

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)