""" Fábricas para la creación de objetos del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de clientes

"""

from .entidades import ClienteNatural
from .reglas import EmailUnico, NombreValido, EmailValido, CedulaValida, MetodoPagoValido
from .excepciones import NombreInvalidoExcepcion, CorreoInvalidoExcepcion, CedulaInvalidaExcepcion, MetodoPagoInvalidoExcepcion, UsuarioExistenteExcepcion
from aeroalpes.seedwork.dominio.fabricas import Fabrica
from aeroalpes.seedwork.dominio.repositorios import Mapeador
from dataclasses import dataclass

@dataclass
class FabricaCliente(Fabrica):
    
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        # Validar si el email ya existe
        if not EmailUnico(cliente_data['email']).es_valido():
            raise UsuarioExistenteExcepcion("El email ya está registrado")

        # Validar nombre
        if not NombreValido(obj.nombre, obj.apellidos).es_valido():
            raise NombreInvalidoExcepcion()
        
        # Validar correo
        if not CorreoValido(obj.email.address).es_valido():
            raise CorreoInvalidoExcepcion()
        
        # Validar cédula (tomar en cuenta el país)
        if not CedulaValida(obj.cedula.numero, obj.cedula.ciudad.pais).es_valido():
            raise CedulaInvalidaExcepcion()
        
        # Validar métodos de pago
        for metodo_pago in obj.metodos_pago:
            if not MetodoPagoValido(metodo_pago.nombre).es_valido():
                raise MetodoPagoInvalidoExcepcion()
        
        # Si todas las reglas son válidas, creamos el cliente
        return ClienteNatural(
            nombre=obj.nombre,
            email=obj.email,
            cedula=obj.cedula,
            fecha_nacimiento=obj.fecha_nacimiento,
            metodos_pago=obj.metodos_pago
        )