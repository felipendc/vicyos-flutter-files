teste = {
    "name": "Redmi K20 Pro/Mi 9T Pro",
    "brand": "Xiaomi",
    "codename": "raphael",
    "supported_versions": [
        {
            "version_code": "eleven",
            "xda_thread": "",
            "stable": "false"
        },
        {
            "version_code": "ten",
            "xda_thread": "https://forum.xda-developers.com/k20-pro/development/rom-pixel-experience-t4014141",
            "deprecated": "true"
        },
        {
            "version_code": "ten_plus",
            "xda_thread": "https://forum.xda-developers.com/k20-pro/development/rom-pixel-experience-t4014141",
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
print(teste["supported_versions"][0]["stable"])

# Printar o valor da cada chave do dicionário que está dentro de uma lista na posisão 1:
print(teste["supported_versions"][1]["version_code"])
print(teste["supported_versions"][1]["xda_thread"])
print(teste["supported_versions"][1]["deprecated"])

# Printar o valor da cada chave do dicionário que está dentro de uma lista na posisão 2:
print(teste["supported_versions"][1]["version_code"])
print(teste["supported_versions"][1]["xda_thread"])
print(teste["supported_versions"][1]["deprecated"])
