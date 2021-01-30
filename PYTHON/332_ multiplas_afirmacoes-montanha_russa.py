print("Bem vindo ao  Montanha-russa!")
altura = int(input("Qual é a sua altura em cm? "))
conta = 0

if altura >= 120:
    print("Você pode andar na montanha-russa!")
    idade = int(input("Qual é a sua idade? "))
    if idade < 12:
        conta = 5
        print("Ingressos para crianças é R$ 5,00.")
    elif idade <= 18:
        conta = 7
        print("Ingresso para juvenis são R$ 7,00.")
    elif idade >= 45 and idade <= 55:
        print("Tudo vai ficar bem. Dê uma volta conosco!")
    else:
        conta = 12
        print("Ingressos para adultos são R$ 12,00.")

    quer_foto = input("Você quer tirar uma foto? S ou N. ")
    if quer_foto == "S" or quer_foto == "s":
        conta += 3

    print(f"A sua conta final é: R$ {conta},00")

else:
    print("Desculpe, Você deve crescer mais pra poder dar uma volta.")
