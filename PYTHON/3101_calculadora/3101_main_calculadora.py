import art
import os
# Calculadora


def adicao(n1, n2):
    return n1 + n2


def subitracao(n1, n2):
    return n1 - n2


def multiplicacao(n1, n2):
    return n1 * n2


def divisao(n1, n2):
    return n1 / n2


# Dicionário:
operadores = {
    '+': adicao,
    '-': subitracao,
    '*': multiplicacao,
    '/': divisao,
}


def calculadora():
    # Essa é uma Docstring. Ela serve para documentar a função.
    # Ou pra descrever pra que a função serve.
    """Essa função serve para fazer calculos matemáticos básicos."""

    os.system('cls') or None
    print(art.logo)
    numero1 = float(input('Qual é o primeiro número?: '))

    # Loopar dentro do dicionário "operadores" e imprimir o valores das chaves.
    for chave in operadores:
        print(chave)

    simbolo_da_operacao = input('Escolha uma das operações acima: ')
    numero2 = float(input('Qual é o segundo número?: '))

    funcao_escolhida = operadores[simbolo_da_operacao]
    primeiro_resultado = funcao_escolhida(numero1, numero2)

    print(f"{numero1} {simbolo_da_operacao} {numero1} = {primeiro_resultado}")

    resultado_anterior = primeiro_resultado

    # "parar_calculo" é uma FLAG que mantém o while loop rodando.
    parar_calculo = False
    while not parar_calculo:
        continuar_calculando = input(
            f"Digite 'S' para continuar calculando com o {resultado_anterior} ou digite 'N' para iniciar uma nova calculadora: ").lower()

        if continuar_calculando == 's':
            simbolo_da_operacao = input('Escolha escolha outra operação: ')
            numero3 = int(input('Qual é o próximo número?: '))

            funcao_escolhida = operadores[simbolo_da_operacao]
            resultado_atual = funcao_escolhida(resultado_anterior, numero3)

            print(
                f"{resultado_anterior} {simbolo_da_operacao} {numero3} = {resultado_atual}")
            resultado_anterior = resultado_atual
        else:
            parar_calculo = True
            calculadora()


calculadora()


# Chamada Recursiva é quando chamamos uma função dentro dela mesma.
# Como no caso da função da calculadora!


#####################################################
###### OUTRA MANEIRA DE ESCREVER O CÓDIGO ##########

# from art import logo
# from replit import clear

# def add(n1, n2):
#   return n1 + n2


# def subtract(n1, n2):
#   return n1 - n2


# def multiply(n1, n2):
#   return n1 * n2


# def divide(n1, n2):
#   return n1 / n2


# operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide
# }


# def calculator():
#   print(logo)

#   num1 = float(input("What's the first number?: "))
#   for symbol in operations:
#     print(symbol)
#   should_continue = True

#   while should_continue:
#     operation_symbol = input("Pick an operation: ")
#     num2 = float(input("What's the next number?: "))
#     calculation_function = operations[operation_symbol]
#     answer = calculation_function(num1, num2)
#     print(f"{num1} {operation_symbol} {num2} = {answer}")

#     if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
#       num1 = answer
#     else:
#           should_continue = False
#       clear()
#       calculator()


# calculator()
