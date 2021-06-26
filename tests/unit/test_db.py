from flask import g

from blog.db import get_db

def test_db(app):
    database = get_db()
    database.execute("""INSERT INTO post (title, repository, content, date)
                            VALUES ('test_title', 'test_repository', 'test_content', '2000-01-01 00:00');""")
    database.commit()
    data = database.execute("SELECT * FROM post WHERE id = 1;").fetchone()

    assert database == g.db
    assert data['title'] == "test_title"
    assert data['repository'] == "test_repository"
    assert data['content'] == "test_content"
    assert data['date'] == "2000-01-01 00:00"