from datetime import datetime
from flask import (
    Blueprint, request, render_template, redirect, url_for, redirect, flash, session
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

        if content == '' and title == '':
            error = 'title and content are required'
        elif title == '':
            error = 'title is required'
        elif content == '':
            error = 'content is required'
            
        
        if error == None:
            db.execute("INSERT INTO post (title, repository, content, date) VALUES (?, ?, ?, ?);", (title, repo, content, date))
            db.commit()

            return redirect(url_for('home.home'))
        
        flash(error)

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

        if content == '' and title == '':
            error = 'title and content are required'
        elif title == '':
            error = 'title is required'
        elif content == '':
            error = 'content is required'

        if error == None:
            db.execute("UPDATE post SET title = ?, repository = ?, content = ?, date = ? WHERE id = ?", (title, repo, content, date, id))
            db.commit()

            return redirect(url_for('home.home'))
        
        flash(error)

    return render_template('blog_update.html', post=post)

@bp.route('/delete/<repository>/<id>')
def delete(repository, id):
    db = get_db()
    db.execute("DELETE FROM post WHERE id = ? AND repository = ?;", (id, repository))
    db.execute("UPDATE post SET id = (id - 1) WHERE id >= ?;", (id,))
    db.execute("UPDATE 'sqlite_sequence' SET seq = (seq - 1)")
    db.commit()
    db.execute("VACUUM;")
    db.commit()
    
    return redirect(url_for('home.home'))
