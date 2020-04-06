from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required, current_user
from flask_security.utils import encrypt_password

db = SQLAlchemy()

roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.u_id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.r_id'))
)


class Role(db.Model, RoleMixin):
    r_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    u_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    mail = db.Column(db.String(255), nullable=False, unique=True)
    _password = db.Column(db.String(255), nullable=False)
    roles = db.relationship('Role', secondary=roles_users,
                            back_populates='users')

    def __str__(self):
        return self.email

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


