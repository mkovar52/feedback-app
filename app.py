from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    # dev db
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password123@localhost/feedback'

else:
    # prod db
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# db object
db = SQLAlchemy(app)

# models


class Feedback(db.Model):
    __tablename__ = 'sales_feedback'

    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    employee = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, customer, employee, rating, comments):
        self.customer = customer
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
        employee = request.form['employee']
        rating = request.form['rating']
        comments = request.form['comments']
        # -- confirm form data
        # print(customer, employee, rating, comments)

        if customer == '' or employee == '':
            return render_template('index.html', message='Please enter required fields')

    return render_template('success.html')


if __name__ == '__main__':
    app.run()
