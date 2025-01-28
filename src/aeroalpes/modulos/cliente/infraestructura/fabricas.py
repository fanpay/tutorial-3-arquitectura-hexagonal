""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de vuelos

"""

from dataclasses import dataclass, field
from aeroalpes.seedwork.dominio.fabricas import Fabrica
from aeroalpes.seedwork.dominio.repositorios import Repositorio
from aeroalpes.modulos.cliente.dominio.repositorios import RepositorioCliente, RepositorioMetodoPago
from .repositorios import RepositorioClienteSQLite, RepositorioMetodoPagoSQLite
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioCliente.__class__:
            return RepositorioClienteSQLite()
        elif obj == RepositorioMetodoPago.__class__:
            return RepositorioMetodoPagoSQLite()
        else:
            raise ExcepcionFabrica("No existe una implementación para el repositorio con el tipo dado.")