from dataclasses import dataclass, field
from aeroalpes.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class MetodoPagoDTO(DTO):
    tipo: str
    detalles: dict

@dataclass(frozen=True)
class ClienteDTO(DTO):
    id: str
    nombre: str
    email: str
    telefono: str
    metodos_pago: list[MetodoPagoDTO] = field(default_factory=list)
