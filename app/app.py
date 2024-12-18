from fastapi import FastAPI


def get_app() -> FastAPI:
    app = FastAPI(title="Management Films Service")

    return app
