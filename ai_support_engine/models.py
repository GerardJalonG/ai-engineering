from pydantic import BaseModel
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
    id: int
    nombre: str
    email: str


class Producto(BaseModel):
    sku: str
    nombre: str
    cantidad: int
    precio: float


class DireccionEnvio(BaseModel):
    ciudad: str
    codigo_postal: str


# MODELO PRINCIPAL

class Pedido(BaseModel):
    id: int
    cliente: Cliente
    estado: EstadoPedido = EstadoPedido.PENDIENTE
    fecha: date
    productos: list[Producto]
    total: float
    metodo_pago: MetodoPago | None = None
    direccion_envio: DireccionEnvio
    notas: str | None = None

class PedidoCreate(BaseModel):
    cliente: Cliente
    estado: EstadoPedido = EstadoPedido.PENDIENTE
    total: float