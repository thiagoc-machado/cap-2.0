from flask import Flask, render_template, redirect, url_for, request
from quiz import perg

app = Flask(__name__)
app.config.from_object(__name__)
i = 1
p = perg()
res = p[7]
cor = 0
er = 0
sn = 0
print(p)
@app.route('/', methods=['GET', 'POST'])
def wtf_quiz():
    global p
    global res
    global cor
    global er
    global sn
    print("Corretas:")
    print(cor)
    print("Erradas")
    print(er)
    print("sem responder")
    print(sn)
    print(p)
    i = 0
    if request.method == "POST":
        resp = request.form["submit_button"]
        print(res)
        if "RESPUESTA: " + resp == res:
            p = perg()
            res = p[7]
            if i == 0:
                cor += 1
                i += 1
                print("Corretaaaaaa")
            return redirect(url_for('passed'))
        if resp == "No Responder":
            if i == 0:
                i =+ 1
                sn +=1
            p = perg()
            txt = ""
        if "RESPUESTA: " + resp != res:
            if i == 0:
                i = + 1
                er += 1
                print("Erradadadadadda")
            pass
    return render_template('quiz.html',text='txt',perg=p[2],alt1=p[3],alt2=p[4],alt3=p[5],alt4=p[6],cor=cor, er=er,sn=sn)

@app.route('/passed')
def passed():
    return render_template('passed.html')

@app.route('/err')
def err():
    return render_template('err.html')

@app.route('/quiz')
def quiz():
#    form = PopQuiz()
    return render_template('quiz.html')


if __name__ == '__main__':
#    from waitress import serve
#    serve(app, host="127.0.0.1", port=8080)
    app.run(debug=True)