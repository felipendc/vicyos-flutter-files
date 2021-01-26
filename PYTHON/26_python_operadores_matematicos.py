# 3 + 5 = Adição / Soma
# 7 -  4 = Subtração
# 3 * 2 = Mutiplicação
# 6 / 3 = Divisão
# 2 ** 3 = Expoênte

# // =  Parte inteira
# % = Módulo


# Quando temos mais de uma operaçâo matemática na mesma linha de comando
# os operadores * e / serão serão resolvidos primeiramente.

# Veja a baixo a ordem de prioridade matemático:

# PEMDAS:
# Parênteses      ()
# Expoêntes       **
# Multiplicação   *
# Divisão         /
# Adição          +
# Subtração       -


# Ordem PEMDASLR (L = Left, R = Righ)
# ()
# **
# * /
# + -

# Ordem PEMDASLR (L = Left, R = Righ) sendo aplicadas no Python:
# Primeiro ele vai var preferências para o que está dentro dos parênteses:
# ()

# Depois ele vai calcular as equações com Expoêntes:
# **

# No Python Multiplicação e Divisão são igualmente importantes.
# Só que o expoênte do lado esquerdo terá a preferência.
# * /

# No Python Adição e Subtração são igualmente importantes.
# Só que o expoênte do lado esquerdo terá a preferência.
# + -

# Exemplo:

# Ordem PEMDASLR (L = Left, R = Righ)
# ()
# **
# * /
# + -

# Na linha de comando a preferência é do operador que está no lado esquerdo:
# nesse caso seria: o "*"
exemplo_um = print(3 * 3 + 3 / 3 - 3)


# nesse caso seria: o "/"
exemplo_dois = print(3 / 3 + 3 * 3 - 3)

# nesse caso seria: o "/"
exemplo_tres = print(3 * (3 + 3) / 3 - 3)

# exemplo_um:
# 3 * 3 + 3 / 3 - 3
# 9 + 3 / 3 - 3
# 1 + 9 - 3
# 10 - 3
# 7

# exemplo_dois:
# 3 / 3 + 3 * 3 - 3
# 1 + 3 * 3 - 3
# 9 + 1 - 3
# 10 - 3
# 7

# exemplo_tres:
# Nesse caso ele vai dá preferência aos calculos que estão dentro dos parênteses (3 + 3)

# 3 * (3 + 3) / 3 - 3
# 3 * 6 / 3 - 3
# 18 / 3 - 3
# 6 - 3
# 3


# DICA:
# É bom user o programa Thony para ver ordem da execusão do vídeo:

# Thonny
# Python IDE for beginners

# link: https://thonny.org/
