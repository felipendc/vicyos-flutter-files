
# print(8 / 3)
# Resultado: 2.6666... "O resultado é em float [com ponto decimal]"

# print(int(8 / 3))
# Resultado: 2 "Sem o ponto decimal"

# print(round(8 / 3))
#  Resultado: 3 "O round arredonta um float para o número mais próximo.
# Exemplo: Se o resultado for 2.4 ou menor: 2.3, 2.2, 2.1, o round() vai arredondar para 2.
# Mas caso se for igual 2.5 ou acima: 2.6, 2.7, 2.8, 2.9, o round() sempre vai arredondar para 3 "

# print(round(8 / 3, 2)) O 2 aqui representa a quantidade de números decimais que eu quero que seja printado:
# Resultado: 2.67 "Tem 2 números após o ponto decimal"

# print(round(8 // 3, 2)) As duas barras server para retornar um valor inteiro, sem casas decimais:
# Resultado: 2

# Continuar fetuando calculos com variáveis:
# result = 4 / 2 "seria 2"
# result /= 2 "O 4 seria dividido por 2 e, a vareável "result" passaria ser 1"

# score = 0

# User scored a point:
# score += 1 "Ele crecentará o 1 na vareável 'score' e ela passará a ser 1"
# score -= 1 "Ele removerá o 1 na vareável 'score' e ela passará a ser 0 novamente"
# Exemplos opcionais: score *= score /=


# f-String: Ele automaricamente já formata as vareáveis para string na funcão print.
# Lembrando que o f tem que vir antes das aspas ou aspas duplas: print(f"") ou print(f'')

# Ex: print(f"O seu placar é: {score}")
# resultado: O seu placar é: 0

# Exemplo:
# score = 0
# height = 1.8
# isWinning = True
# print(f"Your score is: {score}, your height is {height}, you are winning is {isWinning}")
