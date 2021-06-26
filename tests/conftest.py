from tempfile import NamedTemporaryFile

import pytest

from blog import create_app
from blog.db import init_db, get_db

@pytest.fixture(scope="session")
def app():
    db_file = NamedTemporaryFile().name

    app = create_app({
        "TESTING": True,
        "DATABASE": db_file
    })

    with app.app_context():
        init_db()
        get_db()
        yield app


@pytest.fixture(scope="session")
def client(app):
    with app.test_client() as client:
        with app.app_context():
            yield client

