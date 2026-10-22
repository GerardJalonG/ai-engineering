from ai_support_engine.services import buscar_pedido, filtrar_pedidos, calcular_total

# assert buscar_pedido(1001)["id"] == 1001
# assert buscar_pedido(999) is None
# assert filtrar_pedidos("cancelado") == []
# assert calcular_total("enviado") == 25.0

def test_buscar_pedido_existente():
    resultado = buscar_pedido(1001)
    assert resultado["id"] == 1001

def test_buscar_pedido_inexistente():
    resultado = buscar_pedido(9999)
    assert resultado is None
    
def test_filtrar_pedidos_pendientes():
    pedidos = filtrar_pedidos("pendiente")

    assert len(pedidos) > 0

    for pedido in pedidos:
        assert pedido["estado"] == "pendiente"

# def test_calcular_total():
#     total_esperado = 95.5
#     resultado = calcular_total("pendiente")
#     assert resultado == total_esperado