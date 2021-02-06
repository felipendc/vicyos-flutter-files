import random

lista_de_palavras = ["aardvark", "baboon", "camel"]

pegar_uma_palavra = random.randint(0, len(lista_de_palavras) - 1)
palavra_escolhida = lista_de_palavras[pegar_uma_palavra]

# Testing code
print(f'Pssst, a palavra escolhida foi: {palavra_escolhida}.')


display = []


for letra in palavra_escolhida:
    display.append("_")


letra_escolhida = input("Escolha uma letra: ").lower()


index_da_letra = 0
for letra in palavra_escolhida:

    if letra_escolhida == letra:
        # print(index_da_letra)
        display[index_da_letra] = letra
        index_da_letra += 1
        # print('Acertou')
    else:
        # print(index_da_letra)
        index_da_letra += 1
        # print('Errou')


print(f'\nVocê escolheu a letra: {letra_escolhida}')

# O * ao lado do nome da lista removerá as virgulas e os colchetes.
# print(*display)


# Printar as letras corretas em sua posição.
# Dentro de '' deve haver um espaço ' ' para poder separar os caracteres.
# O .join(nome_da_vareável) vai remover as colchetes e as vírgulas da lista ou da vareável.

print("\n" + ' '.join(display) + "\n")
