from flask import Flask , render_template , url_for , flash , redirect
from forms import Registration , Login


app = Flask(__name__)

app.config['SECRET_KEY'] = 'd2093fb7ffb714b7119333f9a59f7b6a'


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
        flash(f'account created for {form.username.data}')
        return redirect(url_for('home'))
    return  render_template('register.html' , title = 'Register', form = form)
    

@app.route('/login')
def login():
    form = Login()
    return  render_template('login.html' , title = 'login', form = form)




if __name__ == '__main__':
    app.run(debug = True)
 