from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    '''Form to add pets to database'''

    name = StringField('Pet Name', validators=[InputRequired()],)
    species = SelectField('Species', choices=[('cat', 'Cat'),('dog', 'Dog'), ('bird', 'Bird'), ('rabbit', 'Rabbit')],)
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField('Age in years', validators=[Optional(), NumberRange(min=0, max=25)])
    notes = TextAreaField('Notes', validators=[Optional(), Length(min=10)])

class EditPetForm(FlaskForm):
    '''Form for editing a pets photo, age, notes and availability'''

    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField('Age in years', validators=[Optional(), NumberRange(min=0, max=25)])
    notes = TextAreaField('Notes', validators=[Optional(), Length(min=10)])
    available = BooleanField('Adopted?')
