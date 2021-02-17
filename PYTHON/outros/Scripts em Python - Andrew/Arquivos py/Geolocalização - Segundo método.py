import requests

r = requests.get("https://get.geojs.io/")

ip_request = requests.get("https://get.geojs.io/v1/ip.json")
ipAdd = ip_request.json()["ip"]
print("\n" + ipAdd)

url = "https://get.geojs.io/v1/ip/geo/" + ipAdd + ".json"
geo_request = requests.get(url)
geo_data = geo_request.json()
print(geo_data)

#Para imprimir informações específicas
print("\nLatitude:", geo_data["latitude"])
print("Longitude:", geo_data["longitude"])

print("Cidade:", geo_data["city"])
print("Estado:", geo_data["region"])
print("País:", geo_data["country"])

input("\nAperte ENTER para sair...")