import secrets
from application import app , db , bcrypt
from flask import render_template , redirect , flash , url_for , request
from application.forms import RegisterForm , LoginForm , UpdateAccountForm
from application.models import User , Post
from flask_login import login_user , current_user , logout_user , login_required

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


def save_picture(form_picture):
    pass

@app.route("/")
@app.route("/home")
def home():
    response = render_template('home.html' , posts = posts)
    return response


@app.route("/about")
def about():
    response = render_template('about.html')
    return response


@app.route("/register" , methods = ['POST' , 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data , password = hashed_password , email = form.email.data)
        db.session.add(user)
        db.session.commit()
        flash ('Your account has been created , Now you can Log in!' , 'success')
        response = redirect(url_for('login'))
    else:
        response = render_template('register.html' , title = 'Register' , form = form)
    return response


@app.route("/login" , methods = ['POST' , 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password , form.password.data):
            login_user(user , remember= form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:    
                return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    response = render_template('login.html' , title = 'Login' , form = form)
    return response

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account" , methods = ['GET' , 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your Account info has been update!' , 'success')
        return redirect('account') #problem for reload page solve (alert)
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    image_file = url_for ('static' , filename = 'profile_pics/'+ current_user.image_file)
    response = render_template('account.html' , title = 'Account' , image_file = image_file , form = form)
    return response

@app.route("/show-db")
@login_required
def showDB():
    data = User.query.all()
    # data = Post.query.all()
    response = render_template('show-db.html' , datas = data , title = 'Show DataBase')
    return response