"""DTOs para la capa de infrastructura del dominio de clientes

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio del cliente

"""

from aeroalpes.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table


# Definir la base para SQLAlchemy
Base = db.declarative_base()

class ClienteDTO(db.Model):
    __tablename__ = 'clientes'
    email = db.Column(db.String, primary_key=True)
    nombre = db.Column(db.String)
    apellido = db.Column(db.String)
    cedula = db.Column(db.String)

class MetodoPagoDTO(db.Model):
    __tablename__ = 'metodos_pago'
    token = db.Column(db.String, primary_key=True)
    tipo = db.Column(db.String)
    nombre = db.Column(db.String)
    cliente_email = db.Column(db.String)  # Relación con el cliente (campo foráneo)