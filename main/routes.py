from flask import render_template, url_for, flash, redirect
from main import app
from main.forms import RegisterForm, LoginForm

posts = [
    {
        "author":"Usman Javed",
        "title":"Blog post 1",
        "content":"First post content to be published.",
        "date_posted":"20-Sep-2024"
    },
    {
        "author":"Akhtar Arif",
        "title":"Blog post 2",
        "content":"Second post content to be published.",
        "date_posted":"21-Sep-2024"
    },
    {
        "author":"Saad Haider",
        "title":"Blog post 3",
        "content":"Third post content to be published.",
        "date_posted":"22-Sep-2024"
    }
]
@app.get('/')
@app.get('/home')
def home():
    return render_template('index.html', posts=posts)

@app.get('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)

@app.route('/login', methods=['get','post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin11' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
            
    return render_template('login.html', title="Login", form=form)
