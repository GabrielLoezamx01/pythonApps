
# Consumiendo la api de pokemon en get.....

import requests

api = "https://pokeapi.co/api/v2/pokemon/ditto"

response = requests.get(api)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Ocurrio un error al obtener la data de la apí:   ")
    print("")
    print("")
    print("")
    print(api)
    print(response)
    
    