import pytest

from app.auth.models import User


@pytest.fixture
def sample_user(db):
    user = User(username="icebreaker", password="swordsfish")
    db.add(user)
    db.commit()
    return user
