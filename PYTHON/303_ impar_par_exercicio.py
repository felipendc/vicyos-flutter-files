# Verifica se o número inserido pelo usuário é par ou impar:

# Estrutura do calculo:
# Usar o módulo para dividir o número inserido por 2. Se o resultado for 0, o número é par,
# caso contrário, o número é impar.


numero = int(input("Qual é o número que você gostaria de checar? "))

resultado = numero % 2

if resultado == 0:
    print(f"{numero} é um número par")
else:
    print(f"{numero} é um número impar")
