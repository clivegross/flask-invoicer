from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Email

class LoginForm(Form):
    email = StringField('email', validators=[Email()])
    remember_me = BooleanField('remember_me', default=False)

