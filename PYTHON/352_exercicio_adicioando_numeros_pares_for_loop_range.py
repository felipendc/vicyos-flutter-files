
soma_dos_numeros_pares = 0

for pares in range(1, 101):

    if pares % 2 == 0:
        soma_dos_numeros_pares += pares
        # print(soma_dos_numeros_pares)

print(soma_dos_numeros_pares)

########################################
### OU EU POSSO ESCREVER DESSA FORMA ###
########################################

# Eu sei que 0 a 101 = 100 pois o 101 não é incluso!
# Por isso que eu coloquei 102. Pois, o pois ele vai contar até 101. se ele não contar até 101
# o for loop não vai fazer a soma correta. Ao invés de ser 2550, ficaria 2450. Poir isso eu acrescentei
# mais um ao 101. ficando 102.

# soma_dos_numeros_pares = 0

# for pares in range(0, 101, 2):
#     if pares % 2 == 0:
#         soma_dos_numeros_pares += pares
#         # print(soma_dos_numeros_pares)

# print(soma_dos_numeros_pares)


############## NOTA #################
# USAR O PROGRAMA THONY LHE AJUDARÁ
# A ENTENDER COM O CÓDIGO FUNCIONA
# DE UMA FORMA MUITO MAIS FÁCIL!.
#####################################


########################################################
# MAIS FORMAS DE ESCREVER A MESMA LÓGICA DO CÓDIGO.
########################################################


# #Write your code below this row 👇

# even_sum = 0
# for number in range(2, 101, 2):
#   # print(number)
#   even_sum += number
# print(even_sum)

# #or

# alternative_sum = 0
# for number in range(1, 101):
#   if number % 2 == 0:
#     # print(number)
#     alternative_sum += number
# print(alternative_sum)
