from wtforms import validators

# Create your validations to the forms

def validation_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('The field must be empty.')
