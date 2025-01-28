
import aeroalpes.seedwork.presentacion.api as api
import json
from aeroalpes.modulos.cliente.aplicacion.servicios import ServicioCliente, ServicioMetodoPago
from aeroalpes.modulos.cliente.aplicacion.dto import ClienteDTO, MetodoPagoDTO
#from aeroalpes.modulos.cliente.aplicacion.mapeadores import MapeadorCliente, MapeadorMetodoPago
from aeroalpes.modulos.cliente.aplicacion.mapeadores import MapeadorCliente
from aeroalpes.seedwork.dominio.excepciones import ExcepcionDominio

from flask import Response, request


bp = api.crear_blueprint('cliente', '/cliente')

@bp.route('/cliente', methods=('POST',))
def registrar_cliente():
    """Endpoint para registrar un cliente."""
    try:
        cliente_dict = request.json  # Recibir datos del cliente en JSON
        
        map_cliente = MapeadorCliente()
        cliente_dto = map_cliente.externo_a_dto(cliente_dict)

        servicio_cliente = ServicioCliente()
        cliente_creado = servicio_cliente.registrar_cliente(cliente_dto)

        return map_cliente.dto_a_externo(cliente_creado), 201  # Devolver cliente creado con código HTTP 201
    except ExcepcionDominio as e:
        return Response(json.dumps({'error': str(e)}), status=400, mimetype='application/json')

@bp.route('/cliente/<id>', methods=('GET',))
def obtener_cliente(id):
    """Endpoint para obtener los datos de un cliente por su ID."""
    try:
        servicio_cliente = ServicioCliente()
        cliente_dto = servicio_cliente.obtener_cliente_por_id(id)

        map_cliente = MapeadorCliente()
        return map_cliente.dto_a_externo(cliente_dto), 200  # Devolver cliente con código HTTP 200
    except ExcepcionDominio as e:
        return Response(json.dumps({'error': str(e)}), status=400, mimetype='application/json')

'''@bp.route('/metodo-pago', methods=('POST',))
def agregar_metodo_pago():
    """Endpoint para agregar un método de pago a un cliente."""
    try:
        datos_metodo = request.json  # Recibir datos del método de pago en JSON
        id_cliente = datos_metodo.get('id_cliente')
        metodo_dict = datos_metodo.get('metodo_pago')

        if not id_cliente or not metodo_dict:
            raise ExcepcionDominio("Debe especificar el cliente y los detalles del método de pago.")

        map_metodo = MapeadorMetodoPago()
        metodo_dto = map_metodo.externo_a_dto(metodo_dict)

        servicio_metodo_pago = ServicioMetodoPago()
        metodo_agregado = servicio_metodo_pago.agregar_metodo_pago(metodo_dto, id_cliente)

        return map_metodo.dto_a_externo(metodo_agregado), 201  # Devolver método de pago creado con código HTTP 201
    except ExcepcionDominio as e:
        return Response(json.dumps({'error': str(e)}), status=400, mimetype='application/json')

@bp.route('/metodo-pago/<id_metodo>', methods=('DELETE',))
def eliminar_metodo_pago(id_metodo):
    """Endpoint para eliminar un método de pago de un cliente."""
    try:
        id_cliente = request.args.get('id_cliente')  # Obtener el ID del cliente desde los parámetros
        if not id_cliente:
            raise ExcepcionDominio("Debe especificar el ID del cliente.")

        servicio_metodo_pago = ServicioMetodoPago()
        servicio_metodo_pago.eliminar_metodo_pago(id_metodo, id_cliente)

        return Response(json.dumps({'message': 'Método de pago eliminado con éxito'}), status=200, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps({'error': str(e)}), status=400, mimetype='application/json') '''