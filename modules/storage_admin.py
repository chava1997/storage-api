"""
Trabajo en progreso de modelos nesesarios
"""
import json
from datetime import datetime
from modules.storage import (
    store_string, store_bytes,
    query_storage, get_storage_file
)


#------------------------------- Mercancias ----------------------------------
#crear mercancia
def create_m(descripcion=None, presentacion=None, clave=None):
    print("Desde Modulo store")
    print(descripcion, presentacion, clave)
    print("Exito")
    almacenable = {
        "descripcion": descripcion,
        "presentacion": presentacion,
        "clave": clave,
    }
    nombre_de_archivo = f"{descripcion}-{presentacion}-{clave}.json"
    datos = store_string(
        "storage_admin/mercancia",
        nombre_de_archivo,
        json.dumps(almacenable)
    )
    return datos



#Consultar mercancias
def query_m(mercancia=None):
    query_result = query_storage(
        "storage_admin/mercancia",
    )
    return query_result["content"]


#consultar mercancia por clave
def query_m_cla(clave=None):
    query_result = query_storage(
        "storage_admin/mercancia",
    )
    if clave == clave:
        return [
           r
           for r in query_result["content"]
           if clave in r
        ]
    print("todo bien")


#consultar mercancia por descripcion
def query_m_des(descripcion=None):
    query_result = query_storage(
        "storage_admin/mercancia",
    )
    if descripcion is not None:
        return [
           r
           for r in query_result["content"]
           if descripcion in r
        ]
    print("todo bien")



#--------------------------------- Entradas ----------------------------------


## Crear entrada
def create_e(id_e=None, fecha_e=None, cantidad_e=None):
    print("Desde Modulo store")
    print(id_e, fecha_e, cantidad_e)
    print("Exito")
    almacenable = {
        "id_e": id_e,
        "fecha_e": fecha_e,
        "cantidad_e": cantidad_e
    }
    nombre_de_archivo = f"{id_e}-{fecha_e}-{cantidad_e}.json"
    datos = store_string(
        "storage_admin/entradas",
        nombre_de_archivo,
        json.dumps(almacenable)
    )
    return datos


#consulta entradas
def query_e(id_e=None):
    query_result = query_storage(
        "storage_admin/entradas",
    )
    return query_result["content"]


#consultar entrada por ID
def query_e_id(id_e=None):
    query_result = query_storage(
        "storage_admin/entradas",
    )
    if id_e is not None:
        return [
           r
           for r in query_result["content"]
           if id_e in r
        ]
    print("todo bien")


#consultar entrada por fecha
def query_e_fec(fecha_e=None):
    query_result = query_storage(
        "storage_admin/entradas",
    )
    if fecha_e is not None:
        return [
           r
           for r in query_result["content"]
           if fecha_e in r
        ]
    print("todo bien")



#consultar entrada por contidad
def query_e_can(cantidad_e=None):
    query_result = query_storage(
        "storage_admin/entradas",
    )
    if cantidad_e is not None:
        return [
           r
           for r in query_result["content"]
           if cantidad_e in r
        ]
    print("todo bien")

#------------------------------------ Salidas ---------------------------------


## Crear salida
def create_s(id_s=None, fecha_s=None, cantidad_s=None):
    print("Desde Modulo store")
    print(id_s, fecha_s, cantidad_s)
    print("Exito")
    almacenable = {
        "id_s": id_s,
        "fecha_s": fecha_s,
        "cantidad_s": cantidad_s
    }
    nombre_de_archivo = f"{id_s}-{fecha_s}-{cantidad_s}.json"
    datos = store_string(
        "storage_admin/salidas",
        nombre_de_archivo,
        json.dumps(almacenable)
    )
    return datos


#consulta salidas
def query_s(id_s=None):
    query_result = query_storage(
        "storage_admin/salidas",
    )
    return query_result["content"]


#consultar salida por ID
def query_s_id(id_s=None):
    query_result = query_storage(
        "storage_admin/salidas",
    )
    if id_s is not None:
        return [
           r
           for r in query_result["content"]
           if id_s in r
        ]
    print("todo bien")


#consultar salida por fecha
def query_s_fec(fecha_s=None):
    query_result = query_storage(
        "storage_admin/salidas",
    )
    if fecha_s is not None:
        return [
           r
           for r in query_result["content"]
           if fecha_s in r
        ]
    print("todo bien")



#consultar salida por contidad
def query_s_can(cantidad_s=None):
    query_result = query_storage(
        "storage_admin/salidas",
    )
    if cantidad_s is not None:
        return [
           r
           for r in query_result["content"]
           if cantidad_s in r
        ]
    print("todo bien")
