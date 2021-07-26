import json
from time import time
import bottle
from modules.bottles import BottleJson
from modules.auth import auth_required
from modules.storage import store_string, get_storage_file
from models.example import ExampleRecord

app = BottleJson()


@app.get("/")
@app.get("/<name>")
@app.get("/<name>/<age:int>")
def index(name="mariano", age=10):
    payload = bottle.request.query
    print(name)
    print(bottle.request.query_string)
    print(payload.dict)
    print(name, age)
    raise bottle.HTTPError(501, 'Error')

@app.post("/")
def index_post():
    payload = bottle.request.json
    print(payload)
    raise bottle.HTTPError(501, 'Error')


@app.get("/auth/simple")
@auth_required
def route_auth_for_anyone():
    return dict(code=200, message="OK")


@app.get("/auth/role")
@auth_required("example", "example:store:write", "example:store:read")
def route_auth_for_example_role():
    return dict(code=200, message="OK")


@app.post("/store")
@auth_required("example:store:write")
def storage_a_file():
    payload = bottle.request.json
    data = "\n".join(payload.items())
    filename = f"{time()}.txt"
    store_string("example", filename, data)
    return dict(code=201, message="Created")


@app.get("/store/<path>")
@auth_required("example:store:read")
def storage_get_a_file(path=None):
    mime, _bytes = get_storage_file(path)
    bottle.response.content_type = mime
    return _bytes


@app.post("/database/test")
@auth_required("example:store:write")
def database_create_test_record():
    return dict(code=201, message="Created")


@app.get("/database/test/<name>")
@auth_required("example:store:read")
def database_query_test_record(name=None):
    return dict(code=201, message="Created")
