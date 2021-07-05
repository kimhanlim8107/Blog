from flask import session, g
from blog.db import init_db, get_db

def test_write(client):
    with client.session_transaction() as sess:
        sess['id'] = 'test_id'
    response_page_load = client.get('/write/create')
    response_empty_title = client.post('/write/create', data={'title':'', 
                                                              'repository':'test_repository', 
                                                              'content':'test_content'})
    response_empty_content = client.post('/write/create', data={'title':'test_title', 
                                                                'repository':'test_repository', 
                                                                'content':''})
    response_empty_form = client.post('/write/create', data={'title':'', 
                                                             'repository':'test_repository', 
                                                             'content':''})
    response_normal_input = client.post('/write/create', data={'title':'test_title', 
                                                            'repository':'test_repository', 
                                                            'content':'test_content'}, follow_redirects=True)
    data = get_db().execute("SELECT * FROM post WHERE post_id = 1").fetchone()

    assert response_page_load.status_code == 200
    assert b'title is required' in response_empty_title.data
    assert b'content is required' in response_empty_content.data
    assert b'title and content are required' in response_empty_form.data
    assert response_normal_input.status_code == 200
    assert data['title'] == 'test_title'
    assert data['repository'] == 'test_repository'
    assert data['content'] == 'test_content'
    assert data['writer'] == 'test_id'

    init_db()
    
def test_update(client):
    get_db().execute("INSERT INTO user (user_id, user_pw) VALUES ('test_id', 'test_pw')")
    get_db().execute("INSERT INTO post (title, repository, content, date, writer) VALUES ('test_title', 'test_repository', 'test_content', '2000-01-01 00:00', 'test_id')")

    g.user = 'test_id'
    with client.session_transaction() as session:
        session['id'] = 'test_id'
        session['writer'] = 'test_id'   
    response_page_load = client.get('/write/update/post/1')
    response_empty_title = client.post('/write/update/post/1', data={'title':'', 
                                                              'repository':'test_repository_update', 
                                                              'content':'test_content_update'})
    response_empty_content = client.post('/write/update/post/1', data={'title':'test_title_update', 
                                                                'repository':'test_repository_update', 
                                                                'content':''})
    response_empty_form = client.post('/write/update/post/1', data={'title':'', 
                                                             'repository':'test_repository_update', 
                                                             'content':''})
    response_normal_input = client.post('/write/update/post/1', data={'title':'test_title_update', 
                                                               'repository':'test_repository_update', 
                                                               'content':'test_content_update'}, follow_redirects=True)
    data = get_db().execute("SELECT * FROM post WHERE post_id = 1").fetchone()

    assert response_page_load.status_code == 200
    assert b'title is required' in response_empty_title.data
    assert b'content is required' in response_empty_content.data
    assert b'title and content are required' in response_empty_form.data
    assert response_normal_input.status_code == 200
    assert data['title'] == 'test_title_update'
    assert data['repository'] == 'test_repository_update'
    assert data['content'] == 'test_content_update'

    init_db()

def test_delete(client):
    response_access_delete = client.get('/write/delete/post/1', follow_redirects=True)
    data = get_db().execute("SELECT * FROM post WHERE post_id = 1").fetchone()

    assert response_access_delete.status_code == 200
    assert data == None