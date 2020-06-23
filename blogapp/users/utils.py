import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from blogapp import mail

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profil_pics', picture_fn)

    output_size = (150, 150)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request' , sender='noreply@weshare.com' , recipients=[user.email])
    msg.body = f""" To reset your password , visit the following link:
{url_for('users.reset_token' , token = token , _external=True)}  
this link expires in 30 minutes 
"""
    mail.send(msg)