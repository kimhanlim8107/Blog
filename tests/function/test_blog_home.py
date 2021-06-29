from bs4 import BeautifulSoup
from blog.db import get_db, init_db

def blog_home(client, repo):
    get_db().execute("INSERT INTO user (user_id, user_pw) VALUES ('test_id', 'test_pw')")
    get_db().execute("INSERT INTO post (title, repository, content, date, writer) VALUES ('test_title', 'test_repository', 'test_content', '2000-01-01 00:00', 'test_client')")

    response_200 = client.get('/{}'.format(repo))
    response_404 = client.get('/{}/page/2'.format(repo))
    post_num = len(BeautifulSoup(response_200.data, 'html.parser').select('ul.main_lists li'))
    
    assert response_200.status_code == 200
    assert response_404.status_code == 404
    assert post_num <= 5

    init_db()

def test_home(client):
    blog_home(client, 'home')

def test_frontend(client):
    blog_home(client, 'frontend')

def test_backend(client):
    blog_home(client, 'backend')

def test_devops(client):
    blog_home(client, 'devops')

def test_cs(client):
    blog_home(client, 'cs')


