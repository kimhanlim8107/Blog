from bs4 import BeautifulSoup

def blog_home(client, repo):
    response_200 = client.get('/{}'.format(repo))
    response_404 = client.get('/{}/page/2'.format(repo))
    post_num = len(BeautifulSoup(response_200.data, 'html.parser').select('ul.main_lists li'))
    
    assert response_200.status_code == 200
    assert response_404.status_code == 404
    assert post_num <= 5

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


