
# # pedidos = [
# #     {"id": 1001, "cliente": "Carlos", "estado": "enviado", "total": 89.90},
# #     {"id": 1002, "cliente": "Laura", "estado": "pendiente", "total": 45.50},
# #     {"id": 1003, "cliente": "Miguel", "estado": "entregado", "total": 120.00},
# #     {"id": 1004, "cliente": "Ana", "estado": "pendiente", "total": 65.00},
# #     {"id": 1005, "cliente": "Pedro", "estado": "enviado", "total": 35.50}
# # ]

# ### EJERCICIO 1

# # def filtrar_pedidos(estado):
# #     pedidos_filtrados = []
# #     for pedido in pedidos:
# #         if pedido.get("estado") == estado:
# #             pedidos_filtrados.append(pedido)
# #     return pedidos_filtrados

# ### EJERCICIO 3

# def calcular_total(estado):
#     total = 0
#     pedidos_filtrados = filtrar_pedidos(estado)
#     for pedido in pedidos_filtrados:
#         total += pedido["total"]
#     return total

# if __name__ == "__main__":
#     print(filtrar_pedidos("pendiente"))
#     print(filtrar_pedidos("enviado"))
#     print(filtrar_pedidos("cancelado"))