def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)


numero_inserido = int(
    input("Digite o número de vezes que a chamada recursiva ocorrerá: "))

soma = fatorial(numero_inserido)


print("O fatorial do número digitado é {}".format(soma))
input("\nAperte ENTER para sair...")
