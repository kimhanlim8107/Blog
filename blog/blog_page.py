from flask import Blueprint, render_template, abort, session, request
from blog.db import get_db

bp = Blueprint('page', __name__)

@bp.route('/post/<post_id>')
def page(post_id):
    db = get_db()
    post = db.execute("SELECT * FROM post WHERE post_id = ?",(post_id)).fetchone()

    if post == None:
        abort(404)
    else:
        session['url'] = request.path
        session['writer'] = post['writer']
        return render_template('blog_page.html', post=post)
