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


resultado_anterior = primeiro_resultado
parar_calculo = False

while not parar_calculo:
    continuar_calculando = input(
        f"Digite 'S' para continuar calculando com o {resultado_anterior} ou digite 'N' para sair ").lower()

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
