from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    pitch = TextAreaField('Write Pitch', validators=[Required()])
    submit = SubmitField('Submit')