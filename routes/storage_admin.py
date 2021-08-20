import bottle
import datetime as dt
from bottle import route, run, post, request
from modules.bottles import BottleJson
<<<<<<< HEAD
#from modules.storage_admin import  create_m, query_m, create_e, query_e, create_s, query_s, query_m_cla, query_m_des, query_e_id, query_e_fec, query_e_can, query_s_id, query_s_fec, query_s_can
import modules.storage_admin as msa
app = BottleJson()

=======
from modules.storage_admin import  create_m, query_m, create_e, query_e, create_s, query_s, query_m_cla, query_m_des, query_e_id, query_e_fec, query_e_can, query_s_id, query_s_fec, query_s_can
app = BottleJson()
# gogole.com/s?hola=mundo&boo=fantasam&fo=bar
# curl http://localhost:8080/storage_admin/foo -X GET
>>>>>>> 1e27660ce027e9a37742d43b94b67f8710b6c99d
@app.get("/foo")
def foo(*args, **kwargs):
    payload = bottle.request.query
    print(bottle.request.query)
    print(payload.dict)
    raise bottle.HTTPError(501,"error")

<<<<<<< HEAD

=======
# curl http://localhost:8080/storage_admin/bar -X POST -H 'Content-Type: application/json' -d '{"un": "json"}'
>>>>>>> 1e27660ce027e9a37742d43b94b67f8710b6c99d
@app.post("/bar")
def bar(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    raise HTTPError(501)


#-------------------------------- Mercancia ----------------------------


<<<<<<< HEAD
# Registar una nueva mercancia en formato json
# curl localhost:8080/storage_admin/mercancia/register -X POST -H "Content-Type: application/json" -d '{"descripcion": "ejemplo","presentacion":"ejemplo","clave": "ejem01"}'
=======
# curl localhost:8080/storage_admin/mercancia/register -X POST -H "Content-Type: application/json" -d '{"descripcion": "mangera de 3/4","presentacion":"caja con 32 unidades","clave": "maca1"}'
>>>>>>> 1e27660ce027e9a37742d43b94b67f8710b6c99d
@app.post("/mercancia/register")
def store(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
<<<<<<< HEAD
        descripcion = str(payload['descripcion'])
=======
        descripcion = str(payload['descrpcion'])
>>>>>>> 1e27660ce027e9a37742d43b94b67f8710b6c99d
        presentacion = str(payload['presentacion'])
        clave = str(payload['clave'])

        if len(descripcion) == 0:
            raise Exception()
        print("dato validos")
<<<<<<< HEAD
        respuesta = msa.create_m(**payload)
=======
        respuesta = create_m(**payload)
>>>>>>> 1e27660ce027e9a37742d43b94b67f8710b6c99d
        print(respuesta)
    except:
        print("datos invalidos")
        raise bottle.HTTPError(400, "Invalid data")
    raise bottle.HTTPError(201, respuesta)



<<<<<<< HEAD
# Consultar todas las mercancias existentes
=======

>>>>>>> 1e27660ce027e9a37742d43b94b67f8710b6c99d
# curl http://localhost:8080/storage_admin/mercancia/query
@app.get("/mercancia/query")
def get_mercancias(*args, **kwargs):
    try:
<<<<<<< HEAD
       respuesta = msa.query_m()
=======
       respuesta = query_m()
>>>>>>> 1e27660ce027e9a37742d43b94b67f8710b6c99d
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)


<<<<<<< HEAD
# Consultar una mercancia espesifica segun su clave
# curl http://localhost:8080/storage_admin/mercancia/query/clave/ejem01 -X GET
@app.get("/mercancia/query/clave/<clave>")
def query_m_cla(*args, clave=None, **kwargs):
    try:
        respuesta = msa.query_m_cla(clave = clave)
=======
# curl http://localhost:8080/storage_admin/mercancia/query/ejemplos11-2010-12-12 -X GET
@app.get("/mercancia/query/<clave>")
def query_m_cla(*args, clave=None, **kwargs):
    try:
        respuesta = query_m_cla(clave = clave)
>>>>>>> 1e27660ce027e9a37742d43b94b67f8710b6c99d
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)


<<<<<<< HEAD
# Consultar una mercancia espesifica segun su descripcion
# curl http://localhost:8080/storage_admin/mercancia/query/descripcion/ejemplo -X GET
@app.get("/mercancia/query/descripcion/<descripcion>")
def query_m_des(*args, descripcion=None, **kwargs):
    try:
        respuesta = msa.query_m_des(descripcion = descripcion)
=======
@app.get("/mercancia/query/<descripcion>")
def query_m_des(*args, descripcion=None, **kwargs):
    try:
        respuesta = query_m_des(descripcion = descripcion)
>>>>>>> 1e27660ce027e9a37742d43b94b67f8710b6c99d
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)


#---------------------------------- Entradas ----------------------------


<<<<<<< HEAD
# Registrar una nueva entrada en formato json
# curl localhost:8080/storage_admin/entradas/register -X POST -H "Content-Type: application/json" -d '{"id_e": "ejem02","fecha_e": "2021-12-12","cantidad_e": "10"}'
=======
# curl localhost:8080/storage_admin/entradas/register -X POST -H "Content-Type: application/json" -d '{"name": "ejemplo","description": "ejemplo"}'
>>>>>>> 1e27660ce027e9a37742d43b94b67f8710b6c99d
@app.post("/entradas/register")
def create_category(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
        id_e = str(payload['id_e'])
        fecha_e = dt.date.fromisoformat(payload['fecha_e'])
        cantidad_e = str(payload['cantidad_e'])
        if len(id_e) == 0:
            raise Exception()
        print("dato validos")
<<<<<<< HEAD
        respuesta = msa.create_e(**payload)
=======
        respuesta = create_e(**payload)
>>>>>>> 1e27660ce027e9a37742d43b94b67f8710b6c99d
        print(respuesta)
    except:
        print("datos invalidos")
        raise bottle.HTTPError(400, "Invalid data")
    raise bottle.HTTPError(201, respuesta)


<<<<<<< HEAD
# Consultar todas las entradas existentes
# curl http://localhost:8080/storage_admin/entradas/query
@app.get("/entradas/query")
def get_entradas(*args, **kwargs):
    try:
       respuesta = msa.query_e()
=======

# curl http://localhost:8080/storage_admin//entradas/query
@app.get("/entradas/query")
def get_entradas(*args, **kwargs):
    try:
       respuesta = query_e()
>>>>>>> 1e27660ce027e9a37742d43b94b67f8710b6c99d
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)


<<<<<<< HEAD
# Consultar una entrada espesifica segun su ID
# curl http://localhost:8080/storage_admin/entradas/query/id_e/ejem02 -X GET
@app.get("/entradas/query/id_e/<id_e>")
def query_e_id(*args, id_e=None, **kwargs):
    try:
        respuesta = msa.query_e_id(id_e = id_e)
=======
# curl http://localhost:8080/storage_admin/entradas/query/ejemplos11-2010-12-12 -X GET
@app.get("/entradas/query/<id_e>")
def query_e_id(*args, id_e=None, **kwargs):
    try:
        respuesta = query_e_id(id_e = id_e)
>>>>>>> 1e27660ce027e9a37742d43b94b67f8710b6c99d
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)


<<<<<<< HEAD
# Consultar todas las entradss registradas con una fecha en comun
# curl http://localhost:8080/storage_admin/entradas/query/fecha_e/2021-12-12 -X GET
@app.get("/entradas/query/fecha_e/<fecha_e>")
def query_e_fec(*args, fecha_e=None, **kwargs):
    try:
        respuesta = msa.query_e_fec(fecha_e = fecha_e)
=======
@app.get("/entradas/query/<fecha_e>")
def query_e_fec(*args, fecha_e=None, **kwargs):
    try:
        respuesta = query_e_fec(fecha_e = fecha_e)
>>>>>>> 1e27660ce027e9a37742d43b94b67f8710b6c99d
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)


<<<<<<< HEAD
# Consultar todas las entradss registradas con la cantidad en comun
# curl http://localhost:8080/storage_admin/entradas/query/cantidad_e/10 -X GET
@app.get("/entradas/query/cantidad_e/<cantidad_e>")
def query_e_can(*args, cantidad_e=None, **kwargs):
    try:
        respuesta = msa.query_e_can(cantidad_e = cantidad_e)
