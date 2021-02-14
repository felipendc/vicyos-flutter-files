import os  # Pra limpar a tela do CMD
import art
from parte_do_dia import horario, fim_horario

ofertadores = {}


def add_novo_ofertador(nome_do_ofertador, lance_do_ofertador, genero_do_ofertador):

    # Posições da lista dentro do dicionário:
    #{chave: valor}
    #{'ofertador': [lance, genero]}

    # A posição 0 vai armazenar o nome do apostador.
    # A posição 1 vai armazenar o genero do apostador(a).
    #{'ofertador': [0, 1]}
    # {'ofertador': [lance_do_ofertador posição 0, genero_do_ofertador posição 1]}
    ofertadores[nome_do_ofertador] = [lance_do_ofertador, genero_do_ofertador]


def ganhador_com_maior_lance():
    maior_lance = 0
    nome_do_ofertador = ''
    for ofertador in ofertadores:
        if ofertadores[ofertador][0] > maior_lance:
            maior_lance = ofertadores[ofertador][0]
            nome_do_ofertador = ofertador.capitalize()
            genero = ofertadores[ofertador][1]
    os.system('cls') or None
    print(art.logo)

    if genero == 'f':
        print(
            f'A vencedora é a: {nome_do_ofertador}, com um lance de: R$ {maior_lance}\n{fim_horario }')
    else:
        print(
            f'O vencedor é o: {nome_do_ofertador}, com um lance de: R$ {maior_lance}\n{fim_horario }')


sem_mais_ofertadores = False
while not sem_mais_ofertadores:

    os.system('cls') or None
    print(art.logo)
    print(f'Olá, {horario}, bem-vindo ao Leilão Cego!')

    add_nome = input('Qual é o seu nome? ').lower()

    os.system('cls') or None
    print(art.logo)
    genero = input(
        'Qual é o seu gênero? Digite: "f" para Feminino ou "m" para Masculino: ').lower()

    os.system('cls') or None
    print(art.logo)
    add_lance = int(input('Qual é o seu lance? R$ '))

    os.system('cls') or None
    print(art.logo)
    add_novo_ofertador(nome_do_ofertador=add_nome,
                       lance_do_ofertador=add_lance, genero_do_ofertador=genero)

    mais_ofertadores = input(
        "Alguém mais deseja ofertar? Digite 'sim' ou 'não'.\n").lower()
    if mais_ofertadores == 'não' or mais_ofertadores == 'nao':
        sem_mais_ofertadores = True

        ganhador_com_maior_lance()
