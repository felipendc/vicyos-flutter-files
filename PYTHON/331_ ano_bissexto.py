ano = int(input("Qual ano você gostaria de checar? "))


# Se o ano selecionado dividido por 400 é igual a 0, ele é um ano bissexto:
# Se o ano não for divisível por 4 mas for divisível por 4 e não for divisivel por 100,e ele é um ano bissexto:

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f"{ano} é um ano bissexto")
        else:
            print(f"{ano} não é um ano bissexto")
    else:
        print(f"{ano} não é um ano bissexto")
else:
    print(f"{ano} não é um ano bissexto")
