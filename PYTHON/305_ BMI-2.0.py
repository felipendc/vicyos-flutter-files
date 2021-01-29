# Converte a vareável "altura" de String para float:
altura = float(input("Digite a sua altura em metros: "))

# Converte a vareável peso" de String para float:
peso = float(input("Digite a sua peso em kg: "))

# Divide o peso pela altura ao quatrado.
# Aredondar o resultado para o número inteiro mais próximo usando o round().
bmi = round(peso / altura ** 2)
# Opcional: bmi = float(peso) / altura ** 2


if bmi <= 18.5:
    print(f"Your BMI is {bmi}, você está abaixo do peso.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, você tem um peso normal.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, você está um pouco acima do peso.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, você está obeso.")
else:
    print(f"Your BMI is {bmi}, você está críticamente obeso!.")
