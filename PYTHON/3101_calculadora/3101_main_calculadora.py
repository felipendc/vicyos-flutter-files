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

decisao_do_usuario = input(
    f"Digite 'S' para continuar calculando com o {primeiro_resultado} ou digite 'N' para sair ").lower()

if decisao_do_usuario == 's':

    nao_continuar = False
    while not nao_continuar:

        reatualizar_resultado = primeiro_resultado
        simbolo_da_operacao = input('Escolha escolha outra operação: ')
        numero3 = int(input('Qual é o próximo número?: '))

        funcao_escolhida = operadores[simbolo_da_operacao]
        segundo_resultado = funcao_escolhida(reatualizar_resultado, numero3)
        reatualizar_resultado = segundo_resultado

        print(
            f"{segundo_resultado} {simbolo_da_operacao} {numero3} = {segundo_resultado}")

        decisao_do_usuario = input(
            f"Digite 'S' para continuar calculando com o {reatualizar_resultado} ou digite 'N' para parar ").lower()

        if decisao_do_usuario == 'n':
            nao_continuar = True
