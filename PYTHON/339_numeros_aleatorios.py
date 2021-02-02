import random  # Para usar números aleatórios.
import os  # Para eu poder interagir com o computador (Windows)

# Limpar a tela do terminal
os.system('cls') or None

# Criar um número int aleatório entre 1 e 10 e incluindo 1 e 10:
inteiro_aleatorio = random.randint(1, 10)

print(f"inteiro_aleatorio entre 1 a 10: {inteiro_aleatorio}\n")

# Criar um número float aleatório entre 0.1 e 1.0 mas, não incluindo o 1.0:
float_aleatorio = random.random()
print(
    f"float_aleatorio entre 0.1 a 1.0 (mas, não incluindo o 1.0): {float_aleatorio}\n")

# Para expandir os números aleatórios de 0.1 1.0 pra 0.1 para 0.5, é só
# multiplicar o valor por 5 mas, não vai incluir o 0.5:
print(float_aleatorio * 5)
