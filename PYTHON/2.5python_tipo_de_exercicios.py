# Recebe os valores que o usuário inseriu:
two_digit_number = input("Digite um valor com dois números: ")

# Converte os dois números que o usuário inseriu para Inteiro
# e soma o primeiro digito com o segundo e printa o resultado na tela.
print(int(two_digit_number[0]) + int(two_digit_number[1]))


# Exemplo:
# 55 = 10

# index0 + index1 = 10
# 5 + 5 = 10


# Uma outra maneira de fazer o mesmo código:
# Aqui eu peço para o usuário digitar um valor com dois números:
two_digit_number = input("Digite um valor com dois números: ")

# Aqui eu pego o primeiro digito do valor que o usuário inseriu:
first_digit = two_digit_number[0]

# Aqui eu pego o segundo digito do valor que o usuário inseriu:
second_digit = two_digit_number[1]

# Aqui eu converto os valores da posição 1 e 2 que o usuário inserio para o formato de números inteiros.
# E eu somo "+" o primeiro digito com o segundo.
result = int(first_digit) + int(second_digit)

# Aqui eu imprimo na tela o a soma dos digitos da posição 1 com a posição 2:
print(result)


# A primeira opção é menos verbosa e direta. Mas, tem suas limitações.

# A segunda opção é mais verbosa e mais precisa.
# Pois, dessa forma eu ainda posso manipular ou modificar as vareáveis "first_digit" e "second_digits"
# em uma parte específica do código.
