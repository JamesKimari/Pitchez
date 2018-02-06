from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, RadioField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField('Pitch Title', validators=[Required()])
    category = RadioField('Pick Category', choices=[('Pickup Lines', 'Pickup Lines'), ('Interview Pitch', 'Interview Pitch'), ('Product Pitch', 'Product Pitch'), ('Promotion Pitch', 'Promotion Pitch')], validators=[Required()])
    author = StringField('Authors name', validators=[Required()])
    pitch_content = TextAreaField('Write Pitch', validators=[Required()])    
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Say something about yourself...', validators = [Required()])
    submit = SubmitField('Submit')