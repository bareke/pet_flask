from wtforms import Form, StringField, TextField
from wtforms import HiddenField, IntegerField, BooleanField
from wtforms.validators import Required, Length, DataRequired, Email
from wtforms.fields.html5 import EmailField

# Create your forms

class BaseForm(Form):
    """ Mitiga formaularios basura """
    honeypot = HiddenField('', validators=[Length(min = 0, max = 0)])


class PersonForm(Form):
    name_person = StringField(
                            'Name',
                            validators=[DataRequired(message = 'Required name'),
                                        Length(min = 3, max = 25),
                                        ])
    last_name_person = StringField(
                            'Last name',
                            validators=[DataRequired(message = 'Required last name'),
                                        Length(min = 3, max = 25, message = 'Enter a valid last name person'),
                                        ])
    telephone_person = IntegerField(
                            'Telephone',
                            validators=[DataRequired(message = 'Required telephone'),
                                        ])
    email_person = EmailField(
                            'Email address',
                            validators=[DataRequired(message = 'Required email'),
                                        Email(message = 'Enter a valid email'),
                                        ])
    #name_person_img = StringField(validators = [Length(min = 1)])


class PetForm(Form):
    name_pet = StringField(
                            'Name pet',
                            validators=[DataRequired(message = 'Required name'),
                                        Length(min = 3, max = 25, message = 'Enter a valid name'),
                                        ])
    type_pet = StringField(
                            'Type pet',
                            validators=[DataRequired(message = 'Required name'),
                                        Length(min = 3, max = 25, message = 'Enter a valid type'),
                            ])
    age_pet = IntegerField(
                            'Age pet',
                            validators=[DataRequired('Required age'),
                                        ])
    #name_pet_img = StringField(validators = [Length(min = 1)])


class QueryPetForm(Form):
    query_type_pet = StringField(
                        'Query type pet',
                        validators=[DataRequired(message = 'Required type pet'),
                                    Length(min = 1, max = 25, message = 'Enter a valid type pet'),
                                    ])


class AdoptPetForm(Form):
    email_person = EmailField(
                            'Email address',
                            validators=[DataRequired(message = 'Required email'),
                                        Email(message = 'Enter a valid email'),
                                        ])
