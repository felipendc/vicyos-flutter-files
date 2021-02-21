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
    print(art.logo)
    gostaria_de_jogar = input(
        "Você gostaria de jogar Vinte-e-um? Digite 's' para jogar ou 'n' não jogar ").lower()

    if gostaria_de_jogar == 's':
        # Primeira carta para o jogador
        cartas_atuais_do_jogador.append(dar_cartas())
        pontuacao_do_jogador = sum(cartas_atuais_do_jogador)

        # Segunda carta para o jogador
        cartas_atuais_do_jogador.append(dar_cartas())
        pontuacao_do_jogador = sum(cartas_atuais_do_jogador)

        # Primeira carta para o computador
        cartas_atuais_do_computador.append(dar_cartas())
        pontuacao_do_computador = sum(cartas_atuais_do_computador)

        # Segunda carta para o computador
        cartas_atuais_do_computador.append(dar_cartas())
        pontuacao_do_computador = sum(cartas_atuais_do_computador)

        os.system('cls') or None
        print(art.logo)
        print(
            f'Suas cartas: {cartas_atuais_do_jogador}, pontuação atual: {pontuacao_do_jogador}')
        print(
            f'Primeira carta do computador: {cartas_atuais_do_computador[0]}')

        while continuar_jogando == True:

            if 11 in cartas_atuais_do_jogador and pontuacao_do_jogador > 21:
                cartas_atuais_do_jogador.remove(11)
                cartas_atuais_do_jogador.append(1)
                pontuacao_do_jogador = sum(cartas_atuais_do_jogador)

            if pontuacao_do_computador > 21 or pontuacao_do_jogador > 21:
                continuar_jogando = False

            comprar_ou_passar = input(
                "Digite 's' para pegar mais uma carta ou digite 'n' para passar a vez: ").lower()

            if comprar_ou_passar == 's':
                # Comprar carta
                cartas_atuais_do_jogador.append(dar_cartas())
                # Pontuação
                pontuacao_do_jogador = sum(cartas_atuais_do_jogador)

                print(
                    f'Suas cartas: {cartas_atuais_do_jogador}, pontuação atual: {pontuacao_do_jogador}')
                print(pontuacao_do_jogador)

                os.system('cls') or None
                print(f'Cartas do jogador {cartas_atuais_do_jogador}')

                # print(
                #     f'Primeira carta do computador: {cartas_atuais_do_jogador[0]}')
                print(f'Cartas do computador {cartas_atuais_do_computador}')

            if 11 in cartas_atuais_do_jogador and pontuacao_do_jogador > 21:
                cartas_atuais_do_jogador.remove(11)
                cartas_atuais_do_jogador.append(1)
                pontuacao_do_jogador = sum(cartas_atuais_do_jogador)

                if pontuacao_do_computador > 21 or pontuacao_do_jogador > 21:
                    continuar_jogando = False
            else:
                continuar_jogando = False
                print(continuar_jogando)

            # Vez do computador jogar:
        while pontuacao_do_computador < 17:
            pontuacao_do_computador = sum(cartas_atuais_do_computador)
            if 11 in cartas_atuais_do_computador and pontuacao_do_computador > 21:
                cartas_atuais_do_computador.remove(11)
                cartas_atuais_do_computador.append(1)

            # Comprar carta para o computador
            cartas_atuais_do_computador.append(dar_cartas())
            # Pontuação do computador
            pontuacao_do_computador = sum(cartas_atuais_do_computador)

    # Fim de jogo
    print('')
    print(
        f'Sua mão final: {cartas_atuais_do_jogador}, pontuação final: {pontuacao_do_jogador}')

    print(
        f'Mão final do computador: {cartas_atuais_do_computador}, pontuação final: {pontuacao_do_computador}')

    if pontuacao_do_jogador == 21:
        print('\nVocê acertou 21 pontos!!!!')

    elif pontuacao_do_computador == 21:
        print('\nO computador acertou 21 pontos!!!!')

    elif pontuacao_do_computador == pontuacao_do_jogador:
        print('\nHouve um impate')

    elif pontuacao_do_jogador > 21 and pontuacao_do_computador <= 21:
        print('\nO computador venceu! Hahaha. Pois, você ultrapassou o limite de 21.')

    elif pontuacao_do_computador > 21 and pontuacao_do_jogador <= 21:
        print('\nVocê ganhou! Hahaha. Pois, computador ultrapassou o limite de 21. ')

    elif pontuacao_do_computador > 21 and pontuacao_do_jogador > 21:
        print('\nVocê e o computador perderam! Hahaha. Pois, ambos ultrapassaram o limite de 21. ')

    elif pontuacao_do_computador > pontuacao_do_jogador and pontuacao_do_computador <= 21:
        print(
            '\nO computador venceu! Hahaha. A pontuação do computador é maior que a sua. ')

    elif pontuacao_do_jogador > pontuacao_do_computador and pontuacao_do_jogador <= 21:
        print('\nVocê venceu! Hahaha A sua pontuação é maior que a docomputador. ')


vinte_e_um()

##############
# Fim do jogo
