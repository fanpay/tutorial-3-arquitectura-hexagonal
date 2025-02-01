"""Entidades del dominio de cliente

En este archivo usted encontrará las entidades del dominio de cliente

"""

from datetime import datetime
from aeroalpes.seedwork.dominio.entidades import Entidad, AgregacionRaiz
from dataclasses import dataclass, field

from .objetos_valor import Nombre, Email, Cedula, Rut, MetodoPago

@dataclass
class Usuario(Entidad):
    nombre: Nombre = field(default_factory=Nombre)
    email: Email = field(default_factory=Email)

@dataclass
class ClienteNatural(Usuario, AgregacionRaiz):
    cedula: Cedula = field(default_factory=Cedula)
    fecha_nacimiento: datetime = field(default_factory=datetime)
    metodos_pago: list[MetodoPago] = field(default_factory=list)

    def agregar_metodo_pago(self, metodo_pago: MetodoPago):
        """Agrega un nuevo método de pago al cliente."""
        self.metodos_pago.append(metodo_pago)

    def eliminar_metodo_pago(self, token: str):
        """Elimina un método de pago basado en su token único."""
        self.metodos_pago = [m for m in self.metodos_pago if m.token != token]

    def obtener_metodo_pago(self, token: str) -> MetodoPago | None:
        """Obtiene un método de pago específico por su token."""
        for metodo in self.metodos_pago:
            if metodo.token == token:
                return metodo
        return None

    def modificar_metodo_pago(self, token: str, nuevo_nombre: str):
        """Modifica el nombre de un método de pago."""
        metodo = self.obtener_metodo_pago(token)
        if metodo:
            metodo.cambiar_nombre(nuevo_nombre)

@dataclass
class ClienteEmpresa(Usuario):
    rut: Rut = field(default_factory=Rut)
    fecha_constitucion: datetime = field(default_factory=datetime)
