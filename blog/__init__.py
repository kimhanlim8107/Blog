import os
from flask import Flask, session, request

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'blog.sqlite')
    )

    if test_config == None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except:
        pass

    from . import db
    db.init_app(app)

    from . import blog_write
    app.register_blueprint(blog_write.bp)

    from . import blog_home
    app.register_blueprint(blog_home.bp)
    app.add_url_rule('/', endpoint='home.home', defaults={'page_num' : 1})

    from . import blog_page
    app.register_blueprint(blog_page.bp)

    from . import blog_auth
    app.register_blueprint(blog_auth.bp)

    return app
