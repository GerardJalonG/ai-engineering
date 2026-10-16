from fastapi import FastAPI, HTTPException
from .services import *

app = FastAPI()


@app.get("/")
def inicio():
    return {"mensaje": "AI Support Engine funcionando"}

@app.get("/pedidos/{id_pedido}")
def get_pedido(id_pedido: int, estado: Optional[str] = None):
    pedido = buscar_pedido(id_pedido)
    if pedido is None:
        raise HTTPException(
            status_code=404,
            detail="Pedido no encontrado"
        )
    return pedido

@app.get("/pedidos")
def get_pedidos():
    return  listar_pedidos()
