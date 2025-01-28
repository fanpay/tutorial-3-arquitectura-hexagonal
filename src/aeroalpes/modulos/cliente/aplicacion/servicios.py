""" Servicios para la capa de aplicación del dominio de clientes y métodos de pago

En este archivo se definen los servicios necesarios para la gestión de clientes
y métodos de pago. Estos servicios usan el patrón CQRS para separar comandos y consultas.

"""

from aeroalpes.seedwork.aplicacion.servicios import Servicio
from aeroalpes.modulos.cliente.dominio.entidades import ClienteNatural as Cliente, MetodoPago
from aeroalpes.modulos.cliente.dominio.fabricas import FabricaCliente
from aeroalpes.modulos.cliente.infraestructura.fabricas import FabricaRepositorio
from aeroalpes.modulos.cliente.infraestructura.repositorios import RepositorioCliente
from .mapeadores import MapeadorCliente
from .dto import ClienteDTO, MetodoPagoDTO

class ServicioCliente(Servicio):
    def __init__(self):
        self._fabrica_repositorio = FabricaRepositorio()
        self._fabrica_cliente = FabricaCliente()

    def registrar_cliente(self, cliente_dto: ClienteDTO) -> ClienteDTO:
        cliente = self._fabrica_cliente.crear_objeto(cliente_dto, MapeadorCliente())
        repositorio = self._fabrica_repositorio.crear_objeto(RepositorioCliente.__class__)
        repositorio.agregar(cliente)
        return self._fabrica_cliente.crear_objeto(cliente, MapeadorCliente())

    def obtener_cliente_por_id(self, id: str) -> ClienteDTO:
        repositorio = self._fabrica_repositorio.crear_objeto(RepositorioCliente.__class__)
        cliente = repositorio.obtener_por_id(id)
        return self._fabrica_cliente.crear_objeto(cliente, MapeadorCliente())

class ServicioMetodoPago(Servicio):
    def __init__(self):
        self._fabrica_repositorio = FabricaRepositorio()

    def agregar_metodo_pago(self, metodo_pago_dto: MetodoPagoDTO, id_cliente: str) -> MetodoPagoDTO:
        repositorio = self._fabrica_repositorio.crear_objeto(RepositorioCliente.__class__)
        cliente = repositorio.obtener_por_id(id_cliente)
        metodo_pago = MetodoPago(tipo=metodo_pago_dto.tipo, detalles=metodo_pago_dto.detalles)
        cliente.agregar_metodo_pago(metodo_pago)
        repositorio.actualizar(cliente)
        return MetodoPagoDTO(tipo=metodo_pago.tipo, detalles=metodo_pago.detalles)

    def eliminar_metodo_pago(self, id_metodo: str, id_cliente: str):
        repositorio = self._fabrica_repositorio.crear_objeto(RepositorioCliente.__class__)
        cliente = repositorio.obtener_por_id(id_cliente)
        cliente.eliminar_metodo_pago(id_metodo)
        repositorio.actualizar(cliente)

