from flask import Flask, render_template
from filter import perg

app = Flask(__name__)
app.config.from_object(__name__)
p = perg()
@app.route('/', methods=['GET', 'POST'])
def wtf_quiz():
    p = perg()
    return render_template('quiz.html',cod = p[0], perg = p[1], alt1 = p[2], alt2 = p[3], alt3 = p[4], alt4 = p[5], res = p[6], norma = p[7], ref = p[8], qtd = p[9])
@app.route('/quiz')
def quiz():
    return render_template('quiz.html')


if __name__ == '__main__':

    app.run(debug=True)