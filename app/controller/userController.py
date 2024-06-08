import re
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.base import db
from app.models.user import User
from itsdangerous import SignatureExpired
from flask_mail import Message

userBP = Blueprint('user', __name__)


@userBP.route('/register', methods=['GET', 'POST'])
def register():
    from ourwork import mail, s

    if request.method == 'POST':
        email = request.form['email']
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already registered.')
            return redirect(url_for('user.register'))

        token = s.dumps(email, salt='email-confirm')
        msg = Message('Confirm Email', recipients=[email])
        link = url_for('user.confirm_email', token=token, _external=True)
        print(link)
        msg.body = 'Your link to complete registration is: {}'.format(link)
        mail.send(msg)

        return render_template('registration_pending.html', email=email)
    return render_template('register.html')


@userBP.route('/confirm_email/<token>')
def confirm_email(token):
    from ourwork import s

    try:
        email = s.loads(token, salt='email-confirm', max_age=3600)
    except SignatureExpired:
        return '<h1>The confirmation link is expired!</h1>'
    return render_template('set_password.html', email=email, token=token)


@userBP.route('/set_password', methods=['POST'])
def set_password():
    from ourwork import s

    email = request.form['email']
    token = request.form['token']
    password = request.form['password']
    password_confirm = request.form['password_confirm']

    # Check if passwords match
    if password != password_confirm:
        flash('Passwords do not match.')
        return redirect(url_for('user.set_password', token=token, email=email))

    # Check password length
    if len(password) < 8:
        flash('Password must be at least 8 characters long.')
        return redirect(url_for('user.set_password', token=token, email=email))

    try:
        email_verified = s.loads(token, salt='email-confirm', max_age=3600)
        if email != email_verified:
            raise Exception('Email verification failed.', 'error')
    except SignatureExpired:
        flash('The confirmation link is expired.', 'error')
        return redirect(url_for('user.register'))

    # Determine user type
    student_pattern = r'@mail\.uic\.edu\.cn$'
    teacher_pattern = r'@uic\.edu\.cn$'
    if re.search(student_pattern, email):
        utype = 'Student'
    elif re.search(teacher_pattern, email):
        utype = 'Teacher'
    else:
        flash('Invalid email domain.', 'error')
        return redirect(url_for('user.register'))

    # Check if user already exists
    user = User.query.filter_by(email=email).first()
    if user:
        flash('Email already registered.', 'error')
        return redirect(url_for('user.login'))

    # Create new user
    user = User(email=email, password=password, utype=utype)
    db.session.add(user)
    db.session.commit()

    flash('Your account has been created successfully. Please log in.', 'success')
    return redirect(url_for('user.login'))


@userBP.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('user.homepage'))
        else:
            flash('Invalid email or password', 'error')
    return render_template('login.html')


@userBP.route('/homepage')
@login_required
def homepage():
    if current_user.utype == 'Teacher':
        return redirect(url_for('search.search'))
    elif current_user.utype == 'Admin':
        return redirect(url_for('request.view_requests'))
    elif current_user.utype == 'Student':
        return redirect(url_for('topic.topicsearch'))
    else:
        return redirect(url_for('user.login'))


@userBP.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.login'))
