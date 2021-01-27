altura = input("Digite a sua altura em metros: ")
peso = input("Digite a sua peso em kg: ")

# Converte as vareáveis "altura" e "peso" de String para float:
bmi = float(peso) / (float(altura) * float(altura))
# Opcional: bmi = float(peso) / altura ** 2


# Converter os números float para inteiros:
bmi_as_int = int(bmi)

# Printar a resposta com números inteiros:
print(bmi_as_int)


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
