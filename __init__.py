from flask import Flask , render_template , url_for , redirect , flash
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

file_dir = os.path.dirname(__file__)
goual_route = os.path.join(os.path.join(file_dir,'database') , 'article-database.db')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'b0074f497b6ee7520a70086c03f45e09'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + goual_route
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' #function-name
login_manager.login_message_category = 'info' #bootstarp class


import application.models
import application.views