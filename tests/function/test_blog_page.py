from blog.db import get_db, init_db

def test_page(client):
    get_db().execute("INSERT INTO user (user_id, user_pw) VALUES ('test_id', 'test_pw')")
    get_db().execute("INSERT INTO post (title, repository, content, date, writer) VALUES ('test_title', 'test_repository', 'test_content', '2000-01-01 00:00', 'test_id')")

    response_page = client.get('/post/1')
    response_wrong = client.get('/post/2')

    assert response_page.status_code == 200
    assert response_wrong.status_code == 404

    init_db()