from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required, Email, EqualTo


class ProfileForm(FlaskForm):
    teamname = StringField('Team Name',validators=[Required()])
    description = TextAreaField('Brief Description', validators = [Required()])
    email = StringField('Your Email Address', validators=[Required(), Email()])
    vision = StringField('Team Vision',validators = [Required()])
    mission = TextAreaField('Team Mission',validators = [Required()])
    members = TextAreaField('Add Team Members',validators = [Required()])
    location = StringField('Where are you located',validators = [Required()])
    support = TextAreaField('Support Needed', validators = [Required()])
    submit = SubmitField('Submit')

class CoachForm(FlaskForm):
    name = StringField('Name',validators=[Required()])
    support_to_provide = TextAreaField('Support to Provide',validators = [Required()])
    description = TextAreaField('What You Want', validators=[Required()])
    submit = SubmitField('Submit')