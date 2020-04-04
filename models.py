from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    u_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    mail = db.Column(db.String, nullable=False)
    _password = db.Column(db.String, nullable=False)

    @property
    def password(self):
        raise AttributeError('Не лезь к паролю')

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    def password_valid(self, password):
        return check_password_hash(self._password, password)


class Group(db.Model):
    __tablename__ = 'groups'
    g_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    course = db.Column(db.String, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    applicants = db.relationship('Applicant', back_populates='group')
    seat = db.Column(db.Integer, nullable=False)


class Applicant(db.Model):
    __tablename__ = 'applicants'
    a_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    mail = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.g_id'))
    group = db.relationship('Group', back_populates='applicants')


