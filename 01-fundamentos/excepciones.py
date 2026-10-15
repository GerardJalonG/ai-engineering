pedidos = [
    {"id": 1001, "estado": "pendiente", "total": 45.50},
    {"id": 1002, "estado": "pendiente", "total": "50"},
    {"id": 1003, "estado": "pendiente", "total": "incorrecto"},
    {"id": 1004, "estado": "pendiente", "total": 25.00},
    {
    "id": 1005,
    "estado": "pendiente",
    "total": None
    }
]

def filtrar_pedidos(estado):
    pedidos_filtrados = []
    for pedido in pedidos:
        if pedido.get("estado") == estado:
            pedidos_filtrados.append(pedido)
    return pedidos_filtrados
### EJERCICIO 1

def calcular_total_v2(estado):
    total = 0
    pedidos_filtrados = filtrar_pedidos(estado)
    for pedido in pedidos_filtrados:
        try:
            float_total = float(pedido.get("total"))
            total += float_total
        except (ValueError, TypeError):
            print(f'Importe invalido en el pedido {pedido["id"]}')
    return total


print(calcular_total_v2("pendiente"))
print(calcular_total_v2("enviado"))