import random  # Para gerar números aleatórios.
import os  # Para eu poder ter acesso aos comandos do CMD  do Windows.

#################################### OQUE O CÓDIGO FAZ? ######################################
# A ideia dese código é criar uma roleta-russa com o nome das pessoas inserida pelo usuário.
# O nome que for sorteado, será a pessoa que pagará a conta do restaurante.

# A idea é combinar a lista com os números aleatórios que eu aprendi no dia anterior!
##############################################################################################

# Split string method (Metodo para dividir string)
# Eu inseri o .capitalize() no final do input() para deixar todas as letras iniciais dos nomes inseridos em letra maiúsculas.
nomes_string = input(
    "Digite os nomes das pessoas, separados por virgula. "). capitalize()

# Converte os nomes das pessoas em uma lista. O método .split (dividir) separa os nomes pelas virgulas.
nomes = nomes_string.split(", ")

# No código abaixo eu vou gerar um número aleatório entre 0 (index[posição] inical) e o tamanho total da lista "nomes".
# Exemplo: numero_aleatorio = random.randint(numero_inicial, até_esse_numero_incluindo_ele)
# O -1 significa que eu estou me referindo ao ultimo index (posição) da lista e não ultrapassar o ultimo index.
numero_aleatorio = random.randint(0, len(nomes) - 1)

# Esse comando vai limpar o terminal:
os.system("cls") or None

# Imprime o nome das pessoas:
print(f'Nome das pessoas: {nomes}')

# Eu vou fazer um teste com o print(). Eu vou me referir a lista: "nomes" e eu vou usar o resultado do "random.randint(a, b)"
#  dentro do index da lista (nomes[random.randint([a, b]]) para eu pegar um nome aleatório, simples assim.
print(f"Nome sorteado: {nomes[numero_aleatorio]}")

# Teste para saber a posição (número) gerada aleatóriamente pelo random.ranint():
print(f"Posição: {numero_aleatorio}")

# Imprimir o tamanho da lista:
print(f'Tamanho da lista "nome": {len(nomes)}')


# Vai imprimir na tela o resultado da roleta-russa.
# A pessoa que foi sorteada, pagará a conta do restaurante.
print(
    f'\n"{nomes[numero_aleatorio]}" pagará a conta hoje! Boa sorte pra você "escolhido". Hahaha!\n')


# # Eu também poderia ter usado o método (função) choice do random.
# link que mostra um exemplo:
# https://www.w3schools.com/python/ref_random_choice.asp
# Mas, nesse exercício o método choice() não era permitido. hahaha.


#############################################
# Segunda maneira de escrever esse código!  #
#############################################


# # Split string method
# names_string = input("Give me everybody's names, seperated by a comma. ")
# names = names_string.split(", ")

# #Write your code below this line 👇

# #Get the total number of items in list.
# num_items = len(names)
# #Generate random numbers between 0 and the last index.
# random_choice = random.randint(0, num_items - 1)
# #Pick out random person from list of names using the random number.
# person_who_will_pay = names[random_choice]

# print(person_who_will_pay + " is going to buy the meal today!")