=======

@app.get("/entradas/query/<cantidad_e>")
def query_e_can(*args, cantidad_e=None, **kwargs):
    try:
        respuesta = query_e_can(cantidad_e = cantidad_e)
>>>>>>> 1e27660ce027e9a37742d43b94b67f8710b6c99d
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)


#---------------------------------- Salidas ----------------------------


<<<<<<< HEAD
# Registrar una nueva salida en formato json
# curl localhost:8080/storage_admin/salidas/register -X POST -H "Content-Type: application/json" -d '{"id_s": "ejem03","fecha_s": "2021-01-01","cantidad_s": "25"}'
=======
# curl localhost:8080/storage_admin/salidas/register -X POST -H "Content-Type: application/json" -d '{"name": "ejemplo","description": "ejemplo"}'
>>>>>>> 1e27660ce027e9a37742d43b94b67f8710b6c99d
@app.post("/salidas/register")
def create_category(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
        id_s = str(payload['id_s'])
        fecha_s = dt.date.fromisoformat(payload['fecha_s'])
        cantidad_s = str(payload['cantidad_s'])
        if len(id_s) == 0:
            raise Exception()
        print("dato validos")
<<<<<<< HEAD
        respuesta = msa.create_s(**payload)
=======
        respuesta = create_s(**payload)
>>>>>>> 1e27660ce027e9a37742d43b94b67f8710b6c99d
        print(respuesta)
    except:
        print("datos invalidos")
        raise bottle.HTTPError(400, "Invalid data")
    raise bottle.HTTPError(201, respuesta)


# curl http://localhost:8080/storage_admin/salidas/query
@app.get("/salidas/query")
def get_salidas(*args, **kwargs):
    try:
<<<<<<< HEAD
       respuesta = msa.query_s()
=======
       respuesta = query_s()
>>>>>>> 1e27660ce027e9a37742d43b94b67f8710b6c99d
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)

<<<<<<< HEAD
# Consultar una entrada espesifica segun su ID
# curl http://localhost:8080/storage_admin/salidas/query/id_s/ejem03 -X GET
@app.get("/salidas/query/id_s/<id_s>")
def query_s_id(*args, id_s=None, **kwargs):
    try:
        respuesta = msa.query_s_id(id_s = id_s)
=======

# curl http://localhost:8080/storage_admin/salidas/query/ejemplos11-2010-12-12 -X GET
@app.get("/salidas/query/<id_s>")
def query_s_id(*args, id_s=None, **kwargs):
    try:
        respuesta = query_s_id(id_s = id_s)
>>>>>>> 1e27660ce027e9a37742d43b94b67f8710b6c99d
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)


<<<<<<< HEAD
# Consultar todas las entradss registradas con una fecha en comun
# curl http://localhost:8080/storage_admin/salidas/query/fecha_s/2021-01-01 -X GET
@app.get("/salidas/query/fecha_s/<fecha_s>")
def query_s_fec(*args, fecha_s=None, **kwargs):
    try:
        respuesta = msa.query_s_fec(fecha_s = fecha_s)
=======
@app.get("/salidas/query/<fecha_s>")
def query_s_fec(*args, fecha_s=None, **kwargs):
    try:
        respuesta = query_s_fec(fecha_s = fecha_s)
>>>>>>> 1e27660ce027e9a37742d43b94b67f8710b6c99d
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)


<<<<<<< HEAD
# Consultar todas las salidas registradas con la cantidad en comun
# curl http://localhost:8080/storage_admin/salidas/query/cantidad_s/25 -X GET
@app.get("/salidas/query/cantidad_s/<cantidad_s>")
def query_s_can(*args, cantidad_s=None, **kwargs):
    try:
        respuesta = msa.query_s_can(cantidad_s = cantidad_s)
=======
@app.get("/salidas/query/<cantidad_s>")
def query_s_can(*args, cantidad_s=None, **kwargs):
    try:
        respuesta = query_s_can(cantidad_s = cantidad_s)
>>>>>>> 1e27660ce027e9a37742d43b94b67f8710b6c99d
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)
