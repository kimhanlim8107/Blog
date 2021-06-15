from blog import create_app

def test_hello(client):
    hello = client.get('/hello')
    assert hello.data == b'Hello World!'