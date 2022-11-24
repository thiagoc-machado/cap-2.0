from flask import Flask, render_template, redirect, url_for, request
from quiz import perg

app = Flask(__name__)
app.config.from_object(__name__)



@app.route('/', methods=['GET', 'POST'])
def wtf_quiz():
    p = perg()
    res = p[7]
    if request.method == "POST":
        resp = request.form["submit_button"]
        print(res)
        if "RESPUESTA: " + resp == res:
            return redirect(url_for('passed'))
    else:
        pass

    return render_template('quiz.html',text='txt', perg=p[2],alt1=p[3],alt2=p[4],alt3=p[5],alt4=p[6])

@app.route('/passed')
def passed():
    return render_template('passed.html')

@app.route('/passed')
def passed():
    return render_template('passed.html')

@app.route('/quiz')
def quiz():
#    form = PopQuiz()
    return render_template('quiz.html')


if __name__ == '__main__':
#    from waitress import serve
#    serve(app, host="127.0.0.1", port=8080)
    app.run(debug=True)