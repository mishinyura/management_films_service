from fastapi import FastAPI
from app.api.routes import ROUTES


def setup_routers(app: FastAPI) -> None:
    for prefix, router in ROUTES.items():
        app.include_router(router, prefix=prefix)
        print(prefix, router)


def get_app() -> FastAPI:
    app = FastAPI(title="Films Service")
    setup_routers(app)
    return app