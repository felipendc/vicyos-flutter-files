# Dicionátios em Python

programando_um_dicionário = {
    "Bug": "Um erro em um programa que impede que o programa funcione como esperado.",

    "Funcao": "Um pedaço de código que você pode chamá-lo ou 'reusá-lo' varias vezes.",
}

# buscando 'pegando' itens dentro de um dictionário.
# print(programando_um_dicionário["Funcao"])

# Adicionar novos itens a um dicionário.
programando_um_dicionário["Loop"] = "O ato de fazer algo várias vezes."

# Criar um dicionário vazio.
dicionario_vazio = {}

# Limpar ou esvaziar um cionário
# programando_um_dicionário = {}
# print(programando_um_dicionário)

# Editar um item dentro de um dicionário
programando_um_dicionário["Bug"] = "Uma inseto no computador."
# print(programando_um_dicionário)

# Iterar (loop) dentro de um dicionário
# printar a chave dentro de programando_um_dicionário:
#   print(key)
#   print(programando_um_dicionário[key])

#######################################

# Nesting
capitais = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Alinhando uma lista dentro de um dicionário

log_de_viagens = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Alinhando dicionários dentro de dicionários

log_de_viagens = {
    "France": {"cidades_visitadas": ["Paris", "Lille", "Dijon"], "total_de_visitas": 12},
    "Germany": {"cidades_visitadas": ["Berlin", "Hamburg", "Stuttgart"], "total_de_visitas": 5},
}

# Alinhando dicionários dentro de listas

log_de_viagens = [
    {
        "country": "France",
        "cidades_visitadas": ["Paris", "Lille", "Dijon"],
        "total_de_visitas": 12,
    },
    {
        "country": "Germany",
        "cidades_visitadas": ["Berlin", "Hamburg", "Stuttgart"],
        "total_de_visitas": 5,
    },
]
