""" Interfaces para los repositorios del dominio de clientes

En este archivo usted encontrará las diferentes interfaces para repositorios
del dominio de clientes

"""

from abc import ABC
from aeroalpes.seedwork.dominio.repositorios import Repositorio
from .entidades import ClienteNatural
from .objetos_valor import MetodoPago

class RepositorioCliente(Repositorio, ABC):
    def agregar_cliente(self, cliente: ClienteNatural) -> None:
        """Agregar un cliente a la base de datos"""
        pass

    def obtener_cliente_por_email(self, email: str) -> ClienteNatural:
        """Obtener un cliente por su email"""
        pass

    def actualizar_cliente(self, cliente: ClienteNatural) -> None:
        """Actualizar la información de un cliente"""
        pass

    def eliminar_cliente(self, cliente: ClienteNatural) -> None:
        """Eliminar un cliente"""
        pass

class RepositorioMetodoPago(Repositorio, ABC):
    def agregar_metodo_pago(self, metodo_pago: MetodoPago) -> None:
        """Agregar un método de pago a la base de datos"""
        pass

    def eliminar_metodo_pago(self, metodo_pago: MetodoPago) -> None:
        """Eliminar un método de pago de la base de datos"""
        pass

    def obtener_metodos_pago(self, cliente: ClienteNatural) -> list[MetodoPago]:
        """Obtener los métodos de pago asociados a un cliente"""
        pass
