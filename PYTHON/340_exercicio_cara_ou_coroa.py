import random

# Gerar um número aleatório entre 0 a 1:1
numero_aleatorio = random.randint(0, 1)

cara_ou_coroa = ""

if numero_aleatorio == 1:
    cara_ou_coroa = "Cara"
else:
    cara_ou_coroa = "Coroa"

escolha = int(
    input('Digite "1" para escolher Cara ou "2" para esscolher Coroa: '))
usuario_escolheu = ""
if escolha == 1:
    usuario_escolheu = "Cara"
else:
    usuario_escolheu = "Coroa"

acertou_ou_nao = ""

if usuario_escolheu == cara_ou_coroa:
    acertou_ou_nao = "Parabéns! Você acertou!"
else:
    acertou_ou_nao = "Que pena! Você errou!"


if escolha == numero_aleatorio:
    print(
        f'Você escolheu: "{usuario_escolheu}" e o resultado também é: "{cara_ou_coroa}". {acertou_ou_nao}')
else:
    print(
        f'Você escolheu: "{usuario_escolheu}" e o resultado foi: "{cara_ou_coroa}". {acertou_ou_nao}')


# Ou eu poderia ter escrito o código de uma forma muito mais curta:

# random_side = random.randint(0, 1)
# if random_side == 1:
#   print("Heads")
# else:
#   print("Tails")
