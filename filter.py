import random


def perg(sec_perg):
        with open("scrapper/"+sec_perg, "r", encoding="utf8") as arquivo:
            dic = []
            nome = []
            txt = "COD:"                    #palavra a ser buscada
            count = 14                      #inicializa contador pra não gravar o primeiro registro
            cap = arquivo.readlines()
            print(arquivo.readlines())
            for linha in cap:
                if txt in linha.split():    #palavra buscada esta na linha do texto?
                    nome.append(linha)      #seleciona a linha no texto
                    count = 0
                if count < 9:               #se o contador for menos que 9 que a quantidades de linhas do bloco
                    if count > 0:           #evita que entre na primeira vez pra não repetir o primeiro registro
                        nome.append(linha)  #adiciona a linha ao bloco
                    count += 1
                if count == 9:              #se contador = 9 grava as linhas no dicionario
                    dic.append(nome)
                    nome = []               #zera a variavel que continha as linhas
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
            # print(dic[nperg])
            # print(res)
            print(qtd)
        return cod, per, alt1, alt2, alt3, alt4, res, norma, ref, qtd
#cod, per, alt1, alt2, alt3, alt4, res, norma, ref, qtd = perg()



