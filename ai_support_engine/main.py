from fastapi import FastAPI, HTTPException
from .services import *
from .models import *
from .exceptions import *
app = FastAPI()


@app.get("/")
def inicio():
    return {"mensaje": "AI Support Engine funcionando"}

@app.get("/pedidos/{id_pedido}")
def get_pedido(id_pedido: int):
    pedido = buscar_pedido(id_pedido)
    if pedido is None:
        raise pedido_no_encontrado()
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

@app.patch("/pedidos/{id_pedido}")
def patch_pedido(id_pedido: int, datos: PedidoEstadoUpdate):
    # PASO 1: Obtener el nuevo estado desde datos
    nuevo_estado = datos.estado.value
    # PASO 2: Llamar a actualizar_estado_pedido()
    # pasando el ID y el nuevo estado
    pedido = actualizar_estado_pedido(id_pedido, nuevo_estado)
    # PASO 3: Comprobar si el pedido existe
    # Si no existe, lanzar HTTPException 404
    if pedido is None:
        raise pedido_no_encontrado()
    # PASO 4: Devolver el pedido actualizado
    return pedido


@app.delete("/pedidos/{id_pedido}")
def delete_pedido(id_pedido: int):
    response = eliminar_pedido(id_pedido)
    mensaje = "Pedido eliminado" if response == True else "No se ha podido eliminar"
    if response is False:
        raise HTTPException(
            status_code=404,
            detail=mensaje
        )
    return mensaje

@app.put("/pedidos/{id_pedido}")
def put_pedido(id_pedido:int, datos: PedidoCreate):
    datos_diccionario = datos.model_dump()
    
    pedido = actualizar_pedido(id_pedido, datos_diccionario)
    if pedido is None:
        raise pedido_no_encontrado()
    return pedido
    
# endpoints temporales db
@app.get("/db/pedidos")
def get_pedidos(estado: str | None = None):
    if estado is not None:
        return filtrar_pedidos(estado)
    return listar_pedidos()

@app.get("/db/pedidos/{id_pedido}", response_model=PedidoDB)
def get_pedido_db(id_pedido: int):
    pedido = buscar_pedido_persistente(id_pedido)
    if pedido is None:
        raise pedido_no_encontrado()
    return pedido

@app.post("/db/pedidos", status_code=201, response_model=PedidoDB)
def post_pedido_db(datos: PedidoCreateDB):

    # PASO 1: Convertir el modelo Pydantic a diccionario
    datos_diccionario = datos.model_dump(mode="json")
    # PASO 2: Llamar a crear_pedido_persistente()
    pedido = crear_pedido_persistente(datos_diccionario)
    return pedido
    # PASO 3: Devolver el pedido creado

@app.patch("/db/pedidos/{id_pedido}", response_model=PedidoDB)
def patch_pedido_db(id_pedido: int, datos: PedidoEstadoUpdate):
    nuevo_estado = datos.estado.value
    pedido = actualizar_estado_persistente(id_pedido, nuevo_estado)
    
    if pedido is None:
        raise pedido_no_encontrado()
    
    return pedido

@app.delete("/db/pedidos/{id_pedido}")
def delete_pedido_db(id_pedido: int):
    eliminado = eliminar_pedido_persistente(id_pedido)
    if not eliminado:
        raise pedido_no_encontrado()
    return {"mensaje": "Pedido eliminado correctamente"}
    
    