from flask import Flask, render_template, redirect, url_for
from quiz import PopQuiz


SECRET_KEY = 'this is a secret key'

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/', methods=['GET', 'POST'])
def wtf_quiz():
    form = PopQuiz()
    if form.validate_on_submit():
        return redirect(url_for('passed'))
    return render_template('quiz.html', form=form)


@app.route('/passed')
def passed():
    return render_template('passed.html')


if __name__ == '__main__':
    app.run(debug=True)