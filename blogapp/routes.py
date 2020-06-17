from flask import render_template , url_for , flash , redirect, request
from blogapp import app, db , bcrypt
from blogapp.forms import Registration , Login
from blogapp.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


posts = [
    {
        'author' : 'Said boutoudit',
        'title' : 'Blog Post 1',
        'content' : '''First Post content : is simply dummy text of the printing and typesetting
                    industry. Lorem Ipsum has been the industrys standard dummy text ever since
                    the w hen an unknown printer took a galley of  scrambled it to
                    make a  specimen book.''',
        'date_posted': '20 Mai 2020'
    } ,
    {
        'author' : 'Janr chris',
        'title' : 'Blog Post 2',
        'content' : '''Second Post content : is simply dummy text of the printing and typesetting
                    industry the release of Letraset sheets containing Lorem Ipsum passages,
                    and more recently with desktop publishing software like Aldus PageMaker including 
                    versions of Lorem Ipsum ''',
        'date_posted': '21 Mai 2020'

    },

    {
        'author' : 'Kamal ait omar',
        'title' : 'Blog Post 3',
        'content' : '''thied Post content : is simply dummy text of the printing and typesetting
                    industry. Lorem Ipsum has been the industrys standard dummy text ever since
                    the w hen an unknown printer ''',
        'date_posted': '22 Mai 2020'

    } 
]

@app.route('/')
@app.route('/home')
def home():
    return  render_template('home.html' , posts = posts)

@app.route('/about')
def about():
    return  render_template('about.html' , title = 'about')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = Registration()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password= hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return  render_template('register.html' , title = 'Register', form = form)
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please Check Your Informations ', 'error') #error is the flash message comment

    return  render_template('login.html' , title = 'login', form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account')
@login_required
def account():
    return  render_template('account.html' , title = 'account')