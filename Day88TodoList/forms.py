from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    task = StringField('Task', validators=[DataRequired()])
    priority = SelectField('Priority', choices=[('1', 'High'), ('2', 'Medium'), ('3', 'Low')], validators=[DataRequired()])
    submit = SubmitField('Add Task')
