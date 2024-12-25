from loguru import logger
import sys


class InterceptHandler:
    def __init__(self, level):
        self.level = level

    def __call__(self, rec):
        # Получаем уровень записи
        level = logger.level(rec["level"].name).no

        # Если уровень записи ниже заданного уровня, пропускаем запись
        if level < self.level:
            return False
        else:
            return True


# Настройка логгера
def setup_logger():
    # Создаем обработчик для перехвата сообщений с уровня DEBUG
    intercept_handler = InterceptHandler(level="DEBUG")

    # Устанавливаем формат вывода логов
    fmt = ("<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> "
           "| <level>{level: <8}</level> "
           "| <cyan>{name}</cyan>"
           ":<cyan>{function}</cyan>"
           ":<cyan>{line}</cyan> - "
           "<level>{message}</level>")

    # Конфигурация логгера
    logger.configure(
        handlers=[
            {
                "sink": "logs/log.log",
                "format": fmt,
                "enqueue": True
            },
            {
                "sink": sys.stdout,
                "format": fmt,
                "filter": intercept_handler,
                "backtrace": True,
                "catch": True
            },
        ]
    )