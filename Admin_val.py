from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo, Email
import email_validator

class Signform(FlaskForm):
    username = StringField('User name:', validators=[DataRequired(message='Please enter your email address'),
                                                     Email(message='Invalid email address')])
    password = PasswordField('Password:', validators=[DataRequired(message='Please enter your password')])
    confirm = PasswordField('Re-enter password:', validators=[DataRequired(message='Please enter your password'),
                                                              EqualTo('password',
                                                                      message='Please match your password')])
    signup = SubmitField('Signup')


class Loginform(FlaskForm):
    username = StringField('User name:', validators=[DataRequired(message='Please enter your email address'),
                                                     Email(message='Invalid email address')])
    password = PasswordField('Password:', validators=[DataRequired(message='Please enter your password')])
    login = SubmitField('Login')
