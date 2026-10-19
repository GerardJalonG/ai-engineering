from .data import pedidos

def buscar_pedido(id_pedido):
    for pedido in pedidos:
        if pedido.get("id") == id_pedido:
            return pedido
    return None

def listar_pedidos():
    return pedidos

def filtrar_pedidos(estado):
    pedidos_filtrados = []
    for pedido in pedidos:
        if pedido.get("estado") == estado:
            pedidos_filtrados.append(pedido)
    return pedidos_filtrados


def calcular_total(estado):
    total = 0
    pedidos_filtrados = filtrar_pedidos(estado)
    for pedido in pedidos_filtrados:
        try:
            float_total = float(pedido.get("total"))
            total += float_total
        except (ValueError, TypeError):
            print(f'Importe invalido en el pedido {pedido["id"]}')
    return total


def crear_pedido(datos: dict) -> dict:

    ids = []

    for pedido in pedidos:
        ids.append(pedido["id"])

    nuevo_id = max(ids) + 1

    nuevo_pedido = {
        "id": nuevo_id,
        "cliente": datos["cliente"],
        "estado": datos["estado"],
        "total": datos["total"]
    }

    pedidos.append(nuevo_pedido)

    return nuevo_pedido