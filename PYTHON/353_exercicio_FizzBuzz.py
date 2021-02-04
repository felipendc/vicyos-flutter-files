# Para cada "numero" entre 1 a 100, faça isso:
for numero in range(1, 101):

    # Se o número é divisível por 3 e 5, printa "FizzBuzz".
    if numero % 3 == 0 and numero % 5 == 0:
        print('FizzBuzz')

    # Se o número é divisível por 3 "Fizz".
    elif numero % 3 == 0:
        print("Fizz")

    # Se o número é divisível por 5, printa "Buzz".
    elif numero % 5 == 0:
        print("Buzz")

    # Caso contrário apenas printa o número.
    else:
        print(numero)
