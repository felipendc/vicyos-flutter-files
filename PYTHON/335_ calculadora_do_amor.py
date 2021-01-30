
print("Welcome to the Love Calculator!")
nome1 = input("Qual é o seu nome? \n")
nome2 = input("Qual é o nome dela / dele? \n")


# Colocar as letras para minúsculas
nome1_lower = nome1.lower()
nome2_lower = nome2.lower()

# Amarzena o total de letras que se repetem:
nome_1_true = 0
nome_2_true = 0

nome_1_love = 0
nome_2_love = 0

# Quantidades que as letras T R U E se repetem no nome 1:
# Adicional: o contra-barra está sendo usado aqui para eu poder pular a linha
# mas, para o enterpretador é com se o código continuasse na mesma linha:
nome_1_true += nome1_lower.count("t") + \
    nome1_lower.count("r") + \
    nome1_lower.count("u") + \
    nome1_lower.count("e")

# Quantidades que as letras T R U E se repetem no nome 2:
# Adicional: o contra-barra está sendo usado aqui para eu poder pular a linha
# mas, para o enterpretador é com se o código continuasse na mesma linha:
nome_2_true += nome2_lower.count("t") + \
    nome2_lower.count("r") + \
    nome2_lower.count("u") + \
    nome2_lower.count("e")


# Quantidades que as letras L O V E se repetem no nome 1:
# Adicional: o contra-barra está sendo usado aqui para eu poder pular a linha
# mas, para o enterpretador é com se o código continuasse na mesma linha:
nome_1_love += nome1_lower.count("l") + \
    nome1_lower.count("o") + \
    nome1_lower.count("v") + \
    nome1_lower.count("e")

# Quantidades que as letras L O V E se repetem no nome 2
# Adicional: o contra-barra está sendo usado aqui para eu poder pular a linha
# mas, para o enterpretador é com se o código continuasse na mesma linha:
nome_2_love += nome2_lower.count("l") + \
    nome2_lower.count("o") + \
    nome2_lower.count("v") + \
    nome2_lower.count("e")

total_de_true = nome_1_true + nome_2_true
total_de_love = nome_1_love + nome_2_love

# JUNTAR O TOTAL DE "total_de_true" com o  "total_de_love" usando o F-"STRING" do Python
# e transformando-o em um numero inteiro para eu poder fazer cálculos matemáticos com ele, caso for preciso.
total_true_e_love = int(f"{total_de_true}{total_de_love}")


if total_true_e_love < 10 or total_true_e_love > 90:
    print(
        f"A sua potutação é: {total_true_e_love}, Vocês são como Coca-Cola e Mentos! hahaha.")

elif total_true_e_love >= 40 and total_true_e_love <= 50:
    print(
        f"A sua potutação é: {total_true_e_love}, Vocês formam um ótimo casal!")
else:
    print(
        f"Ah... Que pena! A sua potutação é: {total_true_e_love}. Boa sorte na procura do seu amor...")
