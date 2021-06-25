from flask import current_app

def test_app(app):
    assert current_app.config['TESTING'] == True