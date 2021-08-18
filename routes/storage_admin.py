import bottle
import datetime as dt
from bottle import route, run, post, request
from modules.bottles import BottleJson
from modules.storage_admin import  create_m, query_m, create_e, query_e, create_s, query_s, query_m_cla, query_m_des, query_e_id, query_e_fec, query_e_can, query_s_id, query_s_fec, query_s_can
app = BottleJson()
# gogole.com/s?hola=mundo&boo=fantasam&fo=bar
# curl http://localhost:8080/storage_admin/foo -X GET
@app.get("/foo")
def foo(*args, **kwargs):
    payload = bottle.request.query
    print(bottle.request.query)
    print(payload.dict)
    raise bottle.HTTPError(501,"error")

# curl http://localhost:8080/storage_admin/bar -X POST -H 'Content-Type: application/json' -d '{"un": "json"}'
@app.post("/bar")
def bar(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    raise HTTPError(501)


#-------------------------------- Mercancia ----------------------------


# curl localhost:8080/storage_admin/mercancia/register -X POST -H "Content-Type: application/json" -d '{"descripcion": "mangera de 3/4","presentacion":"caja con 32 unidades","clave": "maca1"}'
@app.post("/mercancia/register")
def store(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
        descripcion = str(payload['descrpcion'])
        presentacion = str(payload['presentacion'])
        clave = str(payload['clave'])

        if len(descripcion) == 0:
            raise Exception()
        print("dato validos")
        respuesta = create_m(**payload)
        print(respuesta)
    except:
        print("datos invalidos")
        raise bottle.HTTPError(400, "Invalid data")
    raise bottle.HTTPError(201, respuesta)




# curl http://localhost:8080/storage_admin/mercancia/query
@app.get("/mercancia/query")
def get_mercancias(*args, **kwargs):
    try:
       respuesta = query_m()
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)


# curl http://localhost:8080/storage_admin/mercancia/query/ejemplos11-2010-12-12 -X GET
@app.get("/mercancia/query/<clave>")
def query_m_cla(*args, clave=None, **kwargs):
    try:
        respuesta = query_m_cla(clave = clave)
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)


@app.get("/mercancia/query/<descripcion>")
def query_m_des(*args, descripcion=None, **kwargs):
    try:
        respuesta = query_m_des(descripcion = descripcion)
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)


#---------------------------------- Entradas ----------------------------


# curl localhost:8080/storage_admin/entradas/register -X POST -H "Content-Type: application/json" -d '{"name": "ejemplo","description": "ejemplo"}'
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
        respuesta = create_e(**payload)
        print(respuesta)
    except:
        print("datos invalidos")
        raise bottle.HTTPError(400, "Invalid data")
    raise bottle.HTTPError(201, respuesta)



# curl http://localhost:8080/storage_admin//entradas/query
@app.get("/entradas/query")
def get_entradas(*args, **kwargs):
    try:
       respuesta = query_e()
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)


# curl http://localhost:8080/storage_admin/entradas/query/ejemplos11-2010-12-12 -X GET
@app.get("/entradas/query/<id_e>")
def query_e_id(*args, id_e=None, **kwargs):
    try:
        respuesta = query_e_id(id_e = id_e)
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)


@app.get("/entradas/query/<fecha_e>")
def query_e_fec(*args, fecha_e=None, **kwargs):
    try:
        respuesta = query_e_fec(fecha_e = fecha_e)
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)



@app.get("/entradas/query/<cantidad_e>")
def query_e_can(*args, cantidad_e=None, **kwargs):
    try:
        respuesta = query_e_can(cantidad_e = cantidad_e)
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)


#---------------------------------- Salidas ----------------------------


# curl localhost:8080/storage_admin/salidas/register -X POST -H "Content-Type: application/json" -d '{"name": "ejemplo","description": "ejemplo"}'
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
        respuesta = create_s(**payload)
        print(respuesta)
    except:
        print("datos invalidos")
        raise bottle.HTTPError(400, "Invalid data")
    raise bottle.HTTPError(201, respuesta)


# curl http://localhost:8080/storage_admin/salidas/query
@app.get("/salidas/query")
def get_salidas(*args, **kwargs):
    try:
       respuesta = query_s()
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)


# curl http://localhost:8080/storage_admin/salidas/query/ejemplos11-2010-12-12 -X GET
@app.get("/salidas/query/<id_s>")
def query_s_id(*args, id_s=None, **kwargs):
    try:
        respuesta = query_s_id(id_s = id_s)
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)


@app.get("/salidas/query/<fecha_s>")
def query_s_fec(*args, fecha_s=None, **kwargs):
    try:
        respuesta = query_s_fec(fecha_s = fecha_s)
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)


@app.get("/salidas/query/<cantidad_s>")
def query_s_can(*args, cantidad_s=None, **kwargs):
    try:
        respuesta = query_s_can(cantidad_s = cantidad_s)
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)
