""" Excepciones del dominio de clientes

En este archivo usted encontrará los Excepciones relacionadas
al dominio de cliente

"""

from aeroalpes.seedwork.dominio.excepciones import ExcepcionFabrica

class NombreInvalidoExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='El nombre o apellido contiene caracteres no válidos o es nulo'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)

class EmailInvalidoExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='El correo electrónico no cumple con el formato RFC822'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)

class CedulaInvalidaExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='La cédula no cumple con el formato numérico válido'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)

class MetodoPagoInvalidoExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='El nombre del método de pago no es válido'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)

class UsuarioExistenteExcepcion(Exception):
    def __init__(self, mensaje='El email ya está registrado'):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class MetodoPagoExistenteExcepcion(Exception):
    def __init__(self, mensaje='Ya existe un método de pago con los mismos datos'):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class MetodoPagoNoEncontradoExcepcion(Exception):
    def __init__(self, mensaje='Método de pago no encontrado'):
        self.mensaje = mensaje
        super().__init__(self.mensaje)