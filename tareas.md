
 1. [ ] Implementar `BottleJson` como objeto para `app`.
    - (Editar su archivo de rutas e.j. `routes/example.py`)

```python
import bottle
from modules.bottles import BottleJson
app = BottleJson()
```


 2. [ ] Instalar aplicacion al router de la aplicacion principal de bottle.
   - Agregar la declaracion de `import routes.<tu-proyecto>` (sin `.py` obviamente).
   - En la seccion donde se encuentran los `app.mount`, agregar la ruta que
   ustedes usaran, (ejemplo `/example`), y su objeto `app`.
   - (Editar `main.py`)


```
import routes.example
#
# ...
#
app.mount("/example", routes.example.app)
```

 3. [ ] Recibir datos de la peticion a la variable `payload`, e imprimir los datos en la terminal.
    - Si es un `GET` la variable `bottle.request.query`
    - Si es un `POST` la variable `bottle.request.query`

```
@app.get("/foo")
def foo(*args, **kwargs):
    payload = bottle.request.query.dict
    print(payload)
    raise HTTPError(501)


@app.post("/bar")
def bar(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    raise HTTPError(501)
```


 4. [ ] Validar la existencia y formato de los datos en la variable payload.

```python
@app.post("/bar")
def bar(*args, **kwargs):
    """
    Supongamos que solicitamos la informacion
    nombre, fecha, edad.
    fecha formato: YYYY-MM-DD
    """
    payload = bottle.request.json
    print(payload)
    try:
        edad = int(payload['edad'])
        nombre = str(payload['nombre'])
        if len(nombre) == 0:
            raise Exception()
        fecha = str(payload['fecha'])
        # Validacion de fecha
        year, month, date = [int(x) for x in fecha.split("-")]
        print("Datos validos")
    except:
        print("Datos invalidos")
        raise HTTPError(400)
    raise HTTPError(501)
```


 5. [ ] Escribir funciones en el archivo `modules/<tu-proyecto>.py`, que seran llamadas dentro de las rutas, con el contendio de la variable `payload`, algunos ejemplos de esto serian.


```python
# Dentro de `routes/<tu-proyecto>.py`

from modules.<tu-projecto> import almacenar_dato
#
# ...
#

@app.post("/bar")
def bar(*args, **kwargs):
    """
    Supongamos que solicitamos la informacion
    nombre, fecha, edad.
    fecha formato: YYYY-MM-DD
    """
    payload = bottle.request.json
    print(payload)
    try:
        edad = int(payload['edad'])
        nombre = str(payload['nombre'])
        if len(nombre) == 0:
            raise Exception()
        fecha = str(payload['fecha'])
        # Validacion de fecha
        year, month, date = [int(x) for x in fecha.split("-")]
        print("Datos validos")
        respuesta = almacenar_dato(**payload)
        raise HTTPError(201, respuesta)
    except:
        print("Datos invalidos")
        raise HTTPError(400)
    raise HTTPError(500)
```

```python
# Archivo modules/<tu-proyecto>.py

def almacenar_dato(nombre=None, edad=None, fecha=None):
    print("Desde modulo")
    print(nombre, edad, fecha)
    return "Exito"

```


6. [ ] Poblar con la logica correspondiente, las funciones
contenidas en `modules/<tu-proyecto>.py`.


```python
# Archivo modules/<tu-proyecto>.py

import json
from modules.storage import *

#
# ...
#

def almacenar_dato(nombre=None, edad=None, fecha=None):
    print("Desde modulo")
    print(nombre, edad, fecha)
    para_almacenar = {"nombre": nombre, "edad": edad, "fecha": fecha}
    json_text = json.dumps(para_almacenar)
    store_string('mi-carpeta', nombre, para_almacenar)
    return "Exito"
```

