
# print("Welcome to the Love Calculator!")
# nome1 = input("Qual é o seu nome? \n")
# nome2 = input("Qual é o nome dela / dele? \n")

nome1 = "Angela Yu"
nome2 = "Jack Bauer"

# Colocar as letras para minúsculas
nome1_lower = nome1.lower()
nome2_lower = nome2.lower()

# Amarzena o total de letras que se repetem:
nome_1_true = 0
nome_2_true = 0

nome_1_love = 0
nome_2_love = 0

# Quantidades que as letras T R U E se repetem no nome 1
nome_1_true += nome1_lower.count("t") + \
    nome1_lower.count("r") + \
    nome1_lower.count("u") + \
    nome1_lower.count("e")

# Quantidades que as letras T R U E se repetem no nome 2
nome_2_true += nome2_lower.count("t") + \
    nome2_lower.count("r") + \
    nome2_lower.count("u") + \
    nome2_lower.count("e")


# Quantidades que as letras L O V E se repetem no nome 1
nome_1_love += nome1_lower.count("l") + \
    nome1_lower.count("o") + \
    nome1_lower.count("v") + \
    nome1_lower.count("e")

# Quantidades que as letras L O V E se repetem no nome 2
nome_2_love += nome2_lower.count("l") + \
    nome2_lower.count("o") + \
    nome2_lower.count("v") + \
    nome2_lower.count("e")

total_de_true = nome_1_true + nome_2_true
total_de_love = nome_1_love + nome_2_love

# JUNTAR O TOTAL DE "total_de_true" com o  "total_de_love" usando o F-"STRING" do Python
# e transformando-o em um numero inteiro para eu poder fazer cálculos matemáticos com ele, caso for preciso.
juntar_true_e_love = int(f"{total_de_true}{total_de_love}")


# Testar a saída código
print(f"total de true: {total_de_true}")
print(f"total de love: {total_de_love}")
print(f"total de true e love: {juntar_true_e_love}")
