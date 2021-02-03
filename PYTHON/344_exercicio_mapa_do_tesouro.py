row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
mapa = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
posicao = input("Onde você quer colocar o tesouro? ")

# Pega a primeira posição dos digitos inseridos:
fileira = int(posicao[0]) - 1

# Pega a segunda posição dos digitos inseridos:
columa = int(posicao[1]) - 1


# Se refere a posição da lista Mapa
# Coloca a segunda posição do digito inserido na posição da lista Mapa:
coluna_do_mapa = mapa[columa]

# Se refere a posição da lista Row
# Coloca a primeira posição do digito inserido na posição da lista Row:
# E coloca o emoji do dinheiro na posição do seguindo digito inserido pelo usuário.
fileira_do_mapa = coluna_do_mapa[fileira] = "💰"

# Printa como ficou o resultado:
print(f"{row1}\n{row2}\n{row3}")


##########################################
# Segunda maneira de escrever o código:
##########################################

# row1 = ["⬜️", "️⬜️", "️⬜️"]
# row2 = ["⬜️", "⬜️", "️⬜️"]
# row3 = ["⬜️️", "⬜️️", "⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")

# position = input("Where do you want to put the treasure? ")

# horizontal = int(position[0])
# vertical = int(position[1])

# map[vertical - 1][horizontal - 1] = "X"

# print(f"{row1}\n{row2}\n{row3}")
