from blog.blog_write import get_db

def test_write(client):
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
    data = get_db().execute("SELECT * FROM post WHERE title = 'test_title'").fetchone()

    assert response_page_load.status_code == 200
    assert b'title is required' in response_empty_title.data
    assert b'content is required' in response_empty_content.data
    assert b'title and content are required' in response_empty_form.data
    assert response_normal_input.status_code == 200
    assert data['title'] == 'test_title'
    assert data['repository'] == 'test_repository'
    assert data['content'] == 'test_content'
    
def test_update(client):
    response_page_load = client.get('/write/update/test_repository/1')
    response_empty_title = client.post('/write/update/test_repository/1', data={'title':'', 
                                                              'repository':'test_repository_update', 
                                                              'content':'test_content_update'})
    response_empty_content = client.post('/write/update/test_repository/1', data={'title':'test_title_update', 
                                                                'repository':'test_repository_update', 
                                                                'content':''})
    response_empty_form = client.post('/write/update/test_repository/1', data={'title':'', 
                                                             'repository':'test_repository_update', 
                                                             'content':''})
    response_normal_input = client.post('/write/update/test_repository/1', data={'title':'test_title_update', 
                                                               'repository':'test_repository_update', 
                                                               'content':'test_content_update'}, follow_redirects=True)
    data = get_db().execute("SELECT * FROM post WHERE id = 1").fetchone()

    assert response_page_load.status_code == 200
    assert b'title is required' in response_empty_title.data
    assert b'content is required' in response_empty_content.data
    assert b'title and content are required' in response_empty_form.data
    assert response_normal_input.status_code == 200
    assert data['title'] == 'test_title_update'
    assert data['repository'] == 'test_repository_update'
    assert data['content'] == 'test_content_update'

def test_delete(client):
    response_access_delete = client.get('/write/delete/test_repository_update/1', follow_redirects=True)
    data = get_db().execute("SELECT * FROM post WHERE id = 1").fetchone()

    assert response_access_delete.status_code == 200
    assert data == None