from flask import Flask, render_template, url_for
app = Flask(__name__)


posts = [
    {
        'author' : 'Ivo Zelic',
        'title' : 'Blog Post 1',
        'content' : 'First Post Content',
        'date_posted' : 'ožujak 18, 2022'
    },
    {
        'author' : 'Ana Cigula',
        'title' : 'Blog Post 2',
        'content' : 'Second Post Content',
        'date_posted' : 'ožujak 19, 2022'
    }
]



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', 
                        posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', 
                        title='About')

if __name__ == "__main__":
    app.run(debug=True)