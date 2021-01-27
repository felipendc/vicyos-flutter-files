altura = input("Digite a sua altura em metros: ")
peso = input("Digite a sua peso em kg: ")

resultado = float(peso) / (float(altura) * float(altura))
print(resultado)


# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")


# O código acima faz o seguinte calculo:
# peso % altura * altura = resultado

# Em outras palavras:
# 80 ÷ (1.75 x 1.75) = 26.122448979591837

# Antes de dividir o peso pela altura o precisamos multiplicar primeiro a altura * altura
# Pra isso é preciso colocar a altura * altura dentro de parênteses (altura * altura).

# Exemplo:
# 80 ÷ (1.75 x 1.75)
# 80 / 3.0625
# 26.122448979591837
