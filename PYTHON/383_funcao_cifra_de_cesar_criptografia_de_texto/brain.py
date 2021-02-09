import os

# FUNÇÃO QUE VAI CRIPTOGRAFAR OU DECRIPTOGRAFAR UM TEXTO INSERIDO PELO USUÁRIO:


def criptografar(direcao, texto_do_usuario, deslocamento):
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # Se o "deslocamento" for qual a 0 ou maior que o tamanho do alfabeto...
    # então pare o código.
    if deslocamento > 25 or deslocamento == 0:
        os.system('cls') or None  # Limpar CMD

        print(
            '\nNo momento, o número máximo de deslocamento é de "1" até "25". Tente novamente.\n')

    else:
        if direcao == "decodificar":
            # Inverter de positivo para negativo!
            deslocamento *= -1

        indice_das_letras = []
        # Descobre a posição das letras:
        for letra in texto_do_usuario:
            index = - 1
            for posicao in alfabeto:
                index += 1
                if posicao == letra:
                    indice_das_letras.append(index)

        # print(len(alfabeto))  # 26
        reusar_alfabeto = []
        for letra in alfabeto:
            reusar_alfabeto += letra
        for letra in reusar_alfabeto:
            alfabeto += letra

        # Imprime as posições (indices) das letras em números:
        # print(indice_das_letras)

        # Converte a posição das letras em letras.
        converter_para_letra = []
        for elemento in indice_das_letras:
            elemento = deslocamento + int(elemento)
            converter_para_letra.append(alfabeto[elemento])

        if direcao == "codificar":
            os.system('cls') or None  # Limpar CMD
            print("\nO seu texto codificado é: " +
                  ''.join(converter_para_letra) + "\n")
            # print(alfabeto)
        elif direcao == "decodificar":
            os.system('cls') or None  # Limpar CMD
            print("\nO seu texto decodificado é: " +
                  ''.join(converter_para_letra) + "\n")
