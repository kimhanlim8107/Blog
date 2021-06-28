from flask import g

from blog.db import get_db

def test_db(app):
    database = get_db()

    assert database == g.db