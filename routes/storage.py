import json
import bottle
from modules.cors import enable_cors
import modules.bottles
import modules.utils as utils
from modules.auth import auth_required
from modules.storage import (
    store_bytes,
    store_string,
    query_storage,
    get_storage_file
)

app = modules.bottles.BottleJson()


@app.get("/info")
def info():
    raise bottle.HTTPError(401, "Error")


@app.route("/file", method=["POST", "OPTIONS"])
@enable_cors
def route_file(*args, **kwargs):
    """
    This function provides a way to store a single file.
    It recieves a regular html form with a single field named
    `file`.
    """
    file = bottle.request.files.get("file")
    # bottle.request.files.keys()
    #
    # file = bottle.request.file.get(nombre_de_input)
    # file.filename
    # file.file, aplicar la funcion file.file.read()
    # raise HTTPError(406, "Tipo de archivo invalido")
    # filename = get_license_name()
    # store_bytes("files", "certificado.xyz", file.file.read())
    store_bytes("files", file.filename, file.file.read())
    bottle.response.status = 201
    bottle.response.content_type = "application/json"
    return dict(store="success")


@app.route("/json", method=["POST", "OPTIONS"])
@enable_cors
def route_json(*args, **kwargs):
    payload = bottle.request.json
    now_str = utils.get_timestamp()
    _hash = (
        f"{now_str}_hash_{hash((now_str, tuple(payload.keys())))}"
    ).replace(":", "=")
    formname = payload.get("formname", None)
    data = dict(
        ref=_hash,
        datetime=now_str,
        formname=formname,
        payload=payload,
        source=payload.get("source")
    )
    store_string("json", f"{_hash}.json", json.dumps(data))
    bottle.response.status = 201
    bottle.response.content_type = "application/json"
    return dict(store="success", ref=_hash)


@app.route("/query", method=["GET", "OPTIONS"])
@app.route("/query/", method=["GET", "OPTIONS"])
@app.route("/query/<file:path>", method=["GET", "OPTIONS"])
@enable_cors
@auth_required
def query(*args, file="", **kwargs):
    bottle.response.status = 200
    bottle.response.content_type = "application/json"
    return query_storage(file)


@app.route("/download/<file:path>", method=["GET", "OPTIONS"])
@enable_cors
@auth_required
def download(*args, file="", **kwargs):
    bottle.response.status = 200
    mime, _bytes = get_storage_file(file)
    bottle.response.content_type = mime
    return _bytes
