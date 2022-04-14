from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class AddForm(FlaskForm):
    name = StringField('Country Name', validators=[DataRequired()])
    submit = SubmitField('Submit')