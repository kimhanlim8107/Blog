from flask import session
from blog.db import get_db, init_db

def test_register(client):
    get_db().execute("INSERT INTO user (user_id, user_pw) VALUES ('test_id', 'test_pw')")

    response = client.get('/register')
    response_blank = client.post('/register', data={'id':'', 'pw':''})
    response_overlap = client.post('/register', data={'id':'test_id', 'pw':'test_pw'})
    response_correct = client.post('/register', data={'id':'new_test_id', 'pw':'test_pw'}, follow_redirects=True)
    data = get_db().execute("SELECT * FROM user WHERE user_id = 'new_test_id'").fetchone()

    assert response.status_code == 200
    assert b"ID or Password is required" in response_blank.data
    assert b"ID is already registered" in response_overlap.data
    assert response_correct.status_code == 200
    assert data != None

    init_db()


def test_login(client):
    get_db().execute("INSERT INTO user (user_id, user_pw) VALUES ('test_id', 'test_pw')")

    response = client.get('/login')
    response_wrong_user = client.post('/login', data={'id':'wrong_test_id', 'pw':'wrong_test_pw'})
    response_correct_user = client.post('/login', data={'id':'test_id', 'pw':'test_pw'}, follow_redirects=True)

    assert response.status_code == 200
    assert b"ID or Password is Incorrect" in response_wrong_user.data
    assert response_correct_user.status_code == 200

    init_db()

def test_logout(client):
    response = client.get('/logout', follow_redirects=True)
    with client.session_transaction() as sess:
        sess['id'] = 'test_id'
    client.get('/logout', follow_redirects=True)

    assert response.status_code == 200
    assert 'test_id' not in sess
    