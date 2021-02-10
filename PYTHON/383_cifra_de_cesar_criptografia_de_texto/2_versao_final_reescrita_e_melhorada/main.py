import os
import brain
import art
from brain import horario, fim_horario

os.system('cls') or None

finalizar = False
while not finalizar:
    os.system('cls') or None
    print(art.logo, '\n')

    direcao = input(
        f'Olá, {horario}, digite "codificar" para criptografar ou digite "decodificar" para descriptografar:\n')

    texto_do_usuario = ''
    if direcao == "codificar":
        mensagem = input(
            'Digite a mensagem que você quer codificar:\n').lower()
        texto_do_usuario = mensagem
    elif direcao == "decodificar":
        mensagem = input(
            'Digite a mensagem que você quer decodificar:\n').lower()
        texto_do_usuario = mensagem

    deslocar = int(input('Digite o número de deslocamento: '))

    brain.cifra_de_cesar(deslocar=deslocar,
                         mensagem=texto_do_usuario, direcao=direcao)

    reiniciar = input(
        'Para reiniciar digite: "r" ou digite: "f" para finalizar.\n').lower()
    if reiniciar == "f":
        finalizar = True
        os.system('cls') or None
        print(art.logo, '\n')
        print(f'Programa finalizado. {fim_horario}')
