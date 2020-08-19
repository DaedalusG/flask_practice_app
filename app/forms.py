from flask_wtf import FlaskForm
from wtforms.fields import (
    BooleanField, DateField, StringField, SubmitField, TextAreaField, TimeField
)
from wtforms.validators import DataRequired
from wtforms.widgets.html5 import (
    DateInput, TimeInput
)


class AppointmentForm(FlaskForm):
    name = StringField('Name')
    start_date = DateField("Start date", [DataRequired()], widget=DateInput())
    start_time = TimeField("Start Time", [DataRequired()], widget=TimeInput())
    end_date = DateField("End date", [DataRequired()], widget=DateInput())
    end_time = TimeField("End time", [DataRequired()], widget=TimeInput())
    description = TextAreaField("Description")
    private = BooleanField("Private")
    submit = SubmitField("Create an appointment")