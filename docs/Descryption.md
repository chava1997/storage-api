<<<<<<< HEAD
### Store_Admin

# Estructura General del proyecto

## Introduccion a Store_Admin

La principal funcion de Store_Admin es poder dar de alta, de baja y consultar la mercancia de una bodega de forma eficiente y facil; asi como poder hacer consultas de el stock que hay bodega desde cualquier lugar.

El enfoque de este proyecto son empresas pequeñas, que quieren tener un control virtual de la mercancia que entra y sale de su bodega y que desea poder tener acceso a  esta informacion desde cualquier lugar

---

## Que es Store_Admin?

### Motivaciones y propocitos de Store_Admin

la principal motivacion para desarrollar el proyecto es tener la capacidad de administrar de mejor manera flujos de bodega de una forma facil y poder tener la informacion a la mano en cualquier lugar, con el proposito de se una alternativa solida al mometo de pensar en software de administracion de bodega.

### Razon de ser de Store_Admin

A continuacion se contestan algunas preguntas que pueden surgir al respecto de este proyecto.

- ¿Quien es el publico objetivo de este proyecto?
El publico principal de este proyecto son las empresas pequeñas que tienen un flujo bajo de entradas y salidas de mercancia en su bodega y que desean poder accesar a la informacion de de esta desde cualquier lugar.

- ¿Cual es la solucion especifica que plantea este proyecto? La fata de un softwar de administracion de flujo de bodega, el cual peda ser consultado desde cualquier lugar mediante un apagina web.

- ¿Que recursos se necesitan para iniciar trabajo sobre este proyecto?
(Recurso humano, recurso de computo, infrestructura para el despligue)
  - Dispositivo con conexion a internet
  - ordenador capas de correr codigo de python y un entorno http
  - Persona con conocimeinto basico en formatos json, http, python

  - ¿Que se ocupara hacer una ves se implemente el proyecto?
  Comenzar a registrar de forma manual el flujo de bodega (tanto las entradas como las salidas) y entrar a la pagina web de consulta donde se almacenan todos los registros del sistema.

  ---

## API
#### Application Programing Interface

Entidades con las cuales funcoonara la API

- Mercancia (Clave, Descripcion, presentacion)
- Entrada (ID-entrada, Fecha-entrada, Cantidad-entrada)
- Salida (ID-salida, Fecha-salida, Cantidad-salida)



## CRUD (Create, Read, Update, Delete).

### Operaciones de Almacenamiento de datos


####Operaciones de Mercancia

###### Registrar una nueva mercancia
- Solicitar descripcion de la Mercancia
- Solicitar la presentacion en la que viene la mercancia (ejemplo: caja con 4 unidades)
- la clave se generara de manera automatica

#### Operaciones de Flujo de bodega

###### registrar una entrada de mercancia
- solicitar la clave de mercancia
- solicitar la fecha de entrada de la Mercancia
- Solicitar la cantidad de unidades que entran a bodega
- El identificador se genera automaticamente

###### registrar una salidas de mercancia
- solicitar la clave de mercancia
- solicitar la fecha de entrada de la Mercancia
- Solicitar la cantidad de unidades que entran a bodega
- El identificador se genera automaticamente

De esta forma se almacearan los datos



#### Operaciones de consulta de datos

- Consultar mercrancias
  - Por codigo
  - Por descripcion

- Consultr entradas
  - Por identificador
  - Por fecha

- Consultar salida
- Por identificador
- Por fecha

---


## Estructuras de solicitud y respuesta

###Registro de mercancia
```         
{
 "descripcion": "Asi es la mercancia", "presentacion": "", "presentacion": "Este empaque contiene n piezas"
}
```

### Respuesta de registro de mercancia exitoso
```         
{
"code": 201, "message": "La mercacia se registro exitosamente"
}
```

### Mensaje de fallo
```          
{
"code": 500, "message": "No se pudo registrar la mercancia"
}
```

### Registro de entrada
```
{
"clave": "F1","fecha-entrada": "01-01-2021", "cantidad-entrada": "5"
}
```

### Respuesta de entrada registrada exitosamente
```          
{
"code": 201, "message": "Entrada registrada exitosamente"
}
```

### Respuesta de error al registrar entrada
```
{
"code": 500, "message": "No se pudo registrar la entrada"
}
```

### Registro de salida
```
{
"clave": "F1","fecha-salida": "12-12-2021", "cantidad-salida": "5"
}
```

### Respuesta de salida registrada exitosamente
```          
{
"code": 201, "message": "Salida registrada exitosamente"
}
```

### Respuesta de error al registrar salida
```
{
"code": 500, "message": "No se pudo registrar la salida"
}
```
---



## Rutas de la API

| Path                  | Descripción |
| --------------------- | ----------- |
| `/mercancia/query`           | Se podran consultar las mercancias almacenadas con su descripcion |
| `/mercancia/query/<descripcion>`     | Se podran consultar la mercancia que contenga esa descripcion  |
| `/mercancia/query/<clave>` | Se mostrara una mercancia en espesifico segun su clave |
| `/entradas/query`        | Se podran consultar entradas almacenadas |
| `/entradas/query/<ID-entrada>`     | Se mostrara una entrada en espesifico segun su ID   |
| `/entradas/query/<cantidad-entrada>`     | Se podran consultar las entradas con una cantidad espesifica  |
| `/entradas/query/<fecha-entrada>`     | Se podran consultar las entradas de una fecha espesifica  |
| `/salidas/query`        | Se podran consultar salidas almacenadas |
| `/salidas/query/<ID-salida>`     | Se mostrara una salida en espesifico segun su ID   |
| `/salidas/query/<cantidad-salida>`     | Se podran consultar las salidas con una cantidad espesifica  |
| `/salidas/query/<fecha-salida>`     | Se podran consultar las salidas de una fecha espesifica  |
| `/mercancia/register`            | Se podra registrar una nueva mercancia |
| `/entradas/register` | Se podra registrar una nueva entrada |
| `/salidas/register` | Se podra registrar una nueva salida |

---
agregar verbos HTTP ^
---

## Implementación de rutas para los recursos

### POST /mercancia/register
- Recibe datos de registro de mercancia
- 201,Crear registro de la mercancia y regresar clave de la mercancia
- D.O.M, regresa estructura de mensaje de fallo

### GET /mercancia/query/<clave>
- Recibe el identificador correspondiente a una mercancia
- 200 regresa la mercancia que corresponda
- D.O.M, regresa mensaje de mercancia no encontrada 404

### GET /mercancia/query/<descripcion>
- Recibe la descripcion de la mercancia
- 200, regresa la mercancia que contenga esa descripcion
- D.O.M, regresa mensaje de mercancia no encontrada

### POST /entrada/register
- Recibe datos de registro de entrada
- 201,Crear registro de la entrada y regresar el identificador de la entrada
- D.O.M, regresa estructura de mensaje de fallo

### GET /entradas/query/<ID-entrada>
- Recibe el identificador de la entrada
- 200, regresa la entrada que corresponda a ese identificador
- D.O.M, regresa mensaje de entrada no encontrada

### GET /entradas/query/<cantidad-entrada>
- Recibe la cantidad que contiene la entrada
- 200, regresa las entradas que contengan esa cantidad
- D.O.M, regresa mensaje de entrada no encontrada

### GET /entradas/query/<fecha-entrada>
- Recibe una fecha espesifica
- 200, regresa las entras que se hayan registrado con esa fecha
- D.O.M, regresa mensaje de entrada no encontrada

### POST /salidas/register
- 201, registrar una nueva categoria
- D.O.M, regresa mensaje de fallo

### GET /salidas/query/<ID-entrada>
- Recibe el identificador de la salida
- 200, regresa la salida que corresponda a ese identificador
- D.O.M, regresa mensaje de salida no encontrada

### GET /salidas/query/<cantidad-entrada>
- Recibe la cantidad que contiene la salida
- 200, regresa las salidas que contengan esa cantidad
- D.O.M, regresa mensaje de salida no encontrada

### GET /salidas/query/<fecha-entrada>
- Recibe una fecha espesifica
- 200, regresa las salida que se hayan registrado con esa fecha
- D.O.M, regresa mensaje de salida no encontrada

---



## Ejemplos de consultas

### DATA=$(cat /path/to/file)
```
curl -qv \
  ${URL_HOST}${ROUTE} \
  -X ${METHOD} \
  -H "${HEADER_1}" \
  -H "${HEADER_2}" \
  -d "$DATA"
```
### Ejemplo de creacion de registro de mercancia
En este ejemplo se registrara una mercancia nueva, primero se requiere conectar al servidor donde se encuentre corriendo el programa y posteriormente, definir la ruta que se utilizara, depues de esto el programa requiere resibir un usuario para poder crear el registro, para esto el programa valida al usuario (determina si es posible para el usuario crear el registro o no), despues de eso se solicita la informacion de la mercancia y al momento de crear el registro se agrega el identificador reconocido como `KEY`, con esto se habra creado el registro de la mercancia de forma exitosa.


```
URL_HOST=http://localhost:8080 \
ROUTE=/mercancia/register \
METHOD=POST \
HEADER_1='Content-Type: application/json' \
HEADER_2="Authorization: Bearer ${TOKEN}" \
DATA='{"descripcion":"esta es la mercancia", "presentacion":"paquete con 4 unidades"}' \
```


## Archivos Relacionados

- `routes/Store_Admin.py`
- `routes/auth.py`
- `routes/storage`


## Almacenamiento

Todas los registros seran en formato JSON y se almacenaran o en la nube.
>Los datos se almacenan en la nube para poder consultar la informacion desde cualquier lugar
=======
### Store_Admin

# Estructura General del proyecto

## Introduccion a Store_Admin

La principal funcion de Store_Admin es poder dar de alta, de baja y consultar la mercancia de una bodega de forma eficiente y facil; asi como poder hacer consultas de el stock que hay bodega desde cualquier lugar.

El enfoque de este proyecto son empresas pequeñas, que quieren tener un control virtual de la mercancia que entra y sale de su bodega y que desea poder tener acceso a  esta informacion desde cualquier lugar

---

## Que es Store_Admin?

### Motivaciones y propocitos de Store_Admin

la principal motivacion para desarrollar el proyecto es tener la capacidad de administrar de mejor manera flujos de bodega de una forma facil y poder tener la informacion a la mano en cualquier lugar, con el proposito de se una alternativa solida al mometo de pensar en software de administracion de bodega.

### Razon de ser de Store_Admin

A continuacion se contestan algunas preguntas que pueden surgir al respecto de este proyecto.

- ¿Quien es el publico objetivo de este proyecto?
El publico principal de este proyecto son las empresas pequeñas que tienen un flujo bajo de entradas y salidas de mercancia en su bodega y que desean poder accesar a la informacion de de esta desde cualquier lugar.

- ¿Cual es la solucion especifica que plantea este proyecto? La fata de un softwar de administracion de flujo de bodega, el cual peda ser consultado desde cualquier lugar mediante un apagina web.

- ¿Que recursos se necesitan para iniciar trabajo sobre este proyecto?
(Recurso humano, recurso de computo, infrestructura para el despligue)
  - Dispositivo con conexion a internet
  - ordenador capas de correr codigo de python y un entorno http
  - Persona con conocimeinto basico en formatos json, http, python

  - ¿Que se ocupara hacer una ves se implemente el proyecto?
  Comenzar a registrar de forma manual el flujo de bodega (tanto las entradas como las salidas) y entrar a la pagina web de consulta donde se almacenan todos los registros del sistema.

  ---

## API
#### Application Programing Interface

Entidades con las cuales funcoonara la API

- Mercancia (Clave, Descripcion, presentacion)
- Entrada (ID-entrada, Fecha-entrada, Cantidad-entrada)
- Salida (ID-salida, Fecha-salida, Cantidad-salida)



## CRUD (Create, Read, Update, Delete).

### Operaciones de Almacenamiento de datos


####Operaciones de Mercancia

###### Registrar una nueva mercancia
- Solicitar descripcion de la Mercancia
- Solicitar la presentacion en la que viene la mercancia (ejemplo: caja con 4 unidades)
- la clave se generara de manera automatica

#### Operaciones de Flujo de bodega

###### registrar una entrada de mercancia
- solicitar la clave de mercancia
- solicitar la fecha de entrada de la Mercancia
- Solicitar la cantidad de unidades que entran a bodega
- El identificador se genera automaticamente

###### registrar una salidas de mercancia
- solicitar la clave de mercancia
- solicitar la fecha de entrada de la Mercancia
- Solicitar la cantidad de unidades que entran a bodega
- El identificador se genera automaticamente

De esta forma se almacearan los datos



#### Operaciones de consulta de datos

- Consultar mercrancias
  - Por codigo
  - Por descripcion

- Consultr entradas
  - Por identificador
  - Por fecha

- Consultar salida
- Por identificador
- Por fecha

---


## Estructuras de solicitud y respuesta

###Registro de mercancia
```         
{
 "descripcion": "Asi es la mercancia", "presentacion": "", "presentacion": "Este empaque contiene n piezas"
}
```

### Respuesta de registro de mercancia exitoso
```         
{
"code": 201, "message": "La mercacia se registro exitosamente"
}
```

### Mensaje de fallo
```          
{
"code": 500, "message": "No se pudo registrar la mercancia"
}
```

### Registro de entrada
```
{
"clave": "F1","fecha-entrada": "01-01-2021", "cantidad-entrada": "5"
}
```

### Respuesta de entrada registrada exitosamente
```          
{
"code": 201, "message": "Entrada registrada exitosamente"
}
```

### Respuesta de error al registrar entrada
```
{
"code": 500, "message": "No se pudo registrar la entrada"
}
```

### Registro de salida
```
{
"clave": "F1","fecha-salida": "12-12-2021", "cantidad-salida": "5"
}
```

### Respuesta de salida registrada exitosamente
```          
{
"code": 201, "message": "Salida registrada exitosamente"
}
```

### Respuesta de error al registrar salida
```
{
"code": 500, "message": "No se pudo registrar la salida"
}
```
---



## Rutas de la API

| Path                  | Descripción |
| --------------------- | ----------- |
| `/mercancia/query`           | Se podran consultar las mercancias almacenadas con su descripcion |
| `/mercancia/query/<descripcion>`     | Se podran consultar la mercancia que contenga esa descripcion  |
| `/mercancia/query/<clave>` | Se mostrara una mercancia en espesifico segun su clave |
| `/entradas/query`        | Se podran consultar entradas almacenadas |
| `/entradas/query/<ID-entrada>`     | Se mostrara una entrada en espesifico segun su ID   |
| `/entradas/query/<cantidad-entrada>`     | Se podran consultar las entradas con una cantidad espesifica  |
| `/entradas/query/<fecha-entrada>`     | Se podran consultar las entradas de una fecha espesifica  |
| `/salidas/query`        | Se podran consultar salidas almacenadas |
| `/salidas/query/<ID-salida>`     | Se mostrara una salida en espesifico segun su ID   |
| `/salidas/query/<cantidad-salida>`     | Se podran consultar las salidas con una cantidad espesifica  |
| `/salidas/query/<fecha-salida>`     | Se podran consultar las salidas de una fecha espesifica  |
| `/mercancia/register`            | Se podra registrar una nueva mercancia |
| `/entradas/register` | Se podra registrar una nueva entrada |
| `/salidas/register` | Se podra registrar una nueva salida |

