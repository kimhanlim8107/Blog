from datetime import datetime
from flask import (
    Blueprint, request, render_template, redirect, url_for, redirect
)
from blog.db import get_db

bp = Blueprint('write', __name__, url_prefix='/write')

@bp.route('/create', methods=('GET', 'POST'))
def write():
    if request.method == 'POST':
        title = request.form['title']
        repo = request.form['repository']
        content = request.form['content']
        date = datetime.now().strftime('%y-%m-%d %H:%M')
        error = None
        db = get_db()

        if title == None:
            error = 'title is required'
        elif content == None:
            error = 'content is required'
        
        if error == None:
            db.execute("INSERT INTO post (title, repository, content, date) VALUES ('{}', '{}', '{}', '{}');".format(title, repo, content, date))
            db.commit()

            return redirect(url_for('home.home'))
        

    return render_template('blog_write.html')

@bp.route('/update/<repository>/<id>', methods=('GET', 'POST'))
def update(repository, id):
    db = get_db()
    post = db.execute("SELECT * FROM post WHERE repository = '{}' AND id = '{}'".format(repository, id)).fetchone()

    if request.method == 'POST':
        title = request.form['title']
        repo = request.form['repository']
        content = request.form['content']
        date = datetime.now().strftime('%y-%m-%d %H:%M')
        error = None
        db = get_db()

        if title == None:
            error = 'title is required'
        elif content == None:
            error = 'content is required'

        if error == None:
            db.execute("UPDATE post SET title = ?, repository = ?, content = ?, date = ? WHERE id = ?", (title, repo, content, date, id))
            db.commit()
            return redirect(url_for('home.home'))

    return render_template('blog_update.html', post=post)