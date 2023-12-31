from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from app import config
from app.auth.api import router as auth_api_router
from app.core.middleware import register_common_errorhandler
from app.db.middleware import db_session_middleware


def create_app(config):
    """ Factory function for creating an app instance """
    app = FastAPI()
    register_routers(app, config)
    register_middleware(app, config)
    return app


def register_routers(app: FastAPI, config):
    """ Router includes go here """
    app.include_router(auth_api_router, prefix="/auth")


def register_middleware(app: FastAPI, config):
    """ Install some middleware """
    app.middleware("http")(db_session_middleware)
    app.add_middleware(SessionMiddleware, secret_key=config.SECRET_KEY)
    register_common_errorhandler(app, config)


app = create_app(config)
