#!/usr/bin/env python

from flask import Flask, render_template, redirect, url_for
from flask_wtf import Form
from wtforms.fields import RadioField, SubmitField
from guess import Guess

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
game = Guess('Python')
game.expand('Python', 'C++', 'Is it compiled?', True)
game.expand('C++', 'Java', 'Does it run on a VM?', True)


class YesNoQuestionForm(Form):
    answer = RadioField('Your answer', choices=[('yes', 'Yes'), ('no', 'No')])
    submit = SubmitField('Submit')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/question/<int:id>', methods=['GET', 'POST'])
def question(id):
    if game.get_guess(id) is not None:
        return redirect(url_for('guess', id=id))
    form = YesNoQuestionForm()
    if form.validate_on_submit():
        new_id = game.answer_question(form.answer.data == 'yes', id)
        return redirect(url_for('question', id=new_id))
    return render_template('question.html', question=game.get_question(id),
                           form=form)


@app.route('/guess/<int:id>')
def guess(id):
    return render_template('guess.html', guess=game.get_guess(id))


if __name__ == '__main__':
    app.run(debug=True)
