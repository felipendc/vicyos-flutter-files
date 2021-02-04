# Password Generator Project
import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
          'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Bem vindo ao Gerador de Senha Py!")
nr_letras = int(input("Quantas letras você quer na sua senha??\n"))
# nr_simbolos = int(input(f"Quantos simbolos você quer adicionar??\n"))
# nr_numeros = int(input(f"Quantos números você quer adicionar??\n"))

letras_aleatorias_geradas = []


for letras in range(1, nr_letras):

    qualquer_letra = random.randint(1, 4)
    letras_aleatorias_geradas.append(letras[qualquer_letra])
    print(letras_aleatorias_geradas)

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
