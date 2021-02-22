import random
import art
import os


def comprar_carta():
    lista_de_cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    carta_aleatoria = int(random.choice(lista_de_cartas))
    return carta_aleatoria


def jogo_vinte_e_um():
    cartas_atuais_do_adversario = []
    minhas_cartas_atuais = []

    # Pontuação e Flag para parar o While loop
    pontuacao_do_adversario = 0
    minha_pontuacao = 0
    continuar_jogando = True

    ######## INÍCIO DO JOGO ############
    os.system('cls') or None
    gostaria_de_jogar = input(
        f"{art.logo}\nVocê gostaria de jogar Vinte-e-um? Digite 's' para jogar ou 'n' não jogar: ").lower()

    if gostaria_de_jogar == 's':
        # Dar duas cartas para cada jogador
        for jogares in range(2):
            minhas_cartas_atuais.append(comprar_carta())
            cartas_atuais_do_adversario.append(comprar_carta())

        # Reatualizar a pontuação do jogador e do adversário
        minha_pontuacao = sum(minhas_cartas_atuais)
        pontuacao_do_adversario = sum(cartas_atuais_do_adversario)

        os.system('cls') or None
        print(
            f'{art.logo}\nMinhas cartas: {minhas_cartas_atuais}, minha pontuação atual: {minha_pontuacao}')
        print(
            f'Primeira carta do adversário: {cartas_atuais_do_adversario[0]}')

        while continuar_jogando == True:
            comprar_ou_passar = input(
                "Digite 's' para pegar mais uma carta ou digite 'n' para passar a vez: ").lower()

            if comprar_ou_passar == 's':
                # Comprar carta
                minhas_cartas_atuais.append(comprar_carta())

                # Reatualizar a pontuação do jogador
                minha_pontuacao = sum(minhas_cartas_atuais)

                if 11 in minhas_cartas_atuais and minha_pontuacao > 21:
                    minhas_cartas_atuais.remove(11)
                    minhas_cartas_atuais.append(1)

                # Reatualizar a pontuação do jogador
                minha_pontuacao = sum(minhas_cartas_atuais)

                # Limpar a tela do CMD
                os.system('cls') or None
                print(
                    f'{art.logo}\nMinhas cartas: {minhas_cartas_atuais}, minha pontuação atual: {minha_pontuacao}')
                print(
                    f'Primeira carta do adversário: {cartas_atuais_do_adversario[0]}')

                if minha_pontuacao > 21:
                    continuar_jogando = False

            elif comprar_ou_passar != 's':
                continuar_jogando = False

        # Vez do adversário jogar:
        # Atualizar a pontuação do adversário
        pontuacao_do_adversario = sum(cartas_atuais_do_adversario)
        while pontuacao_do_adversario < 17:
            # Reatualizar a pontuação do adversário
            pontuacao_do_adversario = sum(cartas_atuais_do_adversario)
            if 11 in cartas_atuais_do_adversario and pontuacao_do_adversario > 21:
                cartas_atuais_do_adversario.remove(11)
                cartas_atuais_do_adversario.append(1)

            # Comprar carta para o adversário
            cartas_atuais_do_adversario.append(comprar_carta())

        # Reatualizar a pontuação do adversário e finalizar
        pontuacao_do_adversario = sum(cartas_atuais_do_adversario)

    # Fim de jogo
    os.system('cls') or None
    print(
        f'{art.logo}\nMinha mão final: {minhas_cartas_atuais}, minha pontuação final: {minha_pontuacao}')

    print(
        f'Mão final do adversário: {cartas_atuais_do_adversario}, pontuação final do adversário: {pontuacao_do_adversario}')

    if minha_pontuacao == 21:
        print('\nVocê acertou 21 pontos!!!!\n')

    elif pontuacao_do_adversario == 21:
        print('\nO adversário acertou 21 pontos!!!!\n')

    elif pontuacao_do_adversario == minha_pontuacao:
        print('\nHouve um impate.\n')

    elif minha_pontuacao > 21 and pontuacao_do_adversario <= 21:
        print('\nO adversário venceu! Hahaha. Pois, você ultrapassou o limite de 21.\n')

    elif pontuacao_do_adversario > 21 and minha_pontuacao <= 21:
        print('\nVocê ganhou! Hahaha. Pois, adversário ultrapassou o limite de 21.\n')

    elif pontuacao_do_adversario > 21 and minha_pontuacao > 21:
        print('\nVocê e o adversário perderam! Hahaha. Pois, ambos ultrapassaram o limite de 21.\n')

    elif pontuacao_do_adversario > minha_pontuacao and pontuacao_do_adversario <= 21:
        print(
            '\nO adversário venceu! Hahaha. A pontuação do adversário é maior que a sua.\n')

    elif minha_pontuacao > pontuacao_do_adversario and minha_pontuacao <= 21:
        print('\nVocê venceu! Hahaha A sua pontuação é maior que a do adversário.\n')

    jogar_novamente = input(
        "Você gostaria de jogar novamente? Digite 's' para jogar ou 'n' não jogar: ").lower()
    if jogar_novamente == 's':
        jogo_vinte_e_um()


jogo_vinte_e_um()
