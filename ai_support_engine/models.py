from pydantic import BaseModel, Field
from datetime import date
from enum import Enum

    
# ENUMS

class EstadoPedido(str, Enum):
    PENDIENTE = "pendiente"
    PREPARACION = "preparacion"
    ENVIADO = "enviado"
    ENTREGADO = "entregado"
    CANCELADO = "cancelado"


class MetodoPago(str, Enum):
    TARJETA = "tarjeta"
    PAYPAL = "paypal"
    BIZUM = "bizum"
    TRANSFERENCIA = "transferencia"


# MODELOS ANIDADOS

class Cliente(BaseModel):
    id: int = Field(gt=0)
    nombre: str = Field(min_length=2)
    email: str

# MODELO PRINCIPAL

# Output Model: Id returned
class Pedido(BaseModel):
    id: int = Field(gt=0)
    cliente: Cliente
    estado: EstadoPedido = EstadoPedido.PENDIENTE
    total: float
    notas: str


# Input Model: Id not provided by User
class PedidoCreate(BaseModel):
    cliente: Cliente
    estado: EstadoPedido = EstadoPedido.PENDIENTE
    total: float = Field(ge=0)
    notas: str | None = Field(default=None, max_length=250)
    
# Update / Patch
class PedidoEstadoUpdate(BaseModel):
    estado: EstadoPedido