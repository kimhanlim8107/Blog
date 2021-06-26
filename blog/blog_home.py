import math

from flask import Blueprint, render_template, abort

from blog.db import get_db

bp = Blueprint('home', __name__)

def render_post(repository, page_num):
    db = get_db()
    if repository == 'home':
        num_post = db.execute("SELECT count(*) FROM post ORDER BY id DESC").fetchone()[0]
        posts = db.execute("SELECT * FROM post ORDER BY date DESC").fetchall()
    else:
        num_post = db.execute("SELECT count(*) FROM post WHERE repository = '{}' ORDER BY id DESC".format(repository)).fetchone()[0]
        posts = db.execute("SELECT * FROM post WHERE repository = '{}' ORDER BY date DESC".format(repository)).fetchall()
    
    min_page_num = 1

    if num_post == 0:
        max_page_num = 1
    else:
        max_page_num = math.ceil(num_post / 5)
        
    function_name = repository
    posts = posts[(5 * page_num - 5) : (5 * page_num)]

    if page_num < min_page_num or page_num > max_page_num:
        abort(404)
    else:
        return render_template('blog_home.html', function_name=function_name, posts=posts, page_num=page_num, min_page_num=min_page_num, max_page_num=max_page_num)

@bp.route('/home', defaults={'page_num' : 1})
@bp.route('/home/page/<int:page_num>')
def home(page_num):
    return render_post('home', page_num)

@bp.route('/frontend', defaults={'page_num' : 1})
@bp.route('/frontend/page/<int:page_num>')
def frontend(page_num):
    return render_post('frontend', page_num)
    

@bp.route('/backend', defaults={'page_num' : 1})
@bp.route('/bakcend/page/<int:page_num>')
def backend(page_num):
    return render_post('backend', page_num)
    

@bp.route('/devops', defaults={'page_num' : 1})
@bp.route('/devops/page/<int:page_num>')
def devops(page_num):
    return render_post('devops', page_num)
    

@bp.route('/cs', defaults={'page_num' : 1})
@bp.route('/cs/page/<int:page_num>')
def cs(page_num):
    return render_post('cs', page_num)