---
agregar verbos HTTP ^
---

## Implementación de rutas para los recursos

### POST /mercancia/register
- Recibe datos de registro de mercancia
- 201,Crear registro de la mercancia y regresar clave de la mercancia
- D.O.M, regresa estructura de mensaje de fallo

### GET /mercancia/query/<clave>
- Recibe el identificador correspondiente a una mercancia
- 200 regresa la mercancia que corresponda
- D.O.M, regresa mensaje de mercancia no encontrada 404

### GET /mercancia/query/<descripcion>
- Recibe la descripcion de la mercancia
- 200, regresa la mercancia que contenga esa descripcion
- D.O.M, regresa mensaje de mercancia no encontrada

### POST /entrada/register
- Recibe datos de registro de entrada
- 201,Crear registro de la entrada y regresar el identificador de la entrada
- D.O.M, regresa estructura de mensaje de fallo

### GET /entradas/query/<ID-entrada>
- Recibe el identificador de la entrada
- 200, regresa la entrada que corresponda a ese identificador
- D.O.M, regresa mensaje de entrada no encontrada

### GET /entradas/query/<cantidad-entrada>
- Recibe la cantidad que contiene la entrada
- 200, regresa las entradas que contengan esa cantidad
- D.O.M, regresa mensaje de entrada no encontrada

### GET /entradas/query/<fecha-entrada>
- Recibe una fecha espesifica
- 200, regresa las entras que se hayan registrado con esa fecha
- D.O.M, regresa mensaje de entrada no encontrada

### POST /salidas/register
- 201, registrar una nueva categoria
- D.O.M, regresa mensaje de fallo

### GET /salidas/query/<ID-entrada>
- Recibe el identificador de la salida
- 200, regresa la salida que corresponda a ese identificador
- D.O.M, regresa mensaje de salida no encontrada

### GET /salidas/query/<cantidad-entrada>
- Recibe la cantidad que contiene la salida
- 200, regresa las salidas que contengan esa cantidad
- D.O.M, regresa mensaje de salida no encontrada

### GET /salidas/query/<fecha-entrada>
- Recibe una fecha espesifica
- 200, regresa las salida que se hayan registrado con esa fecha
- D.O.M, regresa mensaje de salida no encontrada

---



## Ejemplos de consultas

### DATA=$(cat /path/to/file)
```
curl -qv \
  ${URL_HOST}${ROUTE} \
  -X ${METHOD} \
  -H "${HEADER_1}" \
  -H "${HEADER_2}" \
  -d "$DATA"
```
### Ejemplo de creacion de registro de mercancia
En este ejemplo se registrara una mercancia nueva, primero se requiere conectar al servidor donde se encuentre corriendo el programa y posteriormente, definir la ruta que se utilizara, depues de esto el programa requiere resibir un usuario para poder crear el registro, para esto el programa valida al usuario (determina si es posible para el usuario crear el registro o no), despues de eso se solicita la informacion de la mercancia y al momento de crear el registro se agrega el identificador reconocido como `KEY`, con esto se habra creado el registro de la mercancia de forma exitosa.


```
URL_HOST=http://localhost:8080 \
ROUTE=/mercancia/register \
METHOD=POST \
HEADER_1='Content-Type: application/json' \
HEADER_2="Authorization: Bearer ${TOKEN}" \
DATA='{"descripcion":"esta es la mercancia", "presentacion":"paquete con 4 unidades"}' \
```


## Archivos Relacionados

- `routes/Store_Admin.py`
- `routes/auth.py`
- `routes/storage`


## Almacenamiento

Todas los registros seran en formato JSON y se almacenaran o en la nube.
>Los datos se almacenan en la nube para poder consultar la informacion desde cualquier lugar
>>>>>>> 60315f50ece3d9f9bc0f8ca547436e11cf3408a4
