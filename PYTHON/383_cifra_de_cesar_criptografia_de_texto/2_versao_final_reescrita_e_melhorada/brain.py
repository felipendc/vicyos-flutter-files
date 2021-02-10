import os
import art
from datetime import datetime

# Caracteres adaptado para o Português brasileiro!
caracteres = ['á', 'à', 'â', 'ã', 'é', 'è', 'ê', 'í', 'ì', 'ó', 'ò', 'ô', 'ã', 'õ', 'ú', 'ù', 'ç', '˚', 'º', 'ª', ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
              'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$', '%', '&', '(', ')', '*', '+', 'á', 'à', 'â', 'ã', 'é', 'è', 'ê', 'í', 'ì', 'ó', 'ò', 'ô', 'ã', 'õ', 'ú', 'ù', 'ç', '˚', 'º', 'ª', ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
              'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$', '%', '&', '(', ')', '*', '+']

horas = int(datetime.now().strftime('%H'))

horario = ''
fim_horario = ''

if horas < 12:
    horario += 'bom dia'
    fim_horario += 'Tenha um ótimo dia.\n'
elif horas < 18:
    horario += 'boa tarde'
    fim_horario += 'Tenha uma ótima tarde.\n'
elif horas < 24:
    horario += 'boa noite'
    fim_horario += 'Tenha uma ótima noite.\n'


def cifra_de_cesar(deslocar, mensagem, direcao):
    deslocar = deslocar % 60
    if direcao == 'decodificar':
        deslocar *= -1

    mensagem_final = []

    for elemento in mensagem:
        if elemento in caracteres:
            posicao = caracteres.index(elemento)
            nova_posicao = posicao + deslocar
            mensagem_final.append(caracteres[nova_posicao])

    if direcao == "codificar":
        os.system('cls') or None
        print(art.logo, '\n')
        print("\nO seu texto codificado é: " +
              ''.join(mensagem_final) + "\n")

    elif direcao == "decodificar":
        os.system('cls') or None
        print(art.logo, '\n')
        print("\nO seu texto decodificado é: " +
              ''.join(mensagem_final) + "\n")
