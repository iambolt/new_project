from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from myflask.models import User

class Register(FlaskForm):
    usrname = StringField('Username',validators=[DataRequired(), Length(min=3,max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign up')

    def validate_usrname(self,usrname):

        user = User.query.filter_by(username=usrname.data).first()
        if user:
            raise ValidationError('Username already taken')

    def validate_email(self,email):
    
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already registered')        


class Login(FlaskForm):
    usrname = StringField('Username',validators=[DataRequired(), Length(min=3,max=20)])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me =BooleanField('Remember me')
    submit = SubmitField('Login up')


class PostForm(FlaskForm):
    title =StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')