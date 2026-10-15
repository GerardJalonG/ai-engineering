from .services import buscar_pedido, filtrar_pedidos, calcular_total

print(buscar_pedido(1001))
print(filtrar_pedidos("pendiente"))
print(calcular_total("enviados"))
