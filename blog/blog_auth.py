from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from blog.db import get_db

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    auth_header = 'REGISTER'
    auth_url = url_for('auth.register')

    if request.method == 'POST':
        db = get_db()
        id = request.form['id']
        pw = request.form['pw']
        error = None
        val_data = db.execute("SELECT * FROM user WHERE user_id = ?;", (id,)).fetchone()
        
        if id == '' or pw == '':
            error = "ID or Password is required"
        elif val_data != None:
            error = "ID is already registered"

        flash(error)

        if error == None:
            db.execute("INSERT INTO user (user_id, user_pw) VALUES (?, ?);",(id, pw,))
            db.commit()

            return redirect(url_for('auth.login'))

    return render_template('blog_auth.html', auth_header=auth_header, auth_url=auth_url)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    auth_header = 'LOGIN'
    auth_url = url_for('auth.login')

    if request.method == 'POST':
        db = get_db()
        id = request.form['id']
        pw = request.form['pw']
        error = None
        val_data = db.execute("SELECT * FROM user WHERE user_id = ? AND user_pw = ?;", (id, pw)).fetchone()
        

        if val_data == None:
            error = "ID or Password is Incorrect"

        flash(error)
        
        if error == None:
            session['id'] = id
            return redirect(url_for('home.home'))

    return render_template('blog_auth.html', auth_header=auth_header, auth_url=auth_url)