from dataclasses import dataclass, field
from datetime import datetime
from aeroalpes.modulos.cliente.dominio.objetos_valor import Email, Nombre, Cedula
from aeroalpes.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class MetodoPagoDTO(DTO):
    nombre: str
    tipo: str

@dataclass(frozen=True)
class ClienteDTO(DTO):
    id: str
    nombre: Nombre
    email: Email
    cedula: Cedula
    fecha_nacimiento: datetime
    metodos_pago: list[MetodoPagoDTO] = field(default_factory=list)
