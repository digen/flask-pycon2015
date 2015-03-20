#!/usr/bin/env python

from flask import Flask, render_template

app = Flask(__name__)
questions = ['Is it compiled?', 'Does it run on a VM?']
guesses = ['Python', 'Java', 'C++']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/question/<int:id>')
def question(id):
    return render_template('question.html', question=questions[id])


@app.route('/guess/<int:id>')
def guess(id):
    return render_template('guess.html', guess=guesses[id])


if __name__ == '__main__':
    app.run(debug=True)
