import json

respuesta_api = '''
{
    "success": true,
    "data": {
        "id": 1001,
        "cliente": "Carlos",
        "estado": "enviado",
        "total": 89.90
    }
}
'''

### Ejercicio 1

api_data = json.loads(respuesta_api)
# if api_data["success"] ? print("Es true") : 
if api_data["success"] == True:
    data = api_data["data"]
    cliente = data["cliente"]
    estado = data["estado"]
    total = data["total"]
    print(f'Cliente {cliente}, Estado: {estado}, Total {total}')
    
else:
    print("Error al consultar el pedido")
    
    
### Ejercicio 2
pedido = {
    "id": 1002,
    "cliente": "Laura",
    "estado": "pendiente",
    "total": 45.50
}

respuesta = {
    "success": True,
    "data": pedido
}

respuesta_json = json.dumps(respuesta)
print(respuesta_json)
print(type(respuesta_json))