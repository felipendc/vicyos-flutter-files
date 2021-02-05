# Password Generator Project (Projeto Gerador de Senha)
import random
import os

# 0 é a posição dessa lista dentro da lista opcoes:
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
          'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# 1 é a posição dessa lista dentro da lista opcoes:
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# 2 é a posição dessa lista dentro da lista opcoes:
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# Coloca todas as listas dentro de uma lista.
# Dessa forma, ficará muito mais fácil de se referir
# os itens de cada lista. E não terei problemas com
# mais de um tipo de aspas em cada caractere.

# Estrutura: opcoes[indice-da-lista-AAAA][indice-do-caractere-da-lista-AAAA]
# opcoes[0][0]
opcoes = [letras, numeros, simbolos]

# Limpar o CMD para remover as coisas desnessessárias:
os.system('cls') or None

print("\nBem vindo ao Gerador de Senha Py!")

# Armazenará a quantidade de letras, simbolos e números escolhido pelo usuário:
nr_letras = int(input("Quantas letras você quer na sua senha??\n"))
nr_simbolos = int(input(f"Quantos simbolos você quer adicionar??\n"))
nr_numeros = int(input(f"Quantos números você quer adicionar??\n"))


##############################################################
########## Cria uma lista de letras aleatórias:      #########
##############################################################
# Armazenará as letras:
lista_de_letras = []
for letra_do_alfabeto in range(0, nr_letras):
    num_aleatorio = random.randint(0, 51)
    lista_de_letras.append(opcoes[0][num_aleatorio])
# print(f' Lista de letras: {lista_de_letras}')


##############################################################
######## Cria uma lista de simbolos aleatórios:      #########
##############################################################
# Armazenará os simbolos:
lista_de_simbolos = []
for simbolo in range(0, nr_simbolos):

    gerar_simbolo_aleatorio = random.randint(0, 8)
    lista_de_simbolos.append(opcoes[2][gerar_simbolo_aleatorio])
# print(f' Lista de simbolos: {lista_de_simbolos}')


##############################################################
########    Cria uma lista de números aleatórios:    #########
##############################################################
# Armazenará os números:
lista_de_numeros = []
for numero in range(0, nr_numeros):

    gerar_numero_aleatorio = random.randint(0, 9)
    lista_de_numeros.append(opcoes[1][gerar_numero_aleatorio])
# print(f' Lista de simbolos: {lista_de_numeros}')

# Lista com todos os caracteres em ordem de seleção!
juntar_caracteres = lista_de_letras + lista_de_simbolos + lista_de_numeros

# O random.shuffle(aleatorizar_caracteres) vai fazer embaralhar a lista atual!
# Não esqueça de sempre fazer um backup da lista que você vai usar no random.choice(x)
# Em caso de você precisar re-ultilizar a lista original.
aleatorizar_caracteres = lista_de_letras + lista_de_simbolos + lista_de_numeros
aleatorizar = random.shuffle(aleatorizar_caracteres)


# Printar a senha em ordem de seleconada e em ordem aleatória:
print("\nNa ordem selecionada:\nA sua senha é: "+''.join(juntar_caracteres))
aleatorizar = random.shuffle(aleatorizar_caracteres)
print("\nNa ordem aleatória: \nA sua senha é: " +
      ''.join(aleatorizar_caracteres) + '\n')


######################################################
###### Outra maneira de escrever o mesmo lógica  #####
######################################################

# #Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# #Eazy Level
# # password = ""

# # for char in range(1, nr_letters + 1):
# #   password += random.choice(letters)

# # for char in range(1, nr_symbols + 1):
# #   password += random.choice(symbols)

# # for char in range(1, nr_numbers + 1):
# #   password += random.choice(numbers)

# # print(password)

# #Hard Level
# password_list = []

# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))

# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)

# print(password_list)
# random.shuffle(password_list)
# print(password_list)

# password = ""
# for char in password_list:
#   password += char

# print(f"Your password is: {password}")

