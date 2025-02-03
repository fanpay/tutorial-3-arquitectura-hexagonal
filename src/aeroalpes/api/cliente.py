import aeroalpes.seedwork.presentacion.api as api
import json
from aeroalpes.modulos.cliente.aplicacion.servicios import ServicioCliente, ServicioMetodoPago
from aeroalpes.modulos.cliente.aplicacion.dto import ClienteDTO, MetodoPagoDTO
from aeroalpes.modulos.cliente.aplicacion.mapeadores import MapeadorClienteDTOJson
from aeroalpes.seedwork.dominio.excepciones import ExcepcionDominio

from flask import Response, request

bp = api.crear_blueprint('cliente', '/cliente')

@bp.route('/cliente', methods=('POST',))
def registrar_cliente():
    """Endpoint para registrar un cliente."""
    try:
        cliente_dict = request.json  # Recibir datos del cliente en JSON
        
        map_cliente = MapeadorClienteDTOJson()
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

        map_cliente = MapeadorClienteDTOJson()
        return map_cliente.dto_a_externo(cliente_dto), 200  # Devolver cliente con código HTTP 200
    except ExcepcionDominio as e:
        return Response(json.dumps({'error': str(e)}), status=400, mimetype='application/json')

@bp.route('/metodo-pago', methods=('POST',))
def agregar_metodo_pago():
    """Endpoint para agregar un método de pago."""
    try:
        metodo_pago_dict = request.json  # Recibir datos del método de pago en JSON
        
        map_metodo_pago = MapeadorMetodoPagoDTOJson()
        metodo_pago_dto = map_metodo_pago.externo_a_dto(metodo_pago_dict)

        cliente_id = metodo_pago_dict.get('cliente_id')
        servicio_metodo_pago = ServicioMetodoPago()
        metodo_pago_creado = servicio_metodo_pago.agregar_metodo_pago(cliente_id, metodo_pago_dto)

        return map_metodo_pago.dto_a_externo(metodo_pago_creado), 201  # Devolver método de pago creado con código HTTP 201
    except ExcepcionDominio as e:
        return Response(json.dumps({'error': str(e)}), status=400, mimetype='application/json')

@bp.route('/metodo-pago/<token>', methods=('PUT',))
def modificar_metodo_pago(token):
    """Endpoint para modificar un método de pago."""
    try:
        datos = request.json  # Recibir datos en JSON
        nuevo_nombre = datos.get('nombre')
        cliente_id = datos.get('cliente_id')

        servicio_metodo_pago = ServicioMetodoPago()
        servicio_metodo_pago.modificar_metodo_pago(cliente_id, token, nuevo_nombre)

        return Response(status=204)  # Devolver código HTTP 204 No Content
    except ExcepcionDominio as e:
        return Response(json.dumps({'error': str(e)}), status=400, mimetype='application/json')

@bp.route('/metodo-pago/<token>', methods=('DELETE',))
def eliminar_metodo_pago(token):
    """Endpoint para eliminar un método de pago."""
    try:
        datos = request.json  # Recibir datos en JSON
        cliente_id = datos.get('cliente_id')

        servicio_metodo_pago = ServicioMetodoPago()
        servicio_metodo_pago.eliminar_metodo_pago(cliente_id, token)

        return Response(status=204)  # Devolver código HTTP 204 No Content
    except ExcepcionDominio as e:
        return Response(json.dumps({'error': str(e)}), status=400, mimetype='application/json')