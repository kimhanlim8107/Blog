from datetime import datetime
from flask import (
    Blueprint, request, render_template, redirect, url_for, redirect, flash, session
)
from blog.db import get_db
from blog.blog_auth import login_required, access_required

bp = Blueprint('write', __name__, url_prefix='/write')

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def write():
    if request.method == 'POST':
        writer = session['id']
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
            db.execute("INSERT INTO post (title, repository, content, date, writer) VALUES (?, ?, ?, ?, ?);", (title, repo, content, date, writer))
            db.commit()

            return redirect(url_for('home.home'))
        
        flash(error)

    return render_template('blog_write.html')

@bp.route('/update/post/<post_id>', methods=('GET', 'POST'))
@access_required
def update(post_id):
    db = get_db()
    post = db.execute("SELECT * FROM post WHERE post_id = '{}'".format(post_id)).fetchone()

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
            db.execute("UPDATE post SET title = ?, repository = ?, content = ?, date = ? WHERE post_id = ?", (title, repo, content, date, post_id))
            db.commit()

            return redirect(url_for('home.home'))

        flash(error)

    return render_template('blog_update.html', post=post)

@bp.route('/delete/post/<post_id>')
@access_required
def delete(post_id):
    db = get_db()
    db.execute("DELETE FROM post WHERE post_id = ?", (post_id))
    db.execute("UPDATE post SET post_id = (post_id - 1) WHERE post_id >= ?;", (post_id))
    db.execute("UPDATE 'sqlite_sequence' SET seq = (seq - 1)")
    db.commit()
    db.execute("VACUUM;")
    db.commit()
    
    return redirect(url_for('home.home'))


