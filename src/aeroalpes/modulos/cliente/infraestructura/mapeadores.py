from aeroalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from aeroalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from aeroalpes.modulos.cliente.dominio.entidades import ClienteNatural as Cliente, MetodoPago
from .dto import ClienteDTO, MetodoPagoDTO

class MapeadorCliente(RepMap):
    def entidad_a_dto(self, entidad: Cliente) -> ClienteDTO:
        metodos_pago_dto = [self._procesar_metodo_pago(m) for m in entidad.metodos_pago]
        return ClienteDTO(
            id=str(entidad.id),
            nombre=entidad.nombre,
            email=entidad.email,
            cedula=entidad.cedula,
            fecha_nacimiento=entidad.fecha_nacimiento,
            metodos_pago=metodos_pago_dto
        )

    def dto_a_entidad(self, dto: ClienteDTO) -> Cliente:
        metodos_pago = [self._procesar_metodo_pago(m) for m in dto.metodos_pago]
        return Cliente(
            id=dto.id,
            nombre=dto.nombre,
            email=dto.email,
            cedula=dto.cedula,
            fecha_nacimiento=dto.fecha_nacimiento,
            metodos_pago=metodos_pago
        )

    def _procesar_metodo_pago(self, metodo_dto: MetodoPagoDTO) -> MetodoPago:
        return MetodoPago(
            tipo=metodo_dto.tipo,
            nombre=metodo_dto.nombre,
            token=metodo_dto.token,
            datos_ofuscados=metodo_dto.datos_ofuscados,
            fecha_registro=metodo_dto.fecha_registro
        )

class MapeadorMetodoPago(RepMap):
    def entidad_a_dto(self, entidad: MetodoPago) -> MetodoPagoDTO:
        return MetodoPagoDTO(
            tipo=entidad.tipo,
            nombre=entidad.nombre,
            token=entidad.token,
            datos_ofuscados=entidad.datos_ofuscados,
            fecha_registro=entidad.fecha_registro
        )

    def dto_a_entidad(self, dto: MetodoPagoDTO) -> MetodoPago:
        return MetodoPago(
            tipo=dto.tipo,
            nombre=dto.nombre,
            token=dto.token,
            datos_ofuscados=dto.datos_ofuscados,
            fecha_registro=dto.fecha_registro
        )