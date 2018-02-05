from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField('Pitch Title', validators=[Required()])
    category = StringField('Pitch category', validators=[Required()])
    pitch_content = TextAreaField('Write Pitch', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Say something about you...', validators = [Required()])
    submit = SubmitField('Submit')