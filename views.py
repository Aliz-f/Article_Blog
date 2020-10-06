from application import app
from flask import render_template , redirect , flash , url_for
from application.forms import RegisterForm , LoginForm
from application.models import User , Post

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


@app.route("/")
@app.route("/home")
def home():
    response = render_template('home.html' , posts = posts)
    return response


@app.route("/about")
def about():
    response = 'About page'
    return response


@app.route("/register" , methods = ['POST' , 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash (f'Account Created for {form.username.data}' , 'success')
        response = redirect(url_for('home'))
    else:
        response = render_template('register.html' , title = 'Register' , form = form)
    return response


@app.route("/login" , methods = ['POST' , 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in!' , 'success')
            return redirect(url_for('home'))
    
    else:
        flash('Login Unsuccessful. Please check username and password', 'danger')
    
    response = render_template('login.html' , title = 'Login' , form = form)
    
    return response