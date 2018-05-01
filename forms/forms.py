from wtforms import Form, StringField, TextField, validators, HiddenField

from validations import validation_honeypot

# Create your forms

class PetForm(Form):
    name = StringField('Name', [validators.Required(message = 'Required name.'),
                                validators.Length(min = 3, max = 25, message = 'Enter a valid name.'),
                                ])
    race = StringField('Race', [validators.Required(message = 'Required race.'), ])
    age = StringField('Age', [validators.Required(message = 'Required age.'), ])
    owner = StringField('Owner', [validators.Required(message = 'Required owner.'), ])
    honeypot = HiddenField('', [validation_honeypot])

class PropertyForm(Form):
    owner = StringField('Owner', [validators.Required(message = 'Required owner.')])
