# Lista de dicionários
log_de_viagem = [
    {
        "pais": "France",
        "visitas": 12,
        "cidades": ["Paris", "Lille", "Dijon"]
    },
    {
        "pais": "Germany",
        "visitas": 5,
        "cidades": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

# Fução que cria e adiciona um dicionário na lista "add_nova_cidade":


def add_nova_cidade(add_pais, num_de_visitas, cidades_visitadas):

    log_de_viagem.append(
        {
            "pais": add_pais,
            "visitas": num_de_visitas,
            "cidades": cidades_visitadas
        }
    )


# Chamando a função "add_nova_cidade":
add_nova_cidade("Russia", 2, ["Moscow", "Saint Petersburg"])
print(log_de_viagem)


# Esse será o resultado:

# {
#     'pais': 'France',
#     'visitas': 12,
#     'cidades': ['Paris', 'Lille', 'Dijon']
# },
# {
#     'pais': 'Germany',
#     'visitas': 5,
#     'cidades': ['Berlin', 'Hamburg', 'Stuttgart']
# },
# {
#     'pais': 'Russia',
#     'visitas': 2,
#     'cidades': ['Moscow', 'Saint Petersburg']
# }
