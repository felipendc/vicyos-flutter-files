altura_dos_estudantes = input(
    "Insira uma lista de altura dos estudantes: ").split()
for n in range(0, len(altura_dos_estudantes)):
    altura_dos_estudantes[n] = int(altura_dos_estudantes[n])


soma_das_alturas = 0
for altura in altura_dos_estudantes:
    soma_das_alturas += altura
    print(f'Soma das alturas: {soma_das_alturas}')

quantidate_de_estudantes = 0
for quantidate in altura_dos_estudantes:
    quantidate_de_estudantes += 1
    print(f'Quantidades de estudantes: {quantidate_de_estudantes}')


media_da_altura = round(soma_das_alturas / quantidate_de_estudantes)
print(
    f'Média da altura dos estudantes: {media_da_altura}')
