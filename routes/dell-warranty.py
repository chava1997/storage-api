from os import environ
from json import dumps as json_dumps
import bottle

STORAGE_METHOD = environ["STORAGE_METHOD"]
if STORAGE_METHOD == 'LOCAL':
    print("Using local storage")
    from modules.storage import (
        store_bytes,
        store_string,
        query_storage,
        get_storage_file
    )
elif STORAGE_METHOD == 'GCLOUD':
    print("Using gcloud storage")
    from modules.gstorage import (
        store_bytes,
        store_string,
        query_storage,
        get_storage_file
    )
else:
    raise Exception("Storage method not set")

app = bottle.Bottle()


@app.get("/store")
def store_record(*args, **kwargs):
    # data = bottle.request.json
    # filename = ""
    # store_string("dell", filename, json_dumps(data))
    return dict(code=200)


@app.get("/info/<code>")
def info_by_code(*args, code=None, **kwargs):
    pass
    return dict(code=200)


@app.get("/void")
def void_report(*args, **kwargs):
    return dict(code=200)
