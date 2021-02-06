import random
# Step 1

lista_de_palavras = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
pegar_uma_palavra = random.randint(0, len(lista_de_palavras))
palavra_escolhida = lista_de_palavras[pegar_uma_palavra]
print(palavra_escolhida)


# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
letra_escolhida = input("Escolha uma letra: ").lower()


# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letra in palavra_escolhida:
    if letra_escolhida == letra:
        print('Acertou')
    else:
        print('Errou')
