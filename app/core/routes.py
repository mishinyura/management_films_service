from app.api.auth_api import auth_router, login_router
from app.api.films_api import films_router


ROUTES = {
    '/auth': auth_router,
    '/films': films_router,
    '/auth2': login_router
}