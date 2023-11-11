from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
db = SQLAlchemy()

metadata = db.metadata

# ревизия где есть юзер и ролс
# alembic downgrade
# юзер и ролс
# туры и бронь
# downgrade 


# наследуем UserMixin (flask_login())
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(300), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    role = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)

class Roles(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    users = db.relationship('User', backref='user', lazy=True, cascade="all, delete-orphan")

class Tours(db.Model):
    __tablename__ = 'tours' 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    reservation = db.relationship('Reservation', backref='tour', uselist=False, cascade="all, delete-orphan", )

class Reservation(db.Model):
    __tablename__ = 'reservations'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    status = db.Column(db.String(50))
    payment_status = db.Column(db.String(50))
    tour_id = db.Column(db.Integer, db.ForeignKey('tours.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)