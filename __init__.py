from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from dotenv import load_dotenv

load_dotenv() 

file_dir = os.path.dirname(__file__)
goual_route = os.path.join(os.path.join(file_dir,'database') , 'article-database.db')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'b0074f497b6ee7520a70086c03f45e09'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + goual_route
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login' #function-name
login_manager.login_message_category = 'info' #bootstarp class
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

import application.models

from application.users.views import users
from application.posts.views import posts
from application.main.views import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
