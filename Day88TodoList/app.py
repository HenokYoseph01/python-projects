from flask import Flask, render_template, redirect, url_for
from forms import TodoForm
from operator import itemgetter

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yoursecretkey'

todos = []


@app.route('/', methods=['GET', 'POST'])
def index():
    form = TodoForm()
    if form.validate_on_submit():
        todo = {
            'task': form.task.data,
            'priority': form.priority.data
        }
        todos.append(todo)
        todos.sort(key=itemgetter('priority'))  # Sort tasks by priority
        return redirect(url_for('index'))

    return render_template('index.html', form=form, todos=todos)


@app.route('/delete/<int:index>')
def delete(index):
    del todos[index]
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
