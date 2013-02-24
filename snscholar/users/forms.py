from flask.ext.wtf import Form, TextField, SubmitField, validators

class UserAccessForm(Form):
    firstname = TextField('First Name', [validators.Required()])
    lastname = TextField('Last Name', [validators.Required()])
    submit = SubmitField('Request Access')

