# Password Generator Project
import random
# 0
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
          'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# 1
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# 2
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

opcoes = [letras, numeros, simbolos]

# print("Bem vindo ao Gerador de Senha Py!")
# nr_letras = int(input("Quantas letras você quer na sua senha??\n"))
# nr_simbolos = int(input(f"Quantos simbolos você quer adicionar??\n"))
# nr_numeros = int(input(f"Quantos números você quer adicionar??\n"))

# print(opcoes[0][0])

##############################################################
########## Cria uma lista de letras aleatórias:      #########
##############################################################
lista_de_letras = []
for letra_do_alfabeto in range(0, 4):
    num_aleatorio = random.randint(0, 51)
    lista_de_letras.append(opcoes[0][num_aleatorio])
# print(f' Lista de letras: {lista_de_letras}')


##############################################################
######## Cria uma lista de simbolos aleatórios:      #########
##############################################################
lista_de_simbolos = []
for simbolo in range(0, 4):

    gerar_simbolo_aleatorio = random.randint(0, 8)
    lista_de_simbolos.append(opcoes[2][gerar_simbolo_aleatorio])
# print(f' Lista de simbolos: {lista_de_simbolos}')


##############################################################
########    Cria uma lista de números aleatórios:    #########
##############################################################
lista_de_numeros = []
for numero in range(0, 4):

    gerar_numero_aleatorio = random.randint(0, 9)
    lista_de_numeros.append(opcoes[1][gerar_numero_aleatorio])
# print(f' Lista de simbolos: {lista_de_numeros}')


juntar_caracteres = lista_de_letras + lista_de_simbolos + lista_de_numeros


print(*juntar_caracteres)
print("A sua senha é: "+''.join(juntar_caracteres))
# print(*lista_de_letras+lista_de_simbolos+lista_de_numeros)
# print(lista_de_letras+lista_de_simbolos+lista_de_numeros)
