from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo
from wtforms.fields.html5 import DateTimeLocalField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_login import current_user
from models import Workplace

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class WorkplaceForm(FlaskForm):
    name = StringField('Nazwa', validators=[DataRequired()])
    address = StringField('Adres')
    submit = SubmitField('Dodaj')

class EventForm(FlaskForm):
    start_time = DateTimeLocalField('Start Time', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    end_time = DateTimeLocalField('End Time', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    workplace = QuerySelectField('Workplace', query_factory=lambda: Workplace.query.filter_by(user_id=current_user.id), allow_blank=False, get_label='name')
    submit = SubmitField('Add Event')

class ManageUserForm(FlaskForm):
    role = SelectField('Role', choices=[('Guest', 'Guest'), ('Admin', 'Admin'), ('User', 'User')])
