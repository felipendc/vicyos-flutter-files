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

# O resultado será:
# nota_dos_alunos = {
# 'Harry': 'Exceeds Expectations',
# 'Ron': 'Acceptable',
# 'Hermione': 'Outstanding',
# 'Draco': 'Acceptable',
# 'Neville': 'Fail'
# }


#########################################################
###### OUTRA MANEIRA DE ESCREVER O MESMO CÓDIGO! ########

# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# #Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# #TODO-2: Write your code below to covert scores into grades.👇
# for student in student_scores:
#   score = student_scores[student]
#   if score > 90:
#     student_grades[student] = "Outstanding"
#   elif score > 80:
#     student_grades[student] = "Exceeds Expectations"
#   elif score > 70:
#     student_grades[student] = "Acceptable"
#   else:
#     student_grades[student] = "Fail"


# #Don't change the code below 👇
# print(student_grades)
