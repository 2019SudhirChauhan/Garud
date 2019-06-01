from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms_components import TimeField
#from wtforms.fields import DateField
from wtforms.fields.html5 import DateField

class StaticPredicFrom(FlaskForm):
	Date = DateField("Date", format="%m/%d/%y")
	Time = TimeField("Enter Time", format="%H:%M:%S")
	Submit = SubmitField("Get Traffic")
