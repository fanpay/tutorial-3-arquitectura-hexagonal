"""Reglas de negocio del dominio de cliente"""

from aeroalpes.seedwork.dominio.reglas import ReglaNegocio
from aeroalpes.seedwork.dominio.objetos_valor import Pais
from .objetos_valor import Email, Cedula, MetodoPago


import re

class EmailUnico(ReglaNegocio):
    def __init__(self, email, cliente_repositorio, mensaje="El email ya está registrado"):
        super().__init__(mensaje)
        self.email = email
        self.cliente_repositorio = cliente_repositorio

    def es_valido(self) -> bool:
        # Aquí se consulta el repositorio para verificar si ya existe un cliente con ese email
        cliente = self.cliente_repositorio.obtener_por_email(self.email)
        return cliente is None  # Si no existe, el email es único
        
class NombreValido(ReglaNegocio):
    nombre: str
    apellidos: str

    def __init__(self, nombre: str, apellidos: str, mensaje='El nombre o apellido no pueden ser nulos o contener caracteres especiales'):
        super().__init__(mensaje)
        self.nombre = nombre
        self.apellidos = apellidos

    def es_valido(self) -> bool:
        return bool(self.nombre) and bool(self.apellidos) and re.match("^[A-Za-z ]+$", self.nombre) and re.match("^[A-Za-z ]+$", self.apellidos)

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
            return bool(self.cedula) and re.match(r"^\d{7,8}$", self.cedula)
        elif self.pais.nombre == "Colombia":
            return bool(self.cedula) and re.match(r"^\d{6,10}$", self.cedula)
        # Agregar más validaciones para otros países si es necesario
        return False

class MetodoPagoValido(ReglaNegocio):
    metodo_pago: str

    def __init__(self, metodo_pago: str, mensaje='El nombre del método de pago debe tener entre 5 y 80 caracteres y no contener caracteres especiales'):
        super().__init__(mensaje)
        self.metodo_pago = metodo_pago

    def es_valido(self) -> bool:
        return bool(self.metodo_pago) and 5 <= len(self.metodo_pago) <= 80 and re.match("^[A-Za-z0-9 ]+$", self.metodo_pago)