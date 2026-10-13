"""
This file defines the database models
"""

from pydal.validators import *

from .common import Field, db

import datetime
from py4web import *
from .common import db, Field

# Tabla Vendedores
db.define_table('vendedor',
    Field('nombre', requires=IS_NOT_EMPTY()),
    Field('email', requires=IS_EMAIL()),
    format='%(nombre)s'  # <--- Agrega esta línea al final
)

# Tabla Reglas de Comisión
db.define_table('regla_comision',
    Field('monto_minimo', 'double', default=0.0),
    Field('porcentaje', 'double', requires=IS_FLOAT_IN_RANGE(0, 100))
)

# Tabla Ventas
db.define_table('venta',
    Field('vendedor_id', 'reference vendedor'),
    Field('monto', 'double', requires=IS_NOT_EMPTY()),
    Field('fecha', 'date', default=datetime.date.today)
)

db.commit()

# === SEMBRADO DE DATOS AUTOMÁTICO (SEEDING) ===
if db(db.vendedor).count() == 0:
    # Insertar Vendedores
    db.vendedor.insert(nombre='Alejandro Camino', email='alejandro@empresa.com')
    db.vendedor.insert(nombre='Jimmy Delgado', email='jimmy@empresa.com')
    
    # Insertar Reglas de Comisión
    db.regla_comision.insert(monto_minimo=0, porcentaje=5)
    db.regla_comision.insert(monto_minimo=500, porcentaje=10)
    db.regla_comision.insert(monto_minimo=1500, porcentaje=15)
    
    db.commit()