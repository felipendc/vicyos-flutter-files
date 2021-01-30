# 🚨 Don't change the code below 👇
print("")
print("Bem vindo ao Entrega de Pizzas do Python!")
print("")
print("P = Pizza Pequena: R$ 15,00")
print("M = Pizza Média: R$ 20,00")
print("G = Pizza Grande: R$ 25,00")
print("")
print("Pepperoni para Pizza Pequena: R$ 2,00")
print("Pepperoni para Pizza Média ou Grande: R$ 3,00")
print("Queijo extra para qualquer tamanho: R$ 1,00")
print("")

tamanho = input("Qual é o tamanho da Pizza que você quer? P, M, ou G ")
adicionar_pepperoni = input("Você quer adicionar pepperoni? S ou N ")
extra_queijo = input("Você extra queijo? S ou N ")

pizza_pequena = 15
pizza_media = 20
pizza_grande = 25

pepperoni_pequeno = 2
pepperoni_medio = 3
pepperoni_grande = 3

quer_extra_queijo = 1

conta = 0

if tamanho == "P" or tamanho == "p":
    conta += pizza_pequena
    if adicionar_pepperoni == "S" or adicionar_pepperoni == "s":
        conta += pepperoni_pequeno
    if extra_queijo == "S" or extra_queijo == "s":
        conta += quer_extra_queijo

if tamanho == "M" or tamanho == "m":
    conta += pizza_media
    if adicionar_pepperoni == "S" or adicionar_pepperoni == "s":
        conta += pepperoni_medio
    if extra_queijo == "S" or extra_queijo == "s":
        conta += quer_extra_queijo

if tamanho == "G" or tamanho == "g":
    conta += pizza_grande
    if adicionar_pepperoni == "S" or adicionar_pepperoni == "s":
        conta += pepperoni_grande
    if extra_queijo == "S" or extra_queijo == "s":
        conta += quer_extra_queijo

print(f"O total da sua conta é: R$ {conta},00")
