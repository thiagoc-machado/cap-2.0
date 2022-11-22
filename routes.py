from flask import Flask, render_template, redirect, url_for
from quiz import PopQuiz, p

SECRET_KEY = 'this is a secret key'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods=['GET', 'POST'])
def wtf_quiz():
    form = PopQuiz()
    if form.validate_on_submit():
        print(p.per)
        return redirect(url_for('passed'))
    return render_template('quiz.html', form=form)

@app.route('/passed')
def passed():
    return render_template('passed.html')

@app.route('/err')
def err():
    return render_template('err.html')


if __name__ == '__main__':
#    from waitress import serve
#    serve(app, host="127.0.0.1", port=8080)
    app.run(debug=True)