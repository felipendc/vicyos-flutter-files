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
    '/': multiplicacao,
}

numero1 = int(input('Qual é o primeiro número?: '))

for chave in operadores:
    print(chave)


simbolo_da_operacao = input('Escolha uma das operações acima: ')
numero2 = int(input('Qual é o segundo número?: '))

funcao_escolhida = operadores[simbolo_da_operacao]

primeiro_resultado = funcao_escolhida(numero1, numero2)

print(f"{numero1} {simbolo_da_operacao} {numero1} = {primeiro_resultado}")

simbolo_da_operacao = input('Escolha escolha outra operação: ')
numero3 = int(input('Qual é o próximo número?: '))

funcao_escolhida = operadores[simbolo_da_operacao]
segundo_resultado = funcao_escolhida(primeiro_resultado, numero3)
print(f"{primeiro_resultado} {simbolo_da_operacao} {numero3} = {segundo_resultado}")
