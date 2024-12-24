from fastapi import APIRouter, Request

misc_router = APIRouter()


@misc_router.get("/")
def healthcheck(request: Request) -> str:
    return request.method