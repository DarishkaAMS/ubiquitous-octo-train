from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from Market.models import User


class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check).first()
        if user:
            raise ValidationError('This username is already booked! Please try a different one')

    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password_1 = PasswordField(label='Password:', validators=[Length(min=8), DataRequired()])
    password_2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password_1'), DataRequired()])
    submit = SubmitField(label='Create Account')
