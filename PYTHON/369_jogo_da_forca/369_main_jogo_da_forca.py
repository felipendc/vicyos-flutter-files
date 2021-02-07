import jogo_da_forca_arte as arte  # importa a arte e a logo.
import jogo_da_forca_palavras as palavras  # importa a lista de palavras
import random
import os


pegar_uma_palavra = random.randint(
    0, len(palavras.lista_de_palavras) - 1)

palavra_escolhida = palavras.lista_de_palavras[pegar_uma_palavra]

# Guardará as palavras acertadas:
display = []

fim_do_jogo = False
# Quantidades de vidas = 7 ao total.:
vidas = 6

print(arte.logo)

for letra in palavra_escolhida:
    display.append("_")

# Se a letra já existe na vareável "display",
# ele armazena um aviso que a letra já existe.
# Caso o contrário, ele não armazena nada.
ja_foi_escolhido = ''

# Verifica se a letra não existe na vareável "palavra_escohida".
nao_existe_em_palavra_escolhida = ''

# APENAS PARA TESTAR O CÓDIGO:
print(f'Pssst, a palavra escolhida foi: {palavra_escolhida}.')

###################  WHILE LOOP ##################
while not fim_do_jogo:

    print(' '.join(display))
    print(arte.estagios_desenho[vidas])
    print(ja_foi_escolhido)
    print(nao_existe_em_palavra_escolhida)

    letra_escolhida = input("Escolha uma letra: ").lower()

    if letra_escolhida in display:
        ja_foi_escolhido = f'Tente outra letra. Pois, você já escolheu a letra: "{letra_escolhida}"\n'
    else:
        ja_foi_escolhido = ''

    if letra_escolhida not in palavra_escolhida:
        nao_existe_em_palavra_escolhida = f'Você perdeu uma vida. Pois essa letra "{letra_escolhida}" não existe na palavra.\n'
    else:
        nao_existe_em_palavra_escolhida = ''

    index_da_letra = 0
    for letra in palavra_escolhida:

        if letra_escolhida == letra:
            display[index_da_letra] = letra
            index_da_letra += 1

        else:
            index_da_letra += 1

        os.system('cls') or None  # Pra limpar o CMD do Windows!

    if letra_escolhida not in palavra_escolhida:
        vidas -= 1

    if "_" not in display:
        fim_do_jogo = True
        print('\n\nVocê acertou todas seu MIZELÁÁÁ-VI! \n\n')

    if vidas == 0:
        fim_do_jogo = True

        os.system('cls') or None  # Pra limpar o CMD do Windows!
        print(arte.estagios_desenho[vidas])
        print('Ah, que peninha... parece que você perdeu! Hahaha.\n')


##########################################################
######  OUTRA MANEIRA DE ESCREVER O MESMO CÓDIGO!  #######

#from hangman_art import stages, logo
#from hangman_words import word_list
#from replit import clear

# print(logo)
# game_is_finished = False
# lives = len(stages) - 1

# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

# display = []
# for _ in range(word_length):
#     display += "_"

# while not game_is_finished:
#     guess = input("Guess a letter: ").lower()

#     #Use the clear() function imported from replit to clear the output between guesses.
#     clear()

#     if guess in display:
#         print(f"You've already guessed {guess}")

#     for position in range(word_length):
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter
#     print(f"{' '.join(display)}")

#     if guess not in chosen_word:
#         print(f"You guessed {guess}, that's not in the word. You lose a life.")
#         lives -= 1
#         if lives == 0:
#             game_is_finished = True
#             print("You lose.")

#     if not "_" in display:
#         game_is_finished = True
#         print("You win.")

#     print(stages[lives])
