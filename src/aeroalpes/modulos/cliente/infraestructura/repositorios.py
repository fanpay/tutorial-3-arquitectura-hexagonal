""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de clientes

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de clientes

"""

from aeroalpes.config.db import db
from aeroalpes.modulos.cliente.dominio.repositorios import RepositorioCliente, RepositorioMetodoPago
from aeroalpes.modulos.cliente.dominio.entidades import ClienteNatural
from aeroalpes.modulos.cliente.dominio.objetos_valor import MetodoPago
from .dto import ClienteDTO, MetodoPagoDTO
from uuid import UUID



class RepositorioClienteSQLite(RepositorioCliente):
    def agregar(self, cliente: ClienteNatural) -> None:
        session = db.session
        cliente_dto = ClienteDTO(
            email=cliente.email.address,
            nombre=cliente.nombre.nombres,
            apellido=cliente.nombre.apellidos,
            cedula=cliente.cedula.numero
        )
        session.add(cliente_dto)
        session.commit()

    def obtener_por_id(self, email: str) -> ClienteNatural:
        session = db.session
        cliente_dto = session.query(ClienteDTO).filter_by(email=email).first()
        if cliente_dto:
            return ClienteNatural(
                nombre=cliente_dto.nombre,
                apellido=cliente_dto.apellido,
                email=cliente_dto.email,
                cedula=cliente_dto.cedula
            )
        return None

    def actualizar(self, cliente: ClienteNatural) -> None:
        session = db.session
        cliente_dto = session.query(ClienteDTO).filter_by(email=cliente.email.address).first()
        if cliente_dto:
            cliente_dto.nombre = cliente.nombre.nombres
            cliente_dto.apellido = cliente.nombre.apellidos
            cliente_dto.cedula = cliente.cedula.numero
            session.commit()

    def eliminar(self, cliente: ClienteNatural) -> None:
        session = db.session
        cliente_dto = session.query(ClienteDTO).filter_by(email=cliente.email.address).first()
        if cliente_dto:
            session.delete(cliente_dto)
            session.commit()
            
    def obtener_todos(self, id: UUID) -> ClienteNatural:
        # TODO
        raise NotImplementedError

class RepositorioMetodoPagoSQLite(RepositorioMetodoPago):
    def agregar_metodo_pago(self, metodo_pago: MetodoPago) -> None:
        session = db.session
        metodo_pago_dto = MetodoPagoDTO(
            token=metodo_pago.token,
            tipo=metodo_pago.tipo,
            nombre=metodo_pago.nombre,
            cliente_email=metodo_pago.cliente_email
        )
        session.add(metodo_pago_dto)
        session.commit()

    def eliminar_metodo_pago(self, metodo_pago: MetodoPago) -> None:
        session = db.session
        metodo_pago_dto = session.query(MetodoPagoDTO).filter_by(token=metodo_pago.token).first()
        if metodo_pago_dto:
            session.delete(metodo_pago_dto)
            session.commit()

    def obtener_metodos_pago(self, cliente: ClienteNatural) -> list[MetodoPago]:
        session = db.session
        metodos_dto = session.query(MetodoPagoDTO).filter_by(cliente_email=cliente.email.address).all()
        return [MetodoPago(
            token=metodo.token,
            tipo=metodo.tipo,
            nombre=metodo.nombre
        ) for metodo in metodos_dto]

