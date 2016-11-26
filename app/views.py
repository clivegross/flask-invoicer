from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', mail_port=app.config['MAIL_PORT'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for email="%s", remember_me=%s' %
              (form.email.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template(
        'login.html',
        form=form
    )
