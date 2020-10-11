from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from application.config import config

file_dir = os.path.dirname(__file__)
goual_route = os.path.join(os.path.join(file_dir,'database') , 'article-database.db')


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login' #function-name
login_manager.login_message_category = 'info' #bootstarp class
mail = Mail(app)

import application.models

from application.users.views import users
from application.posts.views import posts
from application.main.views import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
