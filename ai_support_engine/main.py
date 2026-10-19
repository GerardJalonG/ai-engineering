from fastapi import FastAPI, HTTPException
from .services import *
from .models import *

app = FastAPI()


@app.get("/")
def inicio():
    return {"mensaje": "AI Support Engine funcionando"}

@app.get("/pedidos/{id_pedido}")
def get_pedido(id_pedido: int):
    pedido = buscar_pedido(id_pedido)
    if pedido is None:
        raise HTTPException(
            status_code=404,
            detail="Pedido no encontrado"
        )
    return pedido

@app.get("/pedidos")
def get_pedidos(estado: str | None = None):
    if estado is not None:
        return filtrar_pedidos(estado)
    return  listar_pedidos()

@app.post("/pedidos", status_code=201)
def post_pedido(datos: PedidoCreate):
    
    # 1. Convierte datos en un diccionario
    datos_diccionario = datos.model_dump()
    # 2. Llama a crear_pedido() con ese diccionario
    pedido_creado = crear_pedido(datos_diccionario)
    # 3. Devuelve el pedido creado
    return pedido_creado