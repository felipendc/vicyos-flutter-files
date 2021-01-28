# 🚨 Don't change the code below 👇
numero = int(input("Qual é o número que você gostaria de checar? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

resultado = numero % 2

if resultado == 0:
    print(f"{numero} é um número par")
else:
    print(f"{numero} é um número impar")
