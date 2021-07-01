from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from blog.db import get_db

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    auth_header = 'LOGIN'

    if request.method == 'POST':
        db = get_db()
        id = request.form['id']
        pw = request.form['pw']
        error = None
        val_data = db.execute("SELECT * FROM user WHERE user_id = ? AND user_pw = ?", (id, pw)).fetchone()

        if val_data == None:
            error = "ID or Password is Incorrect"

        flash(error)
        
        if error == None:
            session['id'] = id
            return redirect(url_for('home.home'))

    return render_template('blog_auth.html', auth_header=auth_header)