from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class Forms(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    image = FileField('Your image', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Upload')
