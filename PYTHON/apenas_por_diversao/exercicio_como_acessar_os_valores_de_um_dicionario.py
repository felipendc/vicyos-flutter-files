teste = {
    "name": "Redmi K30/Poco X2",
    "brand": "Xiaomi",
    "codename": "phoenix",
    "supported_versions": [
        {
            "version_code": "ten",
            "xda_thread": "https://forum.xda-developers.com/poco-x2/development/rom-pixel-experience-t4073897",
            "deprecated": "true"
        },
        {
            "version_code": "ten_plus",
            "xda_thread": "https://forum.xda-developers.com/poco-x2/development/rom-pixel-experience-t4073897",
            "deprecated": "true"
        }
    ]
}


# Printar o valor da cada chave:
print(teste["name"])
print(teste["brand"])
print(teste["codename"])
print(teste["supported_versions"])

# Printar o valor da cada chave do dicionário que está dentro de uma lista na posisão 0:
print(teste["supported_versions"][0]["version_code"])
print(teste["supported_versions"][0]["xda_thread"])
print(teste["supported_versions"][0]["deprecated"])

# Printar o valor da cada chave do dicionário que está dentro de uma lista na posisão 1:
print(teste["supported_versions"][1]["version_code"])
print(teste["supported_versions"][1]["xda_thread"])
print(teste["supported_versions"][1]["deprecated"])
