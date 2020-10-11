import os , secrets
from PIL import Image
from application import mail
from flask_mail import Message
from flask import url_for , current_app

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    f_name , f_ext = os.path.splitext(form_picture.filename) #found file foramt
    picture_fn = random_hex + f_ext 
    picutre_path = os.path.join(current_app.root_path , 'static/profile_pics', picture_fn)

    out_put_size = (125,125)
    goual_iamge  = Image.open(form_picture)
    goual_iamge.thumbnail(out_put_size)
    goual_iamge.save(picutre_path)
    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)