from flask_wtf import FlaskForm as Form
from wtforms import RadioField
from wtforms.validators import ValidationError
import linecache
import random
def perg():
    i = 0
    err = 0
    corr = 0
    sres = 0
    registro = {}
    dic = []
    index = -8
    nome = ""
    txt = "RESPUESTA:"
    name = ""

    with open("cap.txt", "r", encoding="utf8") as arquivo:
        cap = arquivo.readlines()
        for linha in cap:
            index += 1
            linha = linha.strip('\n')
            if nome == "":
                if txt in linha.split():
                    nome = linha
            else:
                registro[0] = (linecache.getline("C://Users/thiag/PycharmProjects/cop/cap.txt", index)).replace(
                        "\n", "")
                registro[1] = (linecache.getline("C://Users/thiag/PycharmProjects/cop/cap.txt", index + 1)).replace(
                        "\n", "")
                registro[2] = (linecache.getline("C://Users/thiag/PycharmProjects/cop/cap.txt", index + 3)).replace(
                        "\n", "")
                registro[3] = (linecache.getline("C://Users/thiag/PycharmProjects/cop/cap.txt", index + 4)).replace(
                        "\n", "")
                registro[4] = (linecache.getline("C://Users/thiag/PycharmProjects/cop/cap.txt", index + 5)).replace(
                        "\n", "")
                registro[5] = (linecache.getline("C://Users/thiag/PycharmProjects/cop/cap.txt", index + 6)).replace(
                        "\n", "")
                registro[6] = (linecache.getline("C://Users/thiag/PycharmProjects/cop/cap.txt", index + 7)).replace(
                        "\n", "")
                dic.append(registro)
                nome = ""
                registro = {}

    qtd = (len(dic))
    nperg = random.randrange(qtd)

    cod = dic[nperg][0]
    per = dic[nperg][1]
    alt1 = dic[nperg][2]
    alt2 = dic[nperg][3]
    alt3 = dic[nperg][4]
    alt4 = dic[nperg][5]
    res = dic[nperg][6]
    resp = "RESPUESTA: " + name
    tst2 = dic[nperg][6]
    if resp == dic[nperg][6]:
        resul = "Correcto"
        corr += 1

    if resp == "RESPUESTA: NA":
        resul = "Sin respuesta"
        sres += 1

    else:
        resul = "Errado"
        err += 1

    toterr = err
    totcorr = corr
    semres = sres
    return name, cod, per, alt1, alt2, alt3, alt4,res, qtd, resul, err, resp, tst2
name, cod, per, alt1, alt2, alt3, alt4,res, qtd, resul, err, resp, tst2 = perg()

class CorrectAnswer(object):
    def __init__(self, answer):
        self.answer = answer
    def __call__(self, form, field):
        message = 'Incorrect answer.'

        if field.data != self.answer:
            raise ValidationError(message)

#class PopQuiz(Form):
#    q1 = RadioField(
#
#        per,
#       choices=[('RESPUESTA: A', alt1), ('RESPUESTA: B', alt2),('RESPUESTA: C', alt3),('RESPUESTA: D', alt4)],
#        validators=[CorrectAnswer(res)]
#        )



