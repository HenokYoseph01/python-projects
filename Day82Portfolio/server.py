from flask import Flask, render_template,url_for, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Message')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'portfolioKey201'

# Sample list of projects
projects = [
    {
        'title': 'Portfolio Website',
        'description': 'A personal portfolio to showcase my work and skills.',
        'link': 'https://github.com/yourusername/portfolio'
    },
    {
        'title': 'Task Manager App',
        'description': 'A web-based app for managing tasks and to-dos efficiently.',
        'link': 'https://github.com/yourusername/task-manager'
    },
    {
        'title': 'E-commerce Store',
        'description': 'An online store for selling products with payment gateway integration.',
        'link': 'https://github.com/yourusername/e-commerce-store'
    },
    # Add more projects here...
]

@app.route('/')
def portfolio():
    form = ContactForm()
    if form.validate_on_submit():
        flash(f"Message from {form.name.data} received!", 'success')
        return redirect(url_for('portfolio'))
    return render_template('portfolio.html', form=form,projects=projects)

if __name__ == "__main__":
    app.run(debug=True)
