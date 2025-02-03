""" Fábricas para la creación de objetos del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de clientes

"""

from .entidades import ClienteNatural
from .reglas import NombreValido, EmailValido, CedulaValida, MetodoPagoValido
from .excepciones import NombreInvalidoExcepcion, EmailInvalidoExcepcion, CedulaInvalidaExcepcion, MetodoPagoInvalidoExcepcion, UsuarioExistenteExcepcion
from aeroalpes.seedwork.dominio.fabricas import Fabrica
from aeroalpes.seedwork.dominio.repositorios import Mapeador
from dataclasses import dataclass

@dataclass
class FabricaCliente(Fabrica):
    
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        # Validar nombre
        if not NombreValido(obj.nombre).es_valido():
            raise NombreInvalidoExcepcion()
        
        # Validar correo
        if not EmailValido(obj.email).es_valido():
            raise EmailInvalidoExcepcion()
        
        # Validar cédula (tomar en cuenta el país)
        if not CedulaValida(obj.cedula).es_valido():
            raise CedulaInvalidaExcepcion()
        
        # Validar métodos de pago
        for metodo_pago in obj.metodos_pago:
            print("noommmm: ", metodo_pago)
            if not MetodoPagoValido(metodo_pago.nombre).es_valido():
                raise MetodoPagoInvalidoExcepcion()
        
        # Si todas las reglas son válidas, creamos el cliente
        '''return ClienteNatural(
            nombre=obj.nombre,
            email=obj.email,
            cedula=obj.cedula,
            fecha_nacimiento=obj.fecha_nacimiento,
            metodos_pago=obj.metodos_pago
        )'''
        
        cliente: ClienteNatural = mapeador.dto_a_entidad(obj)
        return cliente;