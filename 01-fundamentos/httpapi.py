# import requests

# url = "https://jsonplaceholder.typicode.com/users/2"

# respuesta = requests.get(url, timeout=10)

# print(respuesta.status_code)

# if respuesta.status_code == 200:
#     datos = respuesta.json()

#     print(datos["name"])
#     print(datos["email"])
#     print(datos["address"]["city"])


# ### EJERCICIO 1


# url = "https://jsonplaceholder.typicode.com/users/2"

# respuesta = requests.get(url, timeout=10)

# print(respuesta.status_code)

# if respuesta.status_code == 200:
#     datos = respuesta.json()

#     print(datos["name"])
#     print(datos["email"])
#     print(datos["address"]["city"])
# else:
#     print(f'Error {respuesta.status_code}')
    
### EJERCICIO 5.3

import requests

url = "https://jsonplaceholder.typicode.com/users/2"

try:
    respuesta = requests.get(url, timeout=10)
    
    if respuesta.status_code == 200:
        data = respuesta.json()
        print(data["name"])
    else:
        print(respuesta.status_code)
except requests.exceptions.ConnectionError:
    print("Error de conexion")
except requests.exceptions.Timeout:
    print("Error de timeout")