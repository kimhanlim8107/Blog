from flask import Blueprint, render_template, request, url_for, abort

from blog.db import get_db

bp = Blueprint('home', __name__)

@bp.route('/', defaults={'page_num' : 1})
@bp.route('/home/page/<int:page_num>')
def home(page_num):
    db = get_db()
    num_post = db.execute("SELECT id FROM post ORDER BY id DESC").fetchone()['id']
    min_page_num = 1
    max_page_num = (int(num_post) // 5 + 1)

    if page_num < min_page_num or page_num > max_page_num:
        abort(400)
    else:
        posts = db.execute("SELECT * FROM post ORDER BY date DESC").fetchall()
        posts = posts[(5 * page_num - 5) : (5 * page_num)]
        return render_template('blog_home.html', posts=posts, page_num=page_num, min_page_num=min_page_num, max_page_num=max_page_num)
