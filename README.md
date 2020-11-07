# Lsystem

A partir de uma gramática recebida em txt, gera ao executar um arquivo SVG

# Gramática:

alfabeto: E, D, C, L, x <br />
inicio: ELCxCLD <br />
regras de produção: L > ECDC <br />
                    C > EEx <br />
                    x > ELD <br />

# Representam: <br />
E - virar a esquerda 75° <br />
D - virar a direita 75° <br />
C - andar pra frente 20px <br />
L - andar pra frente 50px <br />
x - nada, para regra de produção <br />


# Formatação da entrada: <br />
ELCxCLD   // inicio <br />
9         // numero de iterações <br />
L>CELDC   //regras de produção <br />
x>ELDDL   <br />
E>CDDCEELDD <br />

#Saida:

<img src="imagem.svg">
