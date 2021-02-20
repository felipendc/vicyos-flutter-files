import random
import art
import os


def dar_cartas():
    lista_de_cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(lista_de_cartas)


def vinte_e_um():
    cartas_do_jogador_atual = []
    cartas_do_computador_atual = []

    # Pontuação e Flag para parar o While loop
    pontuacao_do_computador = 0
    pontuacao_do_jogador = 0
    continuar_jogando = False

    ######## INICIO DO JOGO ############
    os.system('cls') or None
    print(art.logo)
    gostaria_de_jogar = input(
        "Você gostaria de jogar Vinte-e-um? Digite 's' para jogar ou 'n' não jogar ").lower()

    if gostaria_de_jogar == 's':
        # Primeira carta para o jogador
        cartas_do_jogador_atual.append(dar_cartas())
        soma_das_cartas_do_jogador = sum(cartas_do_jogador_atual)
        pontuacao_do_jogador = soma_das_cartas_do_jogador

        # Segunda carta para o jogador
        cartas_do_jogador_atual.append(dar_cartas())
        soma_das_cartas_do_jogador = sum(cartas_do_jogador_atual)
        pontuacao_do_jogador = soma_das_cartas_do_jogador

        # Primeira carta para o computador
        cartas_do_computador_atual.append(dar_cartas())
        soma_das_cartas_do_computador = sum(cartas_do_computador_atual)
        pontuacao_do_computador = soma_das_cartas_do_computador

        # Segunda carta para o computador
        cartas_do_computador_atual.append(dar_cartas())
        soma_das_cartas_do_computador = sum(cartas_do_computador_atual)
        pontuacao_do_computador = soma_das_cartas_do_computador

        os.system('cls') or None
        print(art.logo)
        print(
            f'Suas cartas: {cartas_do_jogador_atual}, pontuação atual: {pontuacao_do_jogador}')
        print(f'Primeira carta do computador: {cartas_do_computador_atual[0]}')

        while pontuacao_do_computador <= 21 and pontuacao_do_jogador <= 21 and continuar_jogando:
            comprar_ou_passar = input(
                "Digite 's' para pegar mais uma carta ou digite 'n' para passar a vez: ").lower()

            if comprar_ou_passar == 's':
                # Comprar carta
                cartas_do_jogador_atual.append(dar_cartas())
                # Pontuação
                soma_das_cartas_do_jogador = sum(cartas_do_jogador_atual)
                pontuacao_do_jogador = soma_das_cartas_do_jogador

                print(
                    f'Suas cartas: {cartas_do_jogador_atual}, pontuação atual: {pontuacao_do_jogador}')
                print(pontuacao_do_jogador)

                # Comprar carta para o computador
                cartas_do_computador_atual.append(dar_cartas())
                # Pontuação do computador
                soma_das_cartas_do_computador = sum(cartas_do_computador_atual)
                pontuacao_do_computador = soma_das_cartas_do_computador
                print(
                    f'Primeira carta do computador: {cartas_do_computador_atual[0]}')
                print(pontuacao_do_computador)
                print(cartas_do_computador_atual)

            else:

                continuar_jogando = True
                print(continuar_jogando)

            # Fim do jogo:

            # Pontuação do jogador
        pontuacao_do_jogador = sum(cartas_do_jogador_atual)
        print(
            f'Sua mão final: {cartas_do_jogador_atual}, pontuação final: {pontuacao_do_jogador}')

        # Pontuação do computador
        pontuacao_do_computador = sum(cartas_do_computador_atual)
        print(
            f'Mão final do computador: {cartas_do_computador_atual}, pontuação final: {pontuacao_do_computador}')
        print(f'VENCEU OU PERDEU')
        print(f'')


vinte_e_um()

##############
# Fim do jogo
