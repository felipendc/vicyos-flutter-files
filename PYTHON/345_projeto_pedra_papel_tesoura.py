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
