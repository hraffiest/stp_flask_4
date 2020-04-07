from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, Email, InputRequired


class SignUpForm(FlaskForm):
    username = StringField('Ваше имя',
                           [Length(min=4, max=25, message='Ваше имя должно быть в пределах от 4-х до 25-ти символов'),
                            InputRequired(message='Поле Ваше имя обязательно для заполнения')])
    email = StringField('Ваш email',
                        [Length(min=4, max=25, message='Ваше имя должно быть в пределах от 4-х до 25-ти символов'),
                         InputRequired(message='Поле Ваше имя обязательно для заполнения'),
                         Email(message='Email введен неверно')])
    password = PasswordField('Пароль',
                             [Length(min=8, max=25, message='Ваш пароль должно быть в пределах от 8 до 25-ти символов'),
                              InputRequired(message='Поле Пароль обязательно для заполнения'),
                              EqualTo('password_equal', message='Пароли не совпадают')])
    password_equal = PasswordField('Повторите пароль')


class LoginForm(FlaskForm):
    email = StringField('Ваш email',
                           [Length(min=4, max=25, message='Ваше имя должно быть в пределах от 4-х до 25-ти символов'),
                            InputRequired(message='Поле Ваше имя обязательно для заполнения'),
                            Email(message='Email введен неверно')])
    password = PasswordField('Пароль',
                             [Length(min=8, max=25, message='Пароль не верный'),
                              InputRequired(message='Поле Пароль обязательно для заполнения')])

    remember = BooleanField('Запомнить меня', default=False)
