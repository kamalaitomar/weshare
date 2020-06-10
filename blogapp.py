from flask import Flask , render_template , url_for

app = Flask(__name__)


posts = [
    {
        'author' : 'Said boutoudit',
        'title' : 'Blog Post 1',
        'content' : '''First Post content : is simply dummy text of the printing and typesetting
                    industry. Lorem Ipsum has been the industrys standard dummy text ever since
                    the w hen an unknown printer took a galley of  scrambled it to
                    make a  specimen book. It has survived not only five centuries, but also the
                    leap into electronic typesetting, remaining essentially unchanged. It was popularised
                    in thewith the release of Letraset sheets containing Lorem Ipsum passages,
                    and more recently with desktop publishing software like Aldus PageMaker including 
                    versions of Lorem Ipsum.''',
        'date_posted': '20 Mai 2020'

    } ,

     {
        'author' : 'Janr chris',
        'title' : 'Blog Post 2',
        'content' : '''Second Post content : is simply dummy text of the printing and typesetting
                    industry. Lorem Ipsum has been the industrys standard dummy text ever since
                    the w hen an unknown printer took a galley of  scrambled it to
                    make a  specimen book. It has survived not only five centuries, but also the
                    leap into electronic typesetting, remaining essentially unchanged. It was popularised
                    in thewith the release of Letraset sheets containing Lorem Ipsum passages,
                    and more recently with desktop publishing software like Aldus PageMaker including 
                    versions of Lorem Ipsum.''',
        'date_posted': '21 Mai 2020'

    },

    {
        'author' : 'Kamal ait omar',
        'title' : 'Blog Post 3',
        'content' : '''thied Post content : is simply dummy text of the printing and typesetting
                    industry. Lorem Ipsum has been the industrys standard dummy text ever since
                    the w hen an unknown printer took a galley of  scrambled it to
                    make a  specimen book. It has survived not only five centuries, but also the
                    leap into electronic typesetting, remaining essentially unchanged. It was popularised
                    in thewith the release of Letraset sheets containing Lorem Ipsum passages,
                    and more recently with desktop publishing software like Aldus PageMaker including 
                    versions of Lorem Ipsum.''',
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

if __name__ == '__main__':
    app.run(debug = True)
 