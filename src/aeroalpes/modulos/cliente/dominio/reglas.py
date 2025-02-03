"""Reglas de negocio del dominio de cliente"""

from aeroalpes.seedwork.dominio.reglas import ReglaNegocio
from aeroalpes.seedwork.dominio.objetos_valor import Pais
from .objetos_valor import Nombre, Email, Cedula, MetodoPago


import re
        
class NombreValido(ReglaNegocio):
    nombre: Nombre

    def __init__(self, nombre, mensaje='El nombre o apellido no pueden ser nulos o contener caracteres especiales'):
        super().__init__(mensaje)
        self.nombre = nombre

    def es_valido(self) -> bool:
        return bool(self.nombre) and bool(self.nombre.nombres) and bool(self.nombre.apellidos) and re.match("^[A-Za-z ]+$", self.nombre.nombres) and re.match("^[A-Za-z ]+$", self.nombre.apellidos)

class EmailValido(ReglaNegocio):
    email: Email

    def __init__(self, email: Email, mensaje='El correo electrónico debe seguir el formato RFC822'):
        super().__init__(mensaje)
        self.email = email

    def es_valido(self) -> bool:
        return bool(self.email.address) and re.match(r"[^@]+@[^@]+\.[^@]+", self.email.address)

class CedulaValida(ReglaNegocio):
    cedula: Cedula
    pais: Pais

    def __init__(self, cedula: Cedula, mensaje='La cédula no cumple con el formato numérico adecuado'):
        super().__init__(mensaje)
        self.cedula = cedula
        self.pais = cedula.ciudad.pais

    def es_valido(self) -> bool:
        # Formato general para cédulas (esto debe ajustarse por país)
        if self.pais.nombre == "Chile":
            return bool(self.cedula) and bool(self.cedula.numero) and re.match(r"^\d{7,8}$", str(self.cedula.numero))
        elif self.pais.nombre == "Colombia":
            return bool(self.cedula) and bool(self.cedula.numero) and re.match(r"^\d{6,10}$", str(self.cedula.numero))
        # Agregar más validaciones para otros países si es necesario
        return False

class MetodoPagoValido(ReglaNegocio):
    metodo_pago: str

    def __init__(self, metodo_pago: str, mensaje='El nombre del método de pago debe tener entre 5 y 80 caracteres y no contener caracteres especiales'):
        super().__init__(mensaje)
        self.metodo_pago = metodo_pago

    def es_valido(self) -> bool:
        return bool(self.metodo_pago) and 5 <= len(self.metodo_pago) <= 80 and re.match("^[A-Za-z0-9 ]+$", self.metodo_pago)