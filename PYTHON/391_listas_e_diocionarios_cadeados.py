# Dicionátios em Python

programando_um_dicionário = {
    "Bug": "Um erro em um programa que impede que o programa funcione como esperado.",

    "Function": "Um pedaço de código que você pode chamá-lo ou 'reusá-lo' varias vezes.",
}

# Retrieving items from dictionary.
# print(programming_dictionary["Function"])

# Adding new items to dictionary.
programando_um_dicionário["Loop"] = "O ato de fazer algo várias vezes."

# Create an empty dictionary.
dicionario_vazio = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
programando_um_dicionário["Bug"] = "Uma inseto no computador."
# print(programming_dictionary)

# Loop through a dictionary
# for key in programming_dictionary:
#   print(key)
#   print(programming_dictionary[key])

#######################################

# Nesting
capitais = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary

log_de_viagens = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting Dictionary in a Dictionary

log_de_viagens = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

# Nesting Dictionaries in Lists

log_de_viagens = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]
