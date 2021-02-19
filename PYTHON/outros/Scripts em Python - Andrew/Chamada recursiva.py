def fatorial(numero):
    print(numero)
    if numero > 1:
        numero -= 1

        # A chamada recursiva acontece aqui. Pois, eu estou chamando a função 'fatorial()' dentro dela mesma.
        # Assim, ocorrendo um loop até que o valor seja menor que 1.
        fatorial(numero)


numero_escolhido = int(
    input("Digite o número de vezes que a chamada recursiva ocorrerá: "))

fatorial(numero_escolhido)

input("\nAperte ENTER para sair...")
