import math
# Função definida!


def cal_latas_de_tintas(altura, largura, cobertura):

    numeros_de_latas = (altura * largura) / cobertura

    # É muito importante usar o math.ceil, pois ele vai arredondar os resultados com
    # números decimais.
    arredondar_resultado = math.ceil(numeros_de_latas)
    print(f'Você vai precisar comprar {arredondar_resultado} latas de tinta.')


# Input do usuário:
parede_altura = int(input("Altura da parede: "))
parede_largura = int(input("Largura da parede: "))

# Cada lata de tinta cobre 5 metros quadrados.
cobre_ate = 5

# Chamando a função!
cal_latas_de_tintas(altura=parede_altura,
                    largura=parede_largura, cobertura=cobre_ate)
