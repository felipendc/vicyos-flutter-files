import random
import random  # Gerar um número aleátorio
import os  # Vou usar para poder executar comandos no CMD do Windows!
pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Limpar a tela do CMD do Windows
os.system('cls') or None

# Salva a escolha do usuário:
escolha = int(input(
    "Qual você escolhe? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura: "))

# Gera um número aleátorio entre 0 a 2:
numero_aleatorio = random.randint(0, 2)

if escolha >= 3 or escolha < 0:
    print("Você digitou um número inválido, você perdeu!")
else:
    # Lógica do jogo!
    if escolha == 0 and numero_aleatorio == 0:
        print(f'Você escolheu: {pedra}\n ')
        print(f'O computador escolheu: {pedra}\n ')
        print('Empate!')

    elif escolha == 0 and numero_aleatorio == 1:
        print(f'Você escolheu: {pedra}\n ')
        print(f'O computador escolheu: {papel}\n ')
        print('Você perdeu. Só lamento!')

    elif escolha == 0 and numero_aleatorio == 2:
        print(f'Você escolheu: {pedra}\n ')
        print(f'O computador escolheu: {tesoura}\n ')
        print('Você venceu. Mizelaví!')

    elif escolha == 1 and numero_aleatorio == 1:
        print(f'Você escolheu: {papel}\n ')
        print(f'O computador escolheu: {papel}\n ')
        print('Empate!')

    elif escolha == 1 and numero_aleatorio == 0:
        print(f'Você escolheu: {papel}\n ')
        print(f'O computador escolheu: {pedra}\n ')
        print('Você venceu. Mizelaví!')

    elif escolha == 1 and numero_aleatorio == 2:
        print(f'Você escolheu: {papel}\n ')
        print(f'O computador escolheu: {tesoura}\n ')
        print('Você perdeu. Só lamento!')

    elif escolha == 2 and numero_aleatorio == 2:
        print(f'Você escolheu: {tesoura}\n ')
        print(f'O computador escolheu: {tesoura}\n ')
        print('Empate!')

    elif escolha == 2 and numero_aleatorio == 0:
        print(f'Você escolheu: {tesoura}\n ')
        print(f'O computador escolheu: {pedra}\n ')
        print('Você perdeu. Só lamento!')

    elif escolha == 2 and numero_aleatorio == 1:
        print(f'Você escolheu: {tesoura}\n ')
        print(f'O computador escolheu: {papel}\n ')
        print('Você venceu. Mizelaví!')

# Código finalizado com sucesso na primeira tentativa!!!


####################################################
#### Outra maneira de escrever o mesmo código:  ####
####################################################

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# game_images = [rock, paper, scissors]

# user_choice = int(
#     input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# if user_choice >= 3 or user_choice < 0:
#     print("You typed an invalid number, you lose!")
# else:
#     print(game_images[user_choice])

#     computer_choice = random.randint(0, 2)
#     print("Computer chose:")
#     print(game_images[computer_choice])

#     if user_choice == 0 and computer_choice == 2:
#         print("You win!")
#     elif computer_choice == 0 and user_choice == 2:
#         print("You lose")
#     elif computer_choice > user_choice:
#         print("You lose")
#     elif user_choice > computer_choice:
#         print("You win!")
#     elif computer_choice == user_choice:
#         print("It's a draw")

####### Debugging challenge: #########
# Try running this code and type 5.
# It will give you an IndexError and point to line 32 as the issue.
# But on line 38 we are trying to prevent a crash by detecting
# any numbers great than or equal to 3 or less than 0.
# So what's going on?
# Can you debug the code and fix it?
# Solution: https://repl.it/@appbrewery/rock-paper-scissors-debugged-end
