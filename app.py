from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)

ENV = 'dev'

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

# -- models


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


# -- App routes
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
        print(customer, order_number, employee, rating, comments)

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


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/portal')
def emp_portal():
    return render_template('empPortal.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
