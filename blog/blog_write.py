from datetime import datetime
from flask import (
    Blueprint, request, render_template, redirect
)
from blog.db import get_db

bp = Blueprint('blog_write', __name__)

@bp.route('/blog_write', methods=('GET', 'POST'))
def blog_write():
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

            return redirect('/blog_write')
        

    return render_template('blog_write.html')