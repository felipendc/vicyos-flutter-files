import random
import art
import os


def dar_cartas():
    lista_de_cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    carta_aleatoria = int(random.choice(lista_de_cartas))
    return carta_aleatoria


def vinte_e_um():
    cartas_atuais_do_computador = []
    cartas_atuais_do_jogador = []

    # Pontuação e Flag para parar o While loop
    pontuacao_do_computador = 0
    pontuacao_do_jogador = 0
    continuar_jogando = True

    ######## INICIO DO JOGO ############
    os.system('cls') or None
    gostaria_de_jogar = input(
        f"{art.logo}\nVocê gostaria de jogar Vinte-e-um? Digite 's' para jogar ou 'n' não jogar: ").lower()

    if gostaria_de_jogar == 's':
        # Dar duas cartas para cada jogador
        for jogares in range(2):
            cartas_atuais_do_jogador.append(dar_cartas())
            cartas_atuais_do_computador.append(dar_cartas())
            pontuacao_do_jogador = sum(cartas_atuais_do_jogador)
            pontuacao_do_computador = sum(cartas_atuais_do_computador)

        os.system('cls') or None
        print(
            f'{art.logo}\nSuas cartas: {cartas_atuais_do_jogador}, pontuação atual: {pontuacao_do_jogador}')
        print(
            f'Primeira carta do computador: {cartas_atuais_do_computador[0]}')

        while continuar_jogando == True:
            comprar_ou_passar = input(
                "Digite 's' para pegar mais uma carta ou digite 'n' para passar a vez: ").lower()

            if comprar_ou_passar == 's':
                # Comprar carta
                cartas_atuais_do_jogador.append(dar_cartas())

                # Reatualizar a pontuação do jogador
                pontuacao_do_jogador = sum(cartas_atuais_do_jogador)

                if 11 in cartas_atuais_do_jogador and pontuacao_do_jogador > 21:
                    cartas_atuais_do_jogador.remove(11)
                    cartas_atuais_do_jogador.append(1)

                # Reatualizar a pontuação do jogador
                pontuacao_do_jogador = sum(cartas_atuais_do_jogador)

                # Limpar a tela do CMD
                os.system('cls') or None
                print(
                    f'{art.logo}\nSuas cartas: {cartas_atuais_do_jogador}, pontuação atual: {pontuacao_do_jogador}')
                print(
                    f'Primeira carta do computador: {cartas_atuais_do_computador[0]}')

                if pontuacao_do_jogador > 21:
                    continuar_jogando = False

            elif comprar_ou_passar != 's':
                continuar_jogando = False

            # Vez do computador jogar:
        while pontuacao_do_computador < 17:

            # Reatualizar a pontuação do computador
            pontuacao_do_computador = sum(cartas_atuais_do_computador)
            if 11 in cartas_atuais_do_computador and pontuacao_do_computador > 21:
                cartas_atuais_do_computador.remove(11)
                cartas_atuais_do_computador.append(1)

            # Comprar carta para o computador
            cartas_atuais_do_computador.append(dar_cartas())

        # Reatualizar a pontuação do computador e finalizar
        pontuacao_do_computador = sum(cartas_atuais_do_computador)

    # Fim de jogo
    os.system('cls') or None
    print(
        f'{art.logo}\nSua mão final: {cartas_atuais_do_jogador}, pontuação final: {pontuacao_do_jogador}')

    print(
        f'Mão final do computador: {cartas_atuais_do_computador}, pontuação final: {pontuacao_do_computador}')

    if pontuacao_do_jogador == 21:
        print('\nVocê acertou 21 pontos!!!!\n')

    elif pontuacao_do_computador == 21:
        print('\nO computador acertou 21 pontos!!!!\n')

    elif pontuacao_do_computador == pontuacao_do_jogador:
        print('\nHouve um impate.\n')

    elif pontuacao_do_jogador > 21 and pontuacao_do_computador <= 21:
        print('\nO computador venceu! Hahaha. Pois, você ultrapassou o limite de 21.\n')

    elif pontuacao_do_computador > 21 and pontuacao_do_jogador <= 21:
        print('\nVocê ganhou! Hahaha. Pois, computador ultrapassou o limite de 21.\n')

    elif pontuacao_do_computador > 21 and pontuacao_do_jogador > 21:
        print('\nVocê e o computador perderam! Hahaha. Pois, ambos ultrapassaram o limite de 21.\n')

    elif pontuacao_do_computador > pontuacao_do_jogador and pontuacao_do_computador <= 21:
        print(
            '\nO computador venceu! Hahaha. A pontuação do computador é maior que a sua.\n')

    elif pontuacao_do_jogador > pontuacao_do_computador and pontuacao_do_jogador <= 21:
        print('\nVocê venceu! Hahaha A sua pontuação é maior que a docomputador.\n')

    jogar_novamente = input(
        "Você gostaria de jogar novamente? Digite 's' para jogar ou 'n' não jogar: ").lower()
    if jogar_novamente == 's':
        vinte_e_um()


vinte_e_um()
