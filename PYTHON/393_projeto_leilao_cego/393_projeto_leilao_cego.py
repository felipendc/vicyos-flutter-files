import os  # Pra limpar a tela do CMD
import art

print('Bem-vindo ao Leilão Cego')


add_nome = input('Qual é o seu nome? ')
add_lance = int(input('Qual é o seu lance? R$'))
novo_apostador = add_nome = input(
    "Alguém mais deseja ofertar? Digite 'sim' ou 'não'. ")

ofertadores = {}


def add_novo_ofertador():
