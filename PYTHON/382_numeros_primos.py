import os

os.system('cls') or None  # Limpar o CMD

# Armazena o número que o usuário inserio:
checar_numero = int(input('Checar número: '))


def checar_primo_ou_composto(primo_ou_composto):

    # Se houver apenas 2 dentro de "numero_de_divisoes" o número é primo!
    numero_de_divisoes = 0
    for numeros in range(1, primo_ou_composto + 1):
        if primo_ou_composto % numeros == 0:
            numero_de_divisoes += 1

    if numero_de_divisoes == 2:
        print(f'\n{primo_ou_composto} é um número primo.\n')
    else:
        print(f'\n{primo_ou_composto}, não é um número primo.\n')


os.system('cls') or None
checar_primo_ou_composto(checar_numero)
