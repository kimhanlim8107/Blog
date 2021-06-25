from tempfile import NamedTemporaryFile

import pytest

from blog import create_app
from blog.db import init_db, get_db

@pytest.fixture(scope="session")
def app():
    db_fd = NamedTemporaryFile().name

    app = create_app({
        "TESTING": True,
        "DATABASE": db_fd
    })

    with app.app_context():
        # 테이블 스키마 실행
        init_db()
        # 테이블 데이터 입력
        get_db().execute("""INSERT INTO post (title, repository, content, date)
                            VALUES ('test_title', 'test_repository', 'test_content', '2000-01-01 00:00');""")
        get_db().commit()
        yield app


@pytest.fixture(scope="session")
def client(app):
    with app.test_client() as client:
        with app.app_context():
            yield client

