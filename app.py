from flask import Flask, flash, redirect, render_template, url_for

from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '02b44f2abc7342ab8286eb3e2a70d995'


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
    
    
@app.route("/register", methods=['GET', 'POST'])
def register():
    
    form = RegistrationForm()
    
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', category='success')
        return redirect(url_for('home'))
    
    return render_template('register.html', 
                        title='Register',
                        form=form)
    

@app.route("/login", methods=['GET', 'POST'])
def login():
    
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == '123':
            flash('You have been logged in', category='success')
        else:
            flash('Login unsuccessful! Please check username and password!', category='danger')
            
    return render_template('login.html', 
                        title='Login',
                        form=form)





if __name__ == "__main__":
    app.run(debug=True)