pontuacao_dos_alunos = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

nota_dos_alunos = {}

for chave in pontuacao_dos_alunos:
    if pontuacao_dos_alunos[chave] <= 70:
        nota_dos_alunos[chave] = 'Reprovou'

    elif pontuacao_dos_alunos[chave] <= 80:
        nota_dos_alunos[chave] = 'Aceitável'

    elif pontuacao_dos_alunos[chave] <= 80:
        nota_dos_alunos[chave] = 'Aceitável'

    elif pontuacao_dos_alunos[chave] <= 90:
        nota_dos_alunos[chave] = 'Excedeu as expectativas'

    elif pontuacao_dos_alunos[chave] <= 100:
        nota_dos_alunos[chave] = 'Excepcional'

print(nota_dos_alunos)
