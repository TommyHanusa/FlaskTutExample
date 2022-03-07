from app import flaskApp
from flask import render_template, flash, redirect,url_for
from app.forms import LoginForm

@flaskApp.route('/')
@flaskApp.route('/index')
def index():
    user = {'username': 'Tommy'} # render_template (jinja2) takes dictionaries
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Seattle!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Fast and the Furious movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@flaskApp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)