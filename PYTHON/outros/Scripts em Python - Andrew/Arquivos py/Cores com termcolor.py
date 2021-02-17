#https://pypi.org/project/termcolor/
from termcolor import colored

#3 listas com todas as cores, fundos e atributos
cor = ["yellow", "green", "blue", "grey", "magenta", "red", "cyan", "white" ]
fundo = ["on_red", "on_green", "on_yellow", "on_blue", "on_magenta", "on_cyan", "on_white"]
atributos = ["bold", "dark", "underline", "blink", "reverse", "concealed"]

#Imprime com todas de letras
print("Cores:")
for i in cor:
    print(colored(("Cor das letras"), i))

#Imprime com todas de fundo
print("\nFundo:")
for i in fundo:
    print(colored(("Cor de fundo"), None, on_color=i))  #None significa que manterá o branco original

#Imprime com todos os atributos
print("\nAtributos:")
for i in atributos:
    print(colored(("Atributos"), None, attrs=[i]))
# attrs recebe uma lista, ainda que ela só tenha um índice, por isso as chaves

#Imprime todas as combinações entre uma cor, um fundo e um atributo
print("\nTodas as combinações:")
for i in cor:
    for j in fundo:
        for k in atributos:
            print(colored(("Teste com todos"), i, on_color=j, attrs=[k]))

#Veja que há ainda a possibilidade de imprimirmos com vários atributos
print("\nImpressão com vários atributos")
print(colored(("Vários atributos"), "grey", on_color="on_red", attrs=['dark', 'blink', 'concealed']))