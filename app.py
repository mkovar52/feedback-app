from flask import Flask, render_template, request, url_for, flash, abort, redirect
from flask_login import login_user, login_required, logout_user
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail
from forms import LoginForm, RegistrationForm
from flask_bcrypt import Bcrypt
from flask_login import UserMixin
from flask_login import LoginManager
# from __init__ import app, db
# from models import User

login_manager = LoginManager()
bcrypt = Bcrypt()
app = Flask(__name__)

ENV = 'dev'
app.config['SECRET_KEY'] = 'mysecretkey'

if ENV == 'dev':
    # dev db
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password123@localhost/feedback'

else:
    # prod db
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://kcprcbqytevqdn:1c24fce25788278a829109e22d3290b7dc1ada958419fd2d63465ee1335d719e@ec2-54-235-92-43.compute-1.amazonaws.com:5432/d4rtjhenrda6h7'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# -- db object
db = SQLAlchemy(app)

login_manager.init_app(app)
login_manager.login_view = 'login'


###############
# -- Models
###############

class Feedback(db.Model):
    __tablename__ = 'sales_feedback'

    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200))
    order_number = db.Column(db.Integer, unique=True)
    employee = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, customer, order_number, employee, rating, comments):
        self.customer = customer
        self.order_number = order_number
        self.employee = employee
        self.rating = rating
        self.comments = comments


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, password):
        self.email = email
        self.password_hash = bcrypt.generate_password_hash(password=password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)


###############
# -- App routes
###############
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():

    if request.method == 'POST':
        customer = request.form['customer']
        order_number = request.form['orderNumber']
        employee = request.form['employee']
        rating = request.form['rating']
        comments = request.form['comments']
        # -- confirm form data
        # print(customer, order_number, employee, rating, comments)

        # -- mandatory fields cannot be empty
        if customer == '' or employee == '' or order_number == '':
            return render_template('index.html', message='Whoops! There was an error with your submission.. <br/><strong>Please enter all required fields</strong>')

        # -- add to db if order_number does not exist, else redirect and display err msg
        if db.session.query(Feedback).filter(Feedback.order_number == order_number).count() == 0:
            print('SUCCESS! save new data')
            data = Feedback(customer, order_number, employee, rating, comments)
            db.session.add(data)
            db.session.commit()

            send_mail(customer, order_number, employee, rating, comments)

            return render_template('success.html', employee=employee, rating=int(rating))

        else:
            print('duplicate order# detected, do not save!')
            return render_template('index.html', message="You've already submitted feedback for that order. Buy more paper, or makeup a new order number! <br/><br/> The people person's paper people's <strong>manager</strong>, <br/><em>-M. Scott</em>")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

    # check if password matches and user is not null
        if user.check_password_hash(form.password.data) and user is not None:
            login_user(user)
            flash("You've successully signed into your account.")

            # redirect to page that was accessed without being logged in
            next = request.args.get('next')

            if next == None or not next[0] == "/":
                next = url_for('profile')

            return redirect(next)

    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You've been logged out.")
    return redirect(url_for('index'))


@app.route('/portal')
@login_required
def emp_portal():
    return render_template('empPortal.html')


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        bcrypt = Bcrypt()
        email = request.form['email']
        password = request.form['password']
        confirm_pw = request.form['confirm_pw']

        print(email, password, confirm_pw)

        if password == '' or confirm_pw == '' or email == '':
            return render_template('register.html', message='<strong>Fields cannot be empty. Please try again.</strong>')

        if confirm_pw != password:
            return render_template('register.html', message="Passwords do not match. Please try again.")

        if "@" not in email:
            return render_template('register.html', message="Not a valid email address. Please try again.")

        # -- If user email does not exist, save as new user.
        if db.session.query(User).filter(User.email == email).count() == 0:

            print("User doesnt exist, time to hash the pw.")
            hashed_password = bcrypt.generate_password_hash(password=password)
            print(f'hashed pass:::: {hashed_password}')

            flash("Thanks for signing up! You may now sign into your account.")

            print("Saving a new user...")
            user = User(email, hashed_password)

            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))

        else:
            print('there was an error saving a user...')
            return render_template('register.html', message="Sorry, an account already exists with that email. Please try again.")

    return render_template('register.html')

    # if request.method == 'GET':
    #     return render_template('register.html')

    # if request.method == 'POST':
    # bcrypt = Bcrypt()

    # email = request.form['email']
    # password = request.form['password']
    # confirm_pw = request.form['confirm_pw']

    # print(email, password)
    # print("hashing password....")
    # hashed_password = bcrypt.generate_password_hash(password=password)

    # print(f'hashed pass:::: {hashed_password}')

    # check if pw matches hash
    # bcrypt.check_password_hash(hashed_password)

    # return render_template('register.html', email=email, password=password)

    # else:
    #     print('something went wrong....')


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
