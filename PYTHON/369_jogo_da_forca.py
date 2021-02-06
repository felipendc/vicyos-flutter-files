import random
import os

##############################################################################
############## PARTE QUE FICARÁ FÓRA DO WHILE LOOP: ##########################
##############################################################################
lista_de_palavras = ["aardvark", "baboon", "camel"]

pegar_uma_palavra = random.randint(0, len(lista_de_palavras) - 1)
palavra_escolhida = lista_de_palavras[pegar_uma_palavra]

# Guardará as palavras acertadas:
display = []
palavra_completada = []

for letra in palavra_escolhida:
    display.append("_")

# APENAS PARA TESTAR O CÓDIGO:
print(f'Pssst, a palavra escolhida foi: {palavra_escolhida}.')


##############################################################################
############## PARTE QUE FICARÁ DENTRO DO WHILE LOOP: ########################
##############################################################################
while not len(palavra_escolhida) == len(palavra_completada):

    os.system('cls') or None  # Pra limpar o CMD do Windows!
    print(' '.join(display))
    letra_escolhida = input("Escolha uma letra: ").lower()

    index_da_letra = 0
    for letra in palavra_escolhida:

        if letra_escolhida == letra:
            display[index_da_letra] = letra
            index_da_letra += 1

            # Add + 1 até ele conter o mesmo número
            # de letra que a letra escolhida.
            palavra_completada += letra
        else:
            index_da_letra += 1

    os.system('cls') or None  # Pra limpar o CMD do Windows!
    print(f'\nVocê escolheu a letra: {letra_escolhida}')
    print("\nA palavra é: " + '"'+' '.join(display)+'"' + "\n")
    print("Parabéns! Você venceu!")
