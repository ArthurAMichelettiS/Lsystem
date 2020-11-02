
#t.width(lv)

'''t.penup()
t.bk(l)
t.pendown()
t.fd(l)
'''



'''
alfabeto: E, D, C, L, x
inicio: ECxLD
regras: L > ECDC
        C > EEx
        x > ELD

E - virar a esquerda 20°
D - virar a direita 20°
C - andar pra frente 10px
L - andar pra frente 30px
x - nada, para regra de produção
'''

txt = open("gramatica.txt", "r+")

entrada = txt.readlines()
txt.close()

palavraIni = [ch for ch in entrada[0]]
qtdLoop = int(entrada[1])

regras = {val.split(">")[0]: val.split(">")[1][:-1] for val in entrada[2:]}

palavraAtual = [ch for ch in palavraIni]
for i in range(qtdLoop):
    novaPalavra = []
    for j in range(len(palavraAtual)):
        if regras.keys().__contains__(palavraAtual[j]):
            novaPalavra.extend([ch for ch in regras[palavraAtual[j]]])

    palavraAtual = novaPalavra

print("".join(novaPalavra))



lv = 5
l = 120

lC = 20
lL = 50
curva = 45

import math
# escrever svg

tam = 1200

pontoAtual = [tam//2, tam//2]
anguloAtual = -90
passoAtual = lC
saidaTxt = f'''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN"
"http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">
<svg height="{tam}" width="{tam}" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve">
<polyline points="
'''

for mov in novaPalavra:
    if mov == "E":
        anguloAtual -= curva
    elif mov == "D":
        anguloAtual += curva
    elif mov == "C":
        passoAtual = lC

        novoPonto = [pontoAtual[0] + passoAtual * math.cos(math.radians(anguloAtual)),
                     pontoAtual[1] + passoAtual * math.sin(math.radians(anguloAtual))]
        saidaTxt += f'{novoPonto[0]},{novoPonto[1]} '
        pontoAtual = [novoPonto[0], novoPonto[1]]
    elif mov == "L":
        passoAtual = lL

        novoPonto = [pontoAtual[0] + passoAtual * math.cos(math.radians(anguloAtual)),
                     pontoAtual[1] + passoAtual * math.sin(math.radians(anguloAtual))]
        saidaTxt += f'{novoPonto[0]},{novoPonto[1]} '
        pontoAtual = [novoPonto[0], novoPonto[1]]


saidaTxt += '"  style="fill:white;stroke:rgb(255,0,0);stroke-width:3" /></svg>'

saida = open("imagem.svg", "w")

saida.write(saidaTxt)
saida.close()
