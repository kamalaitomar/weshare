from flask import render_template , url_for , flash , redirect
from blogapp import app
from blogapp.forms import Registration , Login
from blogapp.models import User, Post



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
    form = Registration()
    if form.validate_on_submit():
        flash(f'account created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return  render_template('register.html' , title = 'Register', form = form)
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        if form.email.data == 'admin@admin.com' and form.password.data == 'admin' or form.email.data == 'admin2@admin.com' and form.password.data == '12345':
            flash('You have been logged in', 'success-login' ) #succes-login is the flash message comment for login
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please Check Your Informations ', 'error') #error is the flash message comment

    return  render_template('login.html' , title = 'login', form = form)