from app.api.auth_api import auth_router
from app.api.films_api import films_router
from app.api.misc_api import misc_router


ROUTES = {
    "": misc_router,
    "/auth": auth_router,
    "/films": films_router
}
