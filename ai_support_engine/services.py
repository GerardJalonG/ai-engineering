from .data import pedidos

def buscar_pedido(id_pedido):
    for pedido in pedidos:
        if pedido.get("id") == id_pedido:
            return pedido
    return None

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
