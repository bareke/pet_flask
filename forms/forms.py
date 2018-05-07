from wtforms import Form, StringField, TextField, validators, HiddenField


# Create your forms

class PetForm(Form):
    name = StringField('Name', [validators.Required(message = 'Required name.'),
                                validators.Length(min = 3, max = 25, message = 'Enter a valid name.'),
                                ])
    type_pet = StringField('Type pet', [validators.Required(message = 'Required race.'), ])
    age = StringField('Age', [validators.Required(message = 'Required age.'), ])
    owner = StringField('Owner', [validators.Required(message = 'Required owner.'), ])
    honeypot = HiddenField('', [validators.Length(min = 0, max = 0)])

class OwnerForm(Form):
    owner = StringField('Owner', [validators.Required(message = 'Required owner.')])
