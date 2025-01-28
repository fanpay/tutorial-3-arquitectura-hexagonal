from aeroalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from aeroalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from aeroalpes.modulos.cliente.dominio.entidades import ClienteNatural as Cliente, MetodoPago
from .dto import ClienteDTO, MetodoPagoDTO

class MapeadorClienteDTOJson(AppMap):
    def _procesar_metodo_pago(self, metodo: dict) -> MetodoPagoDTO:
        return MetodoPagoDTO(tipo=metodo.get('tipo'), detalles=metodo.get('detalles'))

    def externo_a_dto(self, externo: dict) -> ClienteDTO:
        metodos_pago_dto = [self._procesar_metodo_pago(metodo) for metodo in externo.get('metodos_pago', [])]
        return ClienteDTO(
            id=externo.get('id'),
            nombre=externo.get('nombre'),
            email=externo.get('email'),
            telefono=externo.get('telefono'),
            metodos_pago=metodos_pago_dto
        )

    def dto_a_externo(self, dto: ClienteDTO) -> dict:
        return dto.__dict__

class MapeadorCliente(RepMap):
    def _procesar_metodo_pago(self, metodo_dto: MetodoPagoDTO) -> MetodoPago:
        return MetodoPago(tipo=metodo_dto.tipo, detalles=metodo_dto.detalles)

    def entidad_a_dto(self, entidad: Cliente) -> ClienteDTO:
        metodos_pago_dto = [MetodoPagoDTO(m.tipo, m.detalles) for m in entidad.metodos_pago]
        return ClienteDTO(
            id=str(entidad.id),
            nombre=entidad.nombre,
            email=entidad.email,
            telefono=entidad.telefono,
            metodos_pago=metodos_pago_dto
        )

    def dto_a_entidad(self, dto: ClienteDTO) -> Cliente:
        metodos_pago = [self._procesar_metodo_pago(m) for m in dto.metodos_pago]
        return Cliente(
            id=dto.id,
            nombre=dto.nombre,
            email=dto.email,
            telefono=dto.telefono,
            metodos_pago=metodos_pago
        )
