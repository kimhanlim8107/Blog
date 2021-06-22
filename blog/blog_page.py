from flask import Blueprint, render_template
from blog.db import get_db

bp = Blueprint('page',__name__)

@bp.route('/<repository>/<id>')
def page(repository, id):
    db = get_db()
    post = db.execute("SELECT * FROM post WHERE repository='{}' AND id='{}'".format(repository, id)).fetchone()
    return render_template('blog_page.html', post=post)