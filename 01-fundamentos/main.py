
pedidos = [
    {
        "id": 1001,
        "cliente": "Carlos",
        "estado": "enviado",
        "total": 89.90
    },
    {
        "id": 1002,
        "cliente": "Laura",
        "estado": "pendiente",
        "total": 45.50
    },
    {
        "id": 1003,
        "cliente": "Miguel",
        "estado": "entregado",
        "total": 120.00
    },
    {
    "cliente": "Pedro",
    "estado": "pendiente",
    "total": 25.00
    }
]
### EJERCICIO 1: Crear una función que reciba un id de pedido y devuelva el pedido correspondiente.
def buscar_pedido(id_pedido):
    for pedido in pedidos:
        if pedido["id"] == id_pedido:
            return pedido
    return None

print(buscar_pedido(1001))
print(buscar_pedido(10))

### EJERCICIO 2 Elemento sin codigo con KeyError exception

def buscar_pedido_v2(id_pedido):
    for pedido in pedidos:
        if pedido.get("id") == id_pedido:
            return pedido
    return None

print(buscar_pedido_v2(1001))
print(buscar_pedido_v2(10))
