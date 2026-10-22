from fastapi.testclient import TestClient
from ai_support_engine.main import app
from ai_support_engine.data import pedidos
import pytest
import copy


client = TestClient(app)

PEDIDOS_INICIALES = copy.deepcopy(pedidos)


@pytest.fixture
def restaurar_pedidos():
    estado_previo = copy.deepcopy(pedidos)

    # ANTES del test: preparar datos iniciales
    pedidos.clear()
    pedidos.extend(copy.deepcopy(PEDIDOS_INICIALES))

    yield
    pedidos.clear()
    pedidos.extend(copy.deepcopy(PEDIDOS_INICIALES))
    
    
@pytest.fixture
def pedidos_prueba():
    return [
        {"id": 1, "estado": "pendiente"},
        {"id": 2, "estado": "enviado"}
    ]

def test_listar_pedidos():
    response = client.get("/pedidos")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    

def test_buscar_pedido_existente():
    response = client.get("/pedidos/1001")
    
    assert response.status_code == 200
    
    datos = response.json()

    assert datos["id"] == 1001
    assert datos["cliente"]["nombre"] == "Carlos Martínez"

def test_buscar_pedido_inexistente():
    response = client.get("/pedidos/10")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Pedido no encontrado"
    }
    
def test_crear_pedido_total_negativo():
    datos = {
    "cliente": {
        "id": 1,
        "nombre": "Carlos",
        "email": "carlos@example.com"
    },
    "estado": "pendiente",
    "total": -50
    }

    response = client.post("/pedidos", json=datos)
    assert response.status_code == 422

def test_crear_pedido(restaurar_pedidos):
    datos = {
    "cliente": {
        "id": 1,
        "nombre": "Carlos",
        "email": "carlos@example.com"
    },
    "estado": "pendiente",
    "total": 50
    }

    response = client.post("/pedidos", json=datos)
    assert response.status_code == 201
    
    pedido = response.json()
    assert pedido["id"] > 0
    assert pedido["total"] == 50 
    
    response_get = client.get(f"/pedidos/{pedido["id"]}")
    assert response_get.status_code == 200
    
def test_eliminar_de_lista(pedidos_prueba):
    pedidos_prueba.pop(0)
    assert len(pedidos_prueba) == 1


def test_lista_original(pedidos_prueba):
    assert len(pedidos_prueba) == 2
    assert pedidos_prueba[0]["id"] == 1
    
def test_eliminar_pedido(restaurar_pedidos):
    response = client.delete("/pedidos/1001")
    assert response.status_code == 200
    
    response = client.get("/pedidos/1001")
    assert response.status_code == 404
    
def test_pedido_restaurado(restaurar_pedidos):
    response = client.get("/pedidos/1001")
    assert response.status_code == 200
    
    data = response.json()
    assert data["id"] == 1001

def test_actualizar_estado_pedido(restaurar_pedidos):
    datos = {
        "estado": "enviado"
    }
    
    response = client.patch("/pedidos/1001", json=datos)
    assert response.status_code == 200

    response_get = client.get("/pedidos/1001")
    response_json = response_get.json()
    
    assert response.status_code == 200
    assert response_json["estado"] == "enviado"

def test_actualizar_pedido_completo(restaurar_pedidos):
    datos = {
        "cliente": {
            "id": 1,
            "nombre": "Cliente Actualizado",
            "email": "carlos@example.com"
        },
        "estado": "enviado",
        "total": 250.50
    }
    
    response = client.put("/pedidos/1001", json=datos)
    assert response.status_code == 200
    
    response_get = client.get("/pedidos/1001")
    assert response_get.status_code == 200
    get_json = response_get.json()

    assert get_json["id"] == 1001
    assert get_json["cliente"]["nombre"] == "Cliente Actualizado"
    assert get_json["total"] == 250.50

