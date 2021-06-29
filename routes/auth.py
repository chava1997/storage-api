import bottle
from modules.auth import validate_user, register_user, generate_token


app = bottle.Bottle()


@app.get("/")
def root_index(*args, **kwargs):
    print("I'm in auth")
    return dict(code=200)


@app.route("/signup", method=["POST", "OPTIONS"])
def auth_signup(*args, **kwargs):
    payload = bottle.request.json
    if not payload:
        raise Exception("Not valid data")
    if payload.get("password_confirmation") == payload.get("password"):
        del payload["password_confirmation"]
    if user := register_user(**payload):
        bottle.response.status = 201
        bottle.response.content_type = "application/json"
        return dict(code=201, user_id=user.id)
    bottle.response.status = 401
    bottle.response.content_type = "application/json"
    return dict(code=401)


@app.route("/login", method=["POST", "OPTIONS"])
def auth_login(*args, **kwargs):
    payload = bottle.request.json
    if not payload:
        raise Exception("Not valid data")
    print(payload)
    if validate_user(**payload):
        del payload["password"]
        token = generate_token(payload)
        bottle.response.status = 200
        bottle.response.content_type = "application/json"
        return dict(code=200, token=token)
    print("auth failed")
    bottle.response.status = 401
    bottle.response.content_type = "application/json"
    return dict(code=401)
