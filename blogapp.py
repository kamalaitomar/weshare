from flask import Flask , render_template , url_for

app = Flask(__name__)


posts = [
    {
        'author' : 'Said boutoudit',
        'title' : 'Blog Post 1',
        'content' : 'First Post content',
        'date_posted': 'mai 20,2020'

    } ,

     {
        'author' : 'Janr chris',
        'title' : 'Blog Post 2',
        'content' : 'Second Post content',
        'date_posted': 'mai 21,2020'

    },

    {
        'author' : 'Kamal ait omar',
        'title' : 'Blog Post 3',
        'content' : 'third Post content',
        'date_posted': 'mai 22,2020'

    } 
]

@app.route('/')
@app.route('/home')
def home():
    return  render_template('home.html' , posts = posts)

@app.route('/about')
def about():
    return  render_template('about.html' , title = 'about')

if __name__ == '__main__':
    app.run(debug = True)
 