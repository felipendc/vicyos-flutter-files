# criado por: Andrew

# Declara e atribui valores a diversos tipos de estruturas de dados
lista = [0, 1, 2, 3]  # Entre colchetes
tupla = (0, 1, 2, 3)  # Entre parênteses
# Entre chaves com : (dois pontos)
dicionario = {"zero": 0, "um": 1, "dois": 2, "três": 3}
conjunto = {0, 1, 2, 3}  # Entre chaves

# Imprime o tipo e o conteúdo de cada uma das estruturas de dados
print(type(lista), " ", lista)
print(type(tupla), "", tupla)
print(type(dicionario), " ", dicionario)
print(type(conjunto), " ", conjunto, "\n")

# Altera os valores (e a quantidade de variáveis) de cada estrutura
lista = [3, 4, 5]
tupla = (3, 4, 5)
dicionario = {"três": 3, "quatro": 4, "cinco": 5}
conjunto = {3, 4, 5}

# Imprime novamente o tipo e o conteúdo de cada uma das estruturas de dados
print(type(lista), " ", lista)
print(type(tupla), "", tupla)
print(type(dicionario), " ", dicionario)
print(type(conjunto), " ", conjunto, "\n")

# Imprime o conteúdo das estruturas um objeto por vez
print(type(lista), lista[0], lista[1], lista[2])
print(type(tupla), tupla[0], tupla[1], tupla[2])
print(type(dicionario), dicionario.get("três"),
      dicionario.get("quatro"), dicionario.get("cinco"))
# end="" para o print não pular a linha
print("{} ".format(type(conjunto)), end="")
for elemento in conjunto:  # Conjuntos não tem índice mas podem ser iterados com for
    print(elemento, end=" ")  # Imprime o elemento do conjunto sem pular linha

# Comandos da lista
print("\n\n\tFunções da lista")
print("len da lista:", len(lista))  # Imprime o tamanho da lista
print("id da lista:", id(lista))  # Imprime a identidade da lista
# Conta o número de vezes que o valor da variável aparece na lista
print("count:", lista.count(3))
lista.remove(4)  # Remove o valor da lista
print("remove:", lista)
lista.append(4)  # Adiciona o valor a lista
print("append:", lista)
lista.sort()  # Coloca os valores da lista em ordem
print("sort:", lista)
lista.pop(2)  # Apaga um valor na lista indicado pelo índice
print("pop:", lista)
lista.insert(2, 5)  # Insere o valor na lista conforme o índice
print("insert:", lista)
lista.reverse()  # Reverte a ordem dos valores da lista
print("reverse:", lista)
# Se um valor está na lista (True ou False)
print("__contains__:", lista.__contains__(5))
lista2 = lista.copy()  # Copia os valores da lista para uma outra
print("copy:", lista2)  # Imprime a outra lista
lista.__delitem__(0)  # Deleta o valor no índice da lista
print("__delitem__:", lista)
del lista[0]  # Deleta o valor no índice especificado
print("del:", lista)
lista.clear()  # Limpa a lista
print("clear:", lista)

# Comandos da tupla
print("\n\tFunções da tupla")
print("hash:", tupla.__hash__())  # Hash da tupla
# Se a tupla contém um determinado valor
print("__contains__:", tupla.__contains__(3))
print("count:", tupla.count(4))  # Quantas vezes um valor se repete na tupla
print("len:", len(tupla))  # Imprime o tamanho da tupla
# Imprime o índice no qual o valor é encontrado na tupla
print("index:", tupla.index(5))

# Comandos da dicionário
print("\n\tFunções da dicionário")
print("len:", len(dicionario))  # Tamanho do dicionário
# imprime o valor na chave especificada
print("get:", dicionario.get("quatro"))
print("values:", dicionario.values())  # Imprime os valores do dicionário
print("keys:", dicionario.keys())  # Imprime as chaves do dicionário
dicionario.popitem()  # Deleta a última chave e valor do dicionário
print("popitem:", dicionario)
dicionario.pop("três")  # Deleta o valor com a chave especificada
print("pop:", dicionario)
dicionario["três"] = 3  # Adiciona uma chave e valor ao dicionário
dicionario["cinco"] = 5  # Adiciona outra chave e valor ao dicionário
# Imprime apenas o valor da chave específica
print("Adiciona:", dicionario["três"])
del dicionario["quatro"]  # Deleta chave e valor especificados
print("del:", dicionario)
dicionario.__delitem__("cinco")  # Deleta chave e valor especificados
print("__deletitem__:", dicionario)
dicionario["quatro"] = 4  # Adiciona uma chave e valor ao dicionário
dicionario["cinco"] = 5  # Adiciona uma chave e valor ao dicionário
print("Adiciona:", dicionario)
dicionario2 = dicionario.copy()  # Copia o dicionário
print("copy:", dicionario2)
while(len(dicionario) > 0):  # Enquanto houverem itens no dicionário
    dicionario.popitem()  # Deleta o último item do dicionário
print("while, popitem:", dicionario)  # Mostra que o dicionário está vazio

# Associa as letras do alfabeto a números
dicionario = dict(enumerate("abcdefghijklmnopqrstuvxywz"))
print("dict enumerate:", dicionario)

# Imprime "p y t h o n"
print(dicionario[15], dicionario[23], dicionario[19],
      dicionario[7], dicionario[14], dicionario[13])
dicionario.clear()  # Limpa o dicionário
print("clear:", dicionario)  # Mostra que o dicionário está vazio

# Comandos do conjunto (set)
print("\n\tFunções do conjunto (set)")
conjunto.discard(3)  # Discarta um elemento do conjunto
print("discard:", conjunto)
# Add que não adiciona nada, por que o objeto 4 já é parte do conjunto
conjunto.add(4)
conjunto.add(1)  # Adiciona o objeto 1 ao conjunto
conjunto.add(6)  # Adiciona o objeto 9 ao conjunto
print("add:", conjunto)
conjunto.remove(5)  # Remove o objeto especificado
print("remove:", conjunto)
conjunto.pop()  # Apaga o primeiro objeto do conjunto
print("pop:", conjunto)
conjunto.add(2)  # Adiciona um objeto
conjunto2 = conjunto.copy()  # Copia o conjunto
print("copy:", conjunto2)
conjunto.clear()  # Limpa o conjunto
print("clear:", conjunto)

input("\nAperte ENTER para sair...")
