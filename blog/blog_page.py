from flask import Blueprint, render_template, abort, session
from blog.db import get_db

bp = Blueprint('page', __name__)

@bp.route('/<repository>/<id>')
def page(repository, id):
    db = get_db()
    post = db.execute("SELECT * FROM post WHERE repository='{}' AND id='{}'".format(repository, id)).fetchone()

    if post == None:
        abort(404)
    else:
        return render_template('blog_page.html', post=post)