from art import logo
import brain
import os


os.system('cls') or None  # Limpar CMD
print(logo)

# Codificar ou decodificar?
direcao = input(
    'Digite "codificar" para criptografar ou digite "decodificar" para descriptografar:\n')

# Escolha do usuário:
texto_do_usuario = ''
if direcao == "codificar":
    mensagem = input(
        'Digite a mensagem que você quer codificar:\n').lower()
    texto_do_usuario = mensagem
elif direcao == "decodificar":
    mensagem = input(
        'Digite a mensagem que você quer decodificar:\n').lower()
    texto_do_usuario = mensagem

# Números de indices a ser deslocado:
deslocamento = int(input('Digite o número de deslocamento: '))


# Chamar a função "criptografar".
brain.criptografar(direcao=direcao, texto_do_usuario=texto_do_usuario,
                   deslocamento=deslocamento)
