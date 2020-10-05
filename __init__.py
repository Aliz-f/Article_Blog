from flask import Flask , render_template , url_for , redirect , flash
from application.forms import RegisterForm , LoginForm

# from application import forms

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b0074f497b6ee7520a70086c03f45e09'
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
def Home():
    response = render_template('home.html' , posts = posts)
    return response


@app.route("/register" , methods = ['POST' , 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash (f'Account Created for {form.username.data}' , 'success')
        response = redirect(url_for('Home'))
    else:
        response = render_template('register.html' , title = 'Register' , form = form)
    return response

@app.route("/login" , methods = ['POST' , 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in!' , 'success')
            return redirect(url_for('Home'))
    
    else:
        flash('Login Unsuccessful. Please check username and password', 'danger')
    
    response = render_template('login.html' , title = 'Login' , form = form)
    
    return response