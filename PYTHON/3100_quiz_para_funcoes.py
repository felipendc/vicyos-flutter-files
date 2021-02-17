# Questão número 1:
# Sem rodar o código, oque você acha que será printado na tela?

def adicao(n1, n2):
    return n1 + n2


def subtrair(n1, n2):
    return n1 - n2


def multiplicacao(n1, n2):
    return n1 * n2


def divisao(n1, n2):
    return n1 / n2


print(adicao(2, multiplicacao(5, divisao(8, 4))))

# Dica:
# As funções são chamadas do mais interno para o mais externo.
# Então, 1. divisão, 2 multiplicação, 3. adiciao.
# Será 12.0


#####################################################
# Questão 2:
# Ao rodar o seguinte código, oque você acha que será imprimido na tela?


def funcao_de_fora(a, b):
    def funcao_de_dentro(c, d):
        return c + d
    return funcao_de_dentro(a, b)


resultado = funcao_de_fora(5, 10)
print(resultado)
# Resposta: 15


#####################################################
# Questão 3
# Oque será imprimido no console depois de rodar o seguinte código?

def minha_funcao(a):
    if a < 40:
        return
        print("Terrível!")
    if a < 80:
        return "Passou"
    else:
        return "Ótimo"


print(minha_funcao(25))
# Resposta: None
