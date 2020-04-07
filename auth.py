from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user
from __init__ import db
from models import *
from forms import *
auth = Blueprint('auth', __name__)


@auth.route('/login/', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = db.session.query(User).filter(User.mail == form.email.data).first()
            if user and user.password_valid(form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('main.profile'))
            else:
                form.errors['reg'] = ['Неправильный email или пароль']
                return render_template('login.html', form=form)
        else:
            return render_template('login.html', form=form)
    else:
        return render_template('login.html', form=form)


@auth.route('/signup/', methods=['POST', 'GET'])
def signup():
    form = SignUpForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = db.session.query(User).filter(User.mail == form.email.data).first()
            if not user:
                user = User(name=form.username.data,
                            mail=form.email.data,
                            password=form.password.data)
                db.session.add(user)
                db.session.commit()
                return redirect('/login/')
            else:
                form.errors['reg'] = ['Пользователь с таким email уже существует']
                return render_template('signup.html', form=form)
        else:
            return render_template('signup.html', form=form)
    else:
        return render_template('signup.html', form=form)


@auth.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
