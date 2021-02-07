import random
import os

estagios_desenho = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
Irruh! Eu te avisei. Se você errasse, você já saberia o que ia acontecer.
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
Ops! você errou! Agora só restam: 1 vida. Se você errar, já sabem oque acontece, né?
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
Ops! você errou! Agora só restam: 2 vidas. Oh, Ouh!
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
Ops! você errou! Agora só restam: 3 vidas. Tá difícil, não?
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
Ops! você errou! Agora só restam: 4 vidas. Hmmm..!
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
Ops! você errou! Agora só restam: 5 vidas. Hahaha!
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========

''']

lista_de_palavras = ["aardvark", "baboon", "camel"]

pegar_uma_palavra = random.randint(0, len(lista_de_palavras) - 1)
palavra_escolhida = lista_de_palavras[pegar_uma_palavra]

# Guardará as palavras acertadas:
display = []

fim_do_jogo = False
# Quantidades de vidas = 7 ao total.:
vidas = 6


for letra in palavra_escolhida:
    display.append("_")

# APENAS PARA TESTAR O CÓDIGO:
print(f'Pssst, a palavra escolhida foi: {palavra_escolhida}.')


###################  WHILE LOOP ##################
while not fim_do_jogo:

    os.system('cls') or None  # Pra limpar o CMD do Windows!
    print(' '.join(display))
    print(estagios_desenho[vidas])

    letra_escolhida = input("Escolha uma letra: ").lower()

    index_da_letra = 0
    for letra in palavra_escolhida:

        if letra_escolhida == letra:
            display[index_da_letra] = letra
            index_da_letra += 1

        else:
            index_da_letra += 1

    if letra_escolhida not in palavra_escolhida:
        vidas -= 1

    if "_" not in display:
        fim_do_jogo = True
        print('\n\nVocê acertou todas seu MIZELÁÁÁ-VI! \n\n')

    if vidas == 0:
        fim_do_jogo = True

        os.system('cls') or None  # Pra limpar o CMD do Windows!
        print(estagios_desenho[vidas])
        print('Ah, que peninha... parece que você perdeu! Hahaha.\n')
