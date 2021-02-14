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


######################################################
####  OUTRA MANEIRA DE ESCREVER O MESMO CÓDIGO:  #####


# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"]
#     },
# ]
# #DO NOT change the code above 👆

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log.


# def add_new_country(name, visit_count, cities_visited):
#   new_country = {}
#   new_country["country"] = name
#   new_country["visits"] = visit_count
#   new_country["cities"] = cities_visited
#   travel_log.append(new_country)


# #Do not change the code below 👇
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)
