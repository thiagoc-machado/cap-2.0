import random

def perg():

    with open("cap_scrap.txt", "r", encoding="utf8") as arquivo:
        dic = []
        nome = []
        txt = "COD:"
        count = 13
        cap = arquivo.readlines()
        for linha in cap:
            if txt in linha.split():
                nome.append(linha)
                count = 0
            if count < 13:
                if count > 0 and count != 2 and count != 4 and count != 6 and count != 8:
                    nome.append(linha)
                count += 1
            if count == 13:
                dic.append(nome)
                nome = []
                count = + 1

        qtd = (len(dic))
        nperg = random.randrange(qtd)

        cod = dic[nperg][0]
        per = dic[nperg][1]
        alt1 = dic[nperg][2]
        alt2 = dic[nperg][3]
        alt3 = dic[nperg][4]
        alt4 = dic[nperg][5]
        res = dic[nperg][6]
        norma = dic[nperg][7]
        ref = dic[nperg][8]
        print(dic[nperg])
        return cod, per, alt1, alt2, alt3, alt4, res, norma, ref, qtd
cod, per, alt1, alt2, alt3, alt4, res, norma, ref, qtd = perg()

