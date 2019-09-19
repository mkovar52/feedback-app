import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    # dev db
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password123@localhost/feedback'

else:
    # prod db
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://kcprcbqytevqdn:1c24fce25788278a829109e22d3290b7dc1ada958419fd2d63465ee1335d719e@ec2-54-235-92-43.compute-1.amazonaws.com:5432/d4rtjhenrda6h7'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# -- db object
db = SQLAlchemy(app)

login_manager.init_app(app)
login_manager.login_view = 'login'
