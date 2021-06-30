import json
import datetime as dt
import bottle

from modules.storage import (
    store_string,
)

app = bottle.Bottle()


@app.post("/alumno")
def alumno_registro():
    datos = bottle.request.json
    if 'nombre' in datos and 'fecha_de_nacimiento' in datos:
        bd = dt.date.fromisoformat(datos['fecha_de_nacimiento'])
        print(bd)
        print(datos)
        store_string(
            "school/alumnos",
            "matricula.json",
            json.dumps(datos)
        )
        return datos
    return {}


@app.get("/alumno/listar")
def alumno_lista():
    return {}


@app.get("/alumno/<matricula>")
def alumno_por_matricula(matricula):
    return {}


@app.post("/docente")
def docente_registro():
    return {}


@app.get("/docente/list")
def docente_listar():
    return {}


@app.get("/docente/<no_emp>")
def docente_por_no_emp(no_emp):
    return {}


@app.post("/materia")
def materia_registro():
    return {}


@app.post("/materia/<periodo>/<clave>/<matricula>/registrar")
def materia_registrar_alumno(periodo, clave, matricula):
    return {}


@app.post("/materia/<periodo>/<clave>/<matricula>/calificar")
def materia_calificar_alumno(periodo, clave, matricula):
    return {}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
