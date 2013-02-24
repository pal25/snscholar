from flask.ext.wtf import Form, TextField, IntegerField, SelectField, SubmitField, validators

class CourseForm(Form):
    title = TextField('Course Title', [validators.Required()])
    instructor = TextField('Course Instructor')
    abbrev = TextField('Course Abbreviation', [validators.Required(), validators.Regexp(r'[A-Za-z]{3,4}')])
    abbrevnum = TextField('Course Number', [validators.Required(), validators.Regexp(r'[1-9]{1}[0-9]{2}')])
    semester = SelectField('Semester', choices=[('Spring', 'Spring'), ('Summer', 'Summer'), ('Fall', 'Fall')])
    year = IntegerField('Year', [validators.Regexp(r'[19|20|21][0-9]{2}')])
    submit = SubmitField('Add Course')