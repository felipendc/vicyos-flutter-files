import os

dois = ['a', 'b', 'c', ]
tres = ['d', 'e', 'f']
quatro = ['g', 'h', 'i']
cinco = ['j', 'k', 'l']
seis = ['m', 'n', 'o']
sete = ['p', 'q', 'r', 's']
oito = ['t', 'u', 'v']
nove = ['w', 'x', 'y', 'z']

palavra_escolhida = 'flowers'

letras_encontradas = []
for letra in palavra_escolhida:
    for elemento in (dois, tres, quatro, cinco, seis, sete, oito, nove):
        if elemento in tres:
            letras_encontradas.append(tres.index(letra))
print(letras_encontradas)
