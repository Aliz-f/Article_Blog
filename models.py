from application import db , login_manager , app
from datetime import datetime
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@login_manager.user_loader
def load_user (user_id):
    return User.query.get(int(user_id))


class User (db.Model,UserMixin):
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column (db.String (20) , nullable = False , unique = True)
    email = db.Column (db.String (200) , nullable = False , unique = True)
    password = db.Column (db.String(200) , nullable = False)
    posts = db.relationship('Post' , backref = db.backref('author') , lazy = True)
    image_file = db.Column(db.String(100) , nullable = False , default = 'default.jpg')
    
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

class Post (db.Model):
    id = db.Column(db.Integer , primary_key = True)
    title = db.Column (db.String (20) , nullable = False)
    data_posted = db.Column (db.DateTime , nullable = False , default =datetime.utcnow)
    content = db.Column (db.Text , nullable = False)
    user_id = db.Column (db.Integer , db.ForeignKey('user.id') , nullable = False)

db.create_all()