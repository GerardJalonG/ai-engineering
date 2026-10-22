import pytest
import sqlite3

from ai_support_engine.database import *


def test_insertar_pedido_total_negativo():
    
    with pytest.raises(sqlite3.IntegrityError):
        insertar_pedido("pendiente", -50)