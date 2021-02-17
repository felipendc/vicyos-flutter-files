import requests     #Para requisitar as informações da API IP Info
import webbrowser   #Para abrir o site do Google Maps mostrando a localização

#Para requisitar as informações da API e atribuí-las a um dicionário
res = requests.get("https://ipinfo.io/")    #Site da API de geolocalização, vale a pena ler a documentação
dados = res.json()

print("Informações dos dados:\n", dados)     #Imprime os dados do local onde estamos
print("\nOs dados são do tipo {}\n".format(type(dados)))   #Mostra que dados é um dicionário

#Percorre todos os ítens do dicionário e imprime-os na tela
for i in dados:
    print("{}: {}".format(i, dados[str(i)]))

#Para dividir a localização entre latitude e longitude
localizacao = dados["loc"].split(",")
latitude = float(localizacao[0])
longitude = float(localizacao[1])

#Imprime latitude e longitude
print("\nLatitude:", latitude)
print("Longitude:", longitude)

#Abre o navegador de internet no Google Maps com as coordenadas de latitude e longitude
#   obtidas pela API IP Info, new=2 é uma instrução para abrir em uma nova aba
webbrowser.open('www.google.com.br/maps/@{},{}'.format(latitude, longitude), new=2)

input("\nAperte ENTER para sair...")