import random

lista_de_palavras = ["aardvark", "baboon", "camel"]

pegar_uma_palavra = random.randint(0, len(lista_de_palavras))
palavra_escolhida = lista_de_palavras[pegar_uma_palavra]

# Testing code
print(f'Pssst, a palavra escolhida foi: {palavra_escolhida}.')


# TODO-1: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.


letra_escolhida = input("Escolha uma letra: ").lower()

# TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

for letra in palavra_escolhida:
    if letra_escolhida == letra:
        print('Acertou')
    else:
        print('Errou')


# TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
