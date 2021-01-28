# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
# HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the tip calculator")
total_da_conta = input("Qual é o total da conta? $")

porcentagem_da_gorjeta = input(
    "Qual é a porcentagem da gorjeta que vc gostaria de dar? 10, 12, or 15?")

quantidade_de_pessoas = input("Quantas pessoas irão dividir a conta? $")


# Converter os valores inseridos pelo usuário para numeros float (contas contém pontos decimais):
total_da_conta_int = float(total_da_conta)

# Converter os valores inseridos pelo usuário para numeros inteiros:
porcentagem_da_gorjeta_int = int(porcentagem_da_gorjeta)

# Converter os valores inseridos pelo usuário para numeros inteiros:
quantidade_de_pessoas_int = int(quantidade_de_pessoas)

# Calcula a porcentagem da gorjeta baseado no total da conta do cliente.
gorjeta_calculada = total_da_conta_int * \
    (porcentagem_da_gorjeta_int / 100)

Total_da_conta_com_gorjeta = total_da_conta_int + gorjeta_calculada

# Soma a porcentagem da gorjeta com o valor total e divide pela quantidade de pessoas:
dividir_a_conta = Total_da_conta_com_gorjeta / quantidade_de_pessoas_int

# Mostrar apenas 2 valores após o ponto decimal para ficar parecido com centavos usando
# round(valor, 2) o 2 dentro dos parênteses é a quantidade de numeros após o ponto decimal:
resultado_decimais = round(dividir_a_conta, 2)

print(f"Cada pessoa pagar pagará: {resultado_decimais}")

# Lógica:
# total_da_conta + porcentagem_da_gorjeta / pela quantidade_de_pessoas

# resultado =


# Como calcular a porcentagem:
# (pela porcentagem_da_gorjeta / por 100) / * total_da_conta
