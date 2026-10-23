import pytest

from ai_support_engine.database import inicializar_base_datos

@pytest.fixture
def db_path(tmp_path):
    ruta = tmp_path / "test_suport.db"

    inicializar_base_datos(str(ruta))

    return str(ruta)