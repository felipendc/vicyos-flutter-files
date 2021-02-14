import os  # Pra limpar a tela do CMD
import art

ofertadores = {}
maior_lance = ''


def add_novo_ofertador(nome_do_ofertador, lance_do_ofertador):
    ofertadores[nome_do_ofertador] = lance_do_ofertador


# def ganhador_com_maior_lance(maior_lance):


# Part 1
sem_mais_ofertadores = False
while not sem_mais_ofertadores:

    os.system('cls') or None
    print(art.logo)
    print('Bem-vindo ao Leilão Cego!')

    add_nome = input('Qual é o seu nome? ').lower()
    add_lance = int(input('Qual é o seu lance? R$'))

    add_novo_ofertador(nome_do_ofertador=add_nome,
                       lance_do_ofertador=add_lance)

    mais_ofertadores = input(
        "Alguém mais deseja ofertar? Digite 'sim' ou 'não'. ").lower()
    if mais_ofertadores == 'não' or mais_ofertadores == 'nao':
        sem_mais_ofertadores = True

print(ofertadores)
