"""
This file defines actions, i.e. functions the URLs are mapped into
The @action(path) decorator exposed the function at URL:

    http://127.0.0.1:8000/{app_name}/{path}

If app_name == '_default' then simply

    http://127.0.0.1:8000/{path}

If path == 'index' it can be omitted:

    http://127.0.0.1:8000/

The path follows the bottlepy syntax.

@action.uses('generic.html')  indicates that the action uses the generic.html template
@action.uses(session)         indicates that the action uses the session
@action.uses(db)              indicates that the action uses the db
@action.uses(T)               indicates that the action uses the i18n & pluralization
@action.uses(auth.user)       indicates that the action requires a logged in user
@action.uses(auth)            indicates that the action requires the auth object

session, db, T, auth, and tempates are examples of Fixtures.
Warning: Fixtures MUST be declared with @action.uses({fixtures}) else your app will result in undefined behavior
"""

from py4web import action, redirect, HTTP, URL

from .common import T, auth, cache, db, session, Field


from py4web import action, request
from py4web.utils.form import Form, FormStyleBulma
from .common import db, session, auth

@action("index", method=["GET", "POST"])
@action.uses("dashboard.html", db, session)
def index():
    # Formularios rápidos para agregar datos
    form_venta = Form(db.venta, formstyle=FormStyleBulma)
    
    # Filtros de fecha desde la URL
    fecha_inicio = request.query.get('fecha_inicio')
    fecha_fin = request.query.get('fecha_fin')
    
    query = (db.venta.id > 0)
    if fecha_inicio and fecha_fin:
        query &= (db.venta.fecha >= fecha_inicio) & (db.venta.fecha <= fecha_fin)
        
    ventas = db(query).select(
        db.venta.ALL, 
        db.vendedor.nombre,
        left=db.vendedor.on(db.venta.vendedor_id == db.vendedor.id)
    )
    
    # Lógica de cálculo de comisiones (Reglas de Negocio)
    reglas = db(db.regla_comision.id > 0).select(orderby=~db.regla_comision.monto_minimo)
    
    reporte = []
    for v in ventas:
        comision_calculada = 0
        for regla in reglas:
            if v.venta.monto >= regla.monto_minimo:
                comision_calculada = v.venta.monto * (regla.porcentaje / 100)
                break 
        
        reporte.append({
            'vendedor': v.vendedor.nombre,
            'fecha': v.venta.fecha,
            'monto': v.venta.monto,
            'comision': comision_calculada
        })

    return dict(form_venta=form_venta, reporte=reporte)