import os

# ########### JUST TO PLAY AROUND ###########:
# Google Coding Interview With A Facebook Software Engineer.
# LINK: https://www.youtube.com/watch?v=PIeiiceWe_w&t=723s&ab_channel=Cl%C3%A9mentMihailescu

# AVISO: EU SEI QUE NÃO ESTÁ PERFEITO. MAS, FOI APENAS PRA EU ME DIVERTIR UM POUCO.
# POIS, QUANDO EU ESTAVA ASSISTINDO O VÍDEO DO LINK ACIMA, EU ME EMPOUGUEI EU SENTI QUE
# EU TALVEZ CONSEGURIA FAZER O QUE O FOI PEDIDO NO VÍDEO OU TALVEZ EU CONSEGURIA FAZER ALGO PARECIDO.
# ENTÃO, EU PALSEI O VÍDEO ANTES QUE O "SecondThread" COMEÇASSE A RESOLVER O PROBLEMA. HAHAHAH.


um = []
dois = ['a', 'b', 'c', ]
tres = ['d', 'e', 'f']
quatro = ['g', 'h', 'i']
cinco = ['j', 'k', 'l']
seis = ['m', 'n', 'o']
sete = ['p', 'q', 'r', 's']
oito = ['t', 'u', 'v']
nove = ['w', 'x', 'y', 'z']
teclado = [um, dois, tres, quatro, cinco, seis, sete, oito, nove]

# Cat = c, a, t
# print(teclado[1][2], teclado[1][0], teclado[7][0])

palavra_escolhida = 'flowers'

# Teste apena um de cada vez:

# palavra_escolhida = 'foo'
# palavra_escolhida = 'bar'
# palavra_escolhida = 'baz'
# palavra_escolhida = 'foobar'
# palavra_escolhida = 'emo'
# palavra_escolhida = 'cap'
# palavra_escolhida = 'car'
# palavra_escolhida = 'cat'


converter_para_numero_teclado = []
add = []

for letra in palavra_escolhida:
    indice_0 = -1
    indice_1 = -1
    indice_2 = -1
    indice_3 = -1
    indice_4 = -1
    indice_5 = -1
    indice_6 = -1
    indice_7 = -1
    indice_8 = -1

    for letra_do_Teclado in teclado[0]:
        indice_0 += 1
        if letra == letra_do_Teclado:
            add.append(indice_0)
            converter_para_numero_teclado.append(2)

    for letra_do_Teclado in teclado[1]:
        indice_1 += 1
        if letra == letra_do_Teclado:
            add.append(indice_1)
            converter_para_numero_teclado.append(2)

    for letra_do_Teclado in teclado[2]:
        indice_2 += 1
        if letra == letra_do_Teclado:
            add.append(indice_2)
            converter_para_numero_teclado.append(3)

    for letra_do_Teclado in teclado[3]:
        indice_3 += 1
        if letra == letra_do_Teclado:
            add.append(indice_3)
            converter_para_numero_teclado.append(4)

    for letra_do_Teclado in teclado[4]:
        indice_4 += 1
        if letra == letra_do_Teclado:
            add.append(indice_4)
            converter_para_numero_teclado.append(5)

    for letra_do_Teclado in teclado[5]:
        indice_5 += 1
        if letra == letra_do_Teclado:
            add.append(indice_5)
            converter_para_numero_teclado.append(6)

    for letra_do_Teclado in teclado[6]:
        indice_6 += 1
        if letra == letra_do_Teclado:
            add.append(indice_6)
            converter_para_numero_teclado.append(7)

    for letra_do_Teclado in teclado[7]:
        indice_7 += 1
        if letra == letra_do_Teclado:
            add.append(indice_7)
            converter_para_numero_teclado.append(8)

    for letra_do_Teclado in teclado[8]:
        indice_8 += 1
        if letra == letra_do_Teclado:
            add.append(indice_8)
            converter_para_numero_teclado.append(9)

converter_para_str = []
for numero in converter_para_numero_teclado:
    converter_para_str.append(str(numero))

os.system('cls') or None
print(f'A palavra é: {palavra_escolhida}')
print('A palavra em ordem de número de telefone é: ' + ''.join(converter_para_str))
