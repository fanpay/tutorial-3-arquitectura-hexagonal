from datetime import datetime
from aeroalpes.modulos.cliente.dominio.entidades import Nombre, Cedula
from aeroalpes.modulos.cliente.dominio.objetos_valor import Email, Ciudad
from aeroalpes.seedwork.dominio.objetos_valor import Pais
from aeroalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from aeroalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from aeroalpes.modulos.cliente.dominio.entidades import ClienteNatural as Cliente, MetodoPago
from .dto import ClienteDTO, MetodoPagoDTO

class MapeadorClienteDTOJson(AppMap):
    def _procesar_metodo_pago(self, metodo: dict) -> MetodoPagoDTO:
        return MetodoPagoDTO(nombre=metodo.get('nombre'),tipo=metodo.get('tipo'))

    def externo_a_dto(self, externo: dict) -> ClienteDTO:
        metodos_pago_dto = [self._procesar_metodo_pago(metodo) for metodo in externo.get('metodos_pago', [])]

        return ClienteDTO(
           
            id=externo.get('id'),
            nombre=Nombre(nombres=externo.get('nombre').get('nombres'), apellidos=externo.get('nombre').get('apellidos')),
            email=Email(address=externo.get('email').get('address'), dominio=externo.get('email').get('dominio'), es_empresarial=externo.get('email').get('es_empresarial')),
            cedula=Cedula(numero=externo.get('cedula').get('numero'), 
                          ciudad=Ciudad(nombre=externo.get('cedula').get('ciudad').get('nombre'), 
                                        pais=Pais(nombre=externo.get('cedula').get('ciudad').get('pais').get('nombre'),
                                                  codigo=externo.get('cedula').get('ciudad').get('pais').get('codigo')), 
                                        codigo=externo.get('cedula').get('ciudad').get('codigo'))),
            fecha_nacimiento=datetime.fromisoformat(externo.get('fecha_nacimiento')),
            
            metodos_pago=metodos_pago_dto
        )

    def dto_a_externo(self, dto: ClienteDTO) -> dict:
        return dto.__dict__

class MapeadorCliente(RepMap):
    def _procesar_metodo_pago(self, metodo_dto: MetodoPagoDTO) -> MetodoPago:
        return MetodoPago(nombre=metodo_dto.nombre, tipo=metodo_dto.tipo)

    def entidad_a_dto(self, entidad: Cliente) -> ClienteDTO:
        metodos_pago_dto = [MetodoPagoDTO(m.tipo, m.detalles) for m in entidad.metodos_pago]
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
        
    def obtener_tipo(self) -> type:
        return Cliente.__class__