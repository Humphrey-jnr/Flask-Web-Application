from sqlalchemy.orm import session
from files import app
from flask import render_template,redirect,url_for,flash
from files.models import Item,user
from files.forms import RegisterForm
from files import db

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/profile')
def profile_page():
    items= Item.query.all()
    return render_template('profile.html',items=items)

@app.route('/register',methods=['GET','POST'])
def register_page():
    form=RegisterForm()
    if form.validate_on_submit():
        user_to_create=user(username=form.username.data,
                email_address=form.email_address.data,
                password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))

    if form.errors!={}:
        for err_msg in form.errors.values():
            flash(f'There was an Error {err_msg}',category='danger')

    return render_template('register.html',form=form)
  