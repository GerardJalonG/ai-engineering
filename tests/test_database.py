import pytest
import sqlite3

from ai_support_engine.database import *


def test_insertar_pedido_correcto(db_path):
    nuevo_id = insertar_pedido("pendiente", 95.80, db_path)
    
    pedido = buscar_pedido_db(nuevo_id, db_path)

    assert pedido["id"] == nuevo_id
    assert pedido["estado"] == "pendiente"
    assert pedido["total"] == 95.80
    
def test_insertar_pedido_total_negativo(db_path):
    with pytest.raises(sqlite3.IntegrityError):
        insertar_pedido("pendiente", -50, db_path)