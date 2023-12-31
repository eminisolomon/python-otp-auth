from datetime import datetime, timedelta

import pytest
from starlette.testclient import TestClient

from app import config as app_config
from app.db.base import Base
from app.main import app as _app
from app.db.session import Session, engine


@pytest.fixture(scope="session")
def app(config):
    return _app


@pytest.fixture(scope="session")
def config():
    return app_config


@pytest.fixture(scope="session", autouse=True)
def db(app, config):
    Base.metadata.create_all(engine)
    yield Session()
    Base.metadata.drop_all(engine)


@pytest.fixture
def client(app):
    return TestClient(app)


@pytest.fixture
def now():
    return datetime.now


@pytest.fixture
def delta():
    return timedelta
