from application import db
from datetime import datetime


class User (db.Model):
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column (db.String (20) , nullable = False , unique = True)
    email = db.Column (db.String (200) , nullable = False , unique = True)
    password = db.Column (db.String(200) , nullable = False)
    posts = db.relationship('Post' , backref = db.backref('author') , lazy = True)
    image_file = db.Column(db.String(100) , nullable = False , default = 'default.jpg')

class Post (db.Model):
    id = db.Column(db.Integer , primary_key = True)
    title = db.Column (db.String (20) , nullable = False)
    data_posted = db.Column (db.DateTime , nullable = False , default =datetime.utcnow)
    content = db.Column (db.Text , nullable = False)
    user_id = db.Column (db.Integer , db.ForeignKey('user.id') , nullable = False)

# db.create_all()