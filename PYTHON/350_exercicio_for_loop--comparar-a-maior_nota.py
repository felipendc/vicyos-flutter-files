nota_dos_estudantes = input(
    "Insira uma lista de notas dos estudantes: ").split()
for n in range(0, len(nota_dos_estudantes)):
    nota_dos_estudantes[n] = int(nota_dos_estudantes[n])
print(nota_dos_estudantes)

# Vai armazenar cada nota:
comparar = 0

# Vai armazenar a maior nota:
maior_nota = 0

for notas in nota_dos_estudantes:

    # Cada elemento de "nota_dos_estudantes" será armazenado na vareável "comparar".
    comparar = notas

    # Logo em seguida, eu vou comparar os valores que estão nas vareáveis "comparar" e "maior_nota"
    # E, eu verifico se o valor dentro da vareável "comparar" é maior que o valor dentro da vareável "maior_nota".
    if comparar >= maior_nota:

        # Caso seja maior, eu vou copiar o valor da vareável "comparar" para a vareável "maior_numero"
        # E, eu vou fazer essa comparação para cada elemento dentro da vareável "nota_dos_estudantes".
        maior_nota = comparar

# Imprimi na tela a maior nota entre os estudantes da classe:
print(f'A maior nota entre os estudantes da classe é: {maior_nota}')

############################# NOTA! IMPORTANTE #######################################
# É muito importante prestar atenção na posição em que você monta a lógica do código!
# if comparar >= maior_nota: Terá um resultado.
# if maior_nota >= comparar: Terá um resultado reverso!
######################################################################################


###################################################
#### Outra maneira de escrever a mesma lógica #####
###################################################

# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# highest_score = 0
# for score in student_scores:
#   if score > highest_score:
#     highest_score = score
#     # print(highest_score)

# print(f"The highest score in the class is: {highest_score}")
