"""Objetos valor del dominio de cliente

En este archivo usted encontrará los objetos valor del dominio de cliente

"""

from aeroalpes.seedwork.dominio.objetos_valor import ObjetoValor, Ciudad
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4

@dataclass(frozen=True)
class Nombre(ObjetoValor):
    nombres: str
    apellidos: str

@dataclass(frozen=True)
class Email(ObjetoValor):
    address: str
    dominio: str
    es_empresarial: bool

@dataclass(frozen=True)
class Cedula(ObjetoValor):
    numero: int
    ciudad: Ciudad

@dataclass(frozen=True)
class Rut(ObjetoValor):
    numero: int
    ciudad: Ciudad

class TipoMetodoPago(Enum):
    TARJETA_CREDITO = "Tarjeta de crédito"
    TARJETA_DEBITO = "Tarjeta de débito"
    TRANSFERENCIA_BANCARIA = "Transferencia bancaria"
    PAYPAL = "PayPal"
    OTRO = "Otro"

@dataclass(frozen=True)
class MetodoPago(ObjetoValor):
    tipo: TipoMetodoPago
    nombre: str
    token: str = field(default_factory=lambda: str(uuid4()))
    datos_ofuscados: str = field(default="")
    fecha_registro: datetime = field(default_factory=datetime.utcnow)

    def es_tipo(self, tipo: TipoMetodoPago) -> bool:
        """Valida si el método de pago es de un tipo específico."""
        return self.tipo == tipo

    def obtener_representacion_segura(self) -> str:
        """Devuelve una representación segura del método de pago."""
        return f"{self.tipo.value} - {self.datos_ofuscados}"
    
    def cambiar_nombre(self, nuevo_nombre: str):
        """Permite cambiar el nombre del método de pago."""
        self.nombre = nuevo_nombre

