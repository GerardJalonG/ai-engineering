from fastapi import HTTPException

def pedido_no_encontrado() -> HTTPException:
    return HTTPException(
        status_code=404,
        detail="Pedido no encontrado"
    )