# "a" É o inicio do loop
# "b" É o fim  do loop mas, não inclui o valor "b".__doc__
# "c" É o passo ou pulador.

# for item in range(a, b, c):
#     fazer_algo...


# ######## #
# Exemplo: #
# ######## #

# O loop vai começar do 1 até o 100 e não 101 pois o último número não é incluso.
# e ele vai pular de 2 em 2.

# for item in range(1, 101, 2):
#     fazer_algo...

for item in range(1, 101, 2):
    print(item)

# Resultado:
# 1
# 3
# 5
# 7
# 9
# 11
# 13
# etc.
