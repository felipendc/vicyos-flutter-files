
# Definindo a função!
def cal_latas_de_tintas(altura, largura, cobertura):

    numeros_de_latas = (altura * largura) / cobertura
    arredondar_resultado = round(numeros_de_latas)
    print(arredondar_resultado)


# Input do usuário:
parede_altura = int(input("altura da parede: "))
parede_largura = int(input("Largura da parede: "))
cobre_ate = 5

# Chamando a função!
cal_latas_de_tintas(altura=parede_altura,
                    largura=parede_largura, cobertura=cobre_ate)
