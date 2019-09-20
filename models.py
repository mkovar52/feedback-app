# from __init__ import db, login_manager
# from flask_bcrypt import Bcrypt
# from flask_login import UserMixin

# bcrypt = Bcrypt()


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)


# class User(db.Model, UserMixin):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(64), unique=True, index=True)
#     password_hash = db.Column(db.String(128))

#     def __init__(self, email, password):
#         self.email = email
#         self.password_hash = bcrypt.generate_password_hash(password=password)

#     def check_password(self, password):
#         return bcrypt.check_password_hash(self.password_hash, password)


# class Feedback(db.Model):
#     __tablename__ = 'sales_feedback'

#     id = db.Column(db.Integer, primary_key=True)
#     customer = db.Column(db.String(200))
#     order_number = db.Column(db.Integer, unique=True)
#     employee = db.Column(db.String(200))
#     rating = db.Column(db.Integer)
#     comments = db.Column(db.Text())

#     def __init__(self, customer, order_number, employee, rating, comments):
#         self.customer = customer
#         self.order_number = order_number
#         self.employee = employee
#         self.rating = rating
#         self.comments = comments
