from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, TextAreaField


class edittableForm(FlaskForm):
    Number = StringField("Number")
    submit = SubmitField("Edit")

class deletetableForm(FlaskForm):
    submit = SubmitField("Delete")

class deleteMenuForm(FlaskForm):
    submit = SubmitField("Delete")

class addMenuForm(FlaskForm):
    name = StringField("Name")
    price = StringField("Price")
    description = TextAreaField("Description")
    course = RadioField("Course", choices=[('appetizer', 'Appetizer'),('entree','Entree'),
        ('dessert','Dessert'),('beverage','Beverage')])
    submit = SubmitField("Add")

class editMenuForm(FlaskForm):
    name = StringField("Name")
    price = StringField("Price")
    description = TextAreaField("Description")
    course = RadioField("Course", choices=[('appetizer', 'Appetizer'),('entree','Entree'),
        ('dessert','Dessert'),('beverage','Beverage')])
    submit = SubmitField("Edit")