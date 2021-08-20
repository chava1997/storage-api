
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


## Casos de uso

### Registrar una mercancia
- Metodo `Post`
- Objetivo: registrar una nueva mercancia
- Se requiere ingresar los siguientes valores:
  - `descripcion`
  - `presentacion`
  - `clave`
- Si no se ingresa una descripcion la mercancia no se podra registrar

Esta funcion crea un nuevo archivo json en una ruta predefinida con los valores de la nueva mercancia dados por el usuario.

`curl localhost:8080/storage_admin/mercancia/register -X POST -H "Content-Type: application/json" -d '{"descripcion": "ejemplo","presentacion":"ejemplo","clave": "ejem1"}'`

### Consultar las mercancias
- Metodo `GET`
- Objetivo: Consultar todas las mercacias
- Solo se requiere hacer una consulta a la ruta, no se requiere espesificar ningun parametro

En esta funcion se regresa una lista con los json que conforman todas las mercancias disponibles.

`curl http://localhost:8080/storage_admin/mercancia/query -X GET`

### Consultar una mercancia por clave
- Metodo `GET`
- Objetivo: consultar una emrcancia espesifica por su clave
- Se requiere la clave de la mercancia, este dato debe de ser exacto, en caso de ingresar una clave no valida, regresara un error

Esta funcion regresa una mercancia espesifica en funcion de la clave

`curl http://localhost:8080/storage_admin/mercancia/query/ejem1 -X GET`

### Consultar una mercancia por descripcion
- Metodo `GET`
- Objetivo: consultar una emrcancia espesifica por su descripcion
- Se requiere la descripcion de la mercancia, este dato debe de ser exacto, en caso de ingresar una descripcion no valida, regresara un error

Esta funcion regresa una mercancia espesifica en funcion de la descripcion

`curl http://localhost:8080/storage_admin/mercancia/query/ejemplo -X GET`

### Registrar una entrada
- Metodo `Post`
- Objetivo: registrar una nueva entrada
- Se requiere ingresar los siguientes valores:
  - `id_e`
  - `fecha_e`
  - `cantidad_e`

Esta funcion crea un nuevo archivo json en una ruta predefinida con los valores de la nueva entrada dados por el usuario.

`curl localhost:8080/storage_admin/entradas/register -X POST -H "Content-Type: application/json" -d '{"id_e": "001","fecha_e": "2021-12-12", "cantidad_e": "10"}'`

### Consultar entradas
- Metodo `GET`
- Objetivo: Consultar todas las entradas
- Solo se requiere hacer una consulta a la ruta, no se requiere espesificar ningun parametro

En esta funcion se regresa una lista con los json que conforman todas las entradas disponibles.

`curl http://localhost:8080/storage_admin/entradas/query -X GET`

### Consultar una entrada por ID
- Metodo `GET`
- Objetivo: consultar una entrada espesifica por su ID
- Se requiere el ID de la entrada, este dato debe de ser exacto, en caso de ingresar un ID no valida, regresara un error

Esta funcion regresa una entrada espesifica en funcion del ID.

`curl http://localhost:8080/storage_admin/entradas/query/001 -X GET`

### Consultar entradas por fecha
- Metodo `GET`
- Objetivo: consultar todas las entradas con una fecha espesifica
- Se requiere la fecha de las entradas

Esta funcion regresa todas las entradas que se hayan registrado en una fecha espesifica.

`curl http://localhost:8080/storage_admin/entradas/query/2021-12-12 -X GET`

#### Consultar entradas por cantidad
- Metodo `GET`
- Objetivo: consultar todas las entradas con una cantidad espesifica
- Se requiere la cantidad de las entradas

Esta funcion regresa todas las entradas que se hayan registrado con una cantidad espesifica.

`curl http://localhost:8080/storage_admin/entradas/query/10 -X GET`

### Registrar una salida
- Metodo `Post`
- Objetivo: registrar una nueva salida
- Se requiere ingresar los siguientes valores:
  - `id_s`
  - `fecha_s`
  - `cantidad_s`

  Esta funcion crea un nuevo archivo json en una ruta predefinida con los valores de la nueva salida dados por el usuario.

`curl localhost:8080/storage_admin/salidas/register -X POST -H "Content-Type: application/json" -d '{"id_s": "001","fecha_s": "2021-12-12", "cantidad_s": "10"}'`

### Consultar entradas
- Metodo `GET`
- Objetivo: Consultar todas las salidas
- Solo se requiere hacer una consulta a la ruta, no se requiere espesificar ningun parametro

En esta funcion se regresa una lista con los json que conforman todas las salidas disponibles.

`curl http://localhost:8080/storage_admin/salidas/query -X GET`

### Consultar una salida por ID
- Metodo `GET`
- Objetivo: consultar una salida espesifica por su ID
- Se requiere el ID de la salida, este dato debe de ser exacto, en caso de ingresar un ID no valida, regresara un error

Esta funcion regresa una salida espesifica en funcion del ID.

`curl http://localhost:8080/storage_admin/salidas/query/001 -X GET`

### Consultar salidas por fecha
- Metodo `GET`
- Objetivo: consultar todas las salidas con una fecha espesifica
- Se requiere la fecha de las salidas

Esta funcion regresa todas las salidas que se hayan registrado en una fecha espesifica.

`curl http://localhost:8080/storage_admin/salidas/query/2021-12-12 -X GET`

#### Consultar salidas por cantidad
- Metodo `GET`
- Objetivo: consultar todas las salidas con una cantidad espesifica
- Se requiere la cantidad de las salidas

Esta funcion regresa todas las salidas que se hayan registrado con una cantidad espesifica.

`curl http://localhost:8080/storage_admin/salidas/query/10 -X GET`




## Planeacion del desarrollo del frontend


### Index
En `Storage-admin-0000-Index` se muestra la pagina principal de la interfaz web.
- Mercancia: Se conforma por el boton `Registrar` y el boton `consultar`
  - Boton registrar: redireccionara a la pagina de registro de nueva mercancia
  - Boton consultar: redireccionara a la pagina de consultas de mercancia, en esta podras buscar mercancias por `clave`, `descripcion` y `presentacion`

- Entrada: Se conforma por el boton `Registrar` y el boton `consultar`
  - Boton registrar: redireccionara a la pagina de registro de nueva entrada
  - Boton consultar: redireccionara a la pagina de consultas de entradas, en esta podras buscar entrada por `clave`, `descripcion` y `presentacion`

- Salida: Se conforma por el boton `Registrar` y el boton `consultar`
  - Boton registrar: redireccionara a la pagina de registro de nueva salida
  - Boton consultar: redireccionara a la pagina de consultas de salidas, en esta podras buscar salidas por `clave`, `descripcion` y `presentacion`

<img src="https://github.com/chava1997/storage-api/blob/master/images/Storage-admin-0000-Index.png" width="550">  


### Registro de mercancia
En `Storage-admin-0006-Registro de mercancia` se solicitan los datos para la creacion de una nueva mercancia.
- Registrar mercancia: Se conforma por las cajas de texto `clave`, `descripcion` y `presentacion` y por los botones regresar y registrar.
  - Caja de texto `clave`: se solicita la `clave` de la nueva mercancia
  - Caja de texto `descripcion`: se solicita la `descripcion` de la nueva mercancia
  - Caja de texto `presentacion`: se solicita la `presentacion` de la nueva mercancia
  - Boton regresar: reidreccionara a la pagina Index
  - Boton registrar: en caso de ue la informacion sea correcta mostrara una caja de texto diciendo que la mercancia se registro correctamente de lo contrario mostrara un mensaje de error

<img src="https://github.com/chava1997/storage-api/blob/master/images/Storage-admin-0006-Registro%20de%20mercancia.png" width="550">  


### Registro de entrada
En `Storage-admin-0004-Registro de entrada` se solicitan los datos para la creacion de una nueva entrada.
- Registrar entrada: Se conforma por las cajas de texto `ID`, `cantidad` y `fecha` y por los botones regresar y registrar.
  - Caja de texto `ID`: se solicita el `ID` de la nueva entrada
  - Caja de texto `cantidad`: se solicita la `cantidad` de la nueva entrada
  - Caja de texto `fecha`: se solicita la `fecha` de la nueva entrada
  - Boton regresar: reidreccionara a la pagina Index
  - Boton registrar: en caso de ue la informacion sea correcta mostrara una caja de texto diciendo que la entrada se registro correctamente de lo contrario mostrara un mensaje de error

<img src="https://github.com/chava1997/storage-api/blob/master/images/Storage-admin-0004-Registro%20de%20entrada.png" width="550">


### Registro de salida
En `Storage-admin-0005-Registro de salida` se solicitan los datos para la creacion de una nueva salida.
- Registrar salida: Se conforma por las cajas de texto `ID`, `cantidad` y `fecha` y por los botones regresar y registrar.
  - Caja de texto `ID`: se solicita el `ID` de la nueva salida
  - Caja de texto `cantidad`: se solicita la `cantidad` de la nueva salida
  - Caja de texto `fecha`: se solicita la `fecha` de la nueva salida
  - Boton regresar: reidreccionara a la pagina Index
  - Boton registrar: en caso de ue la informacion sea correcta mostrara una caja de texto diciendo que la salida se registro correctamente de lo contrario mostrara un mensaje de error

<img src="https://github.com/chava1997/storage-api/blob/master/images/Storage-admin-0005-Registro%20de%20salida.png" width="550">


### Consulta de mercancias
En `Storage-admin-0003-Consultar mercancias` se mustran todas las mercancias registradas y se dan las opciones de buscar datos por `clave`, `descripcion` y por `presentacion`.
- Consultar mercancia: Se conforma por las cajas de texto `clave`, `descripcion` y `presentacion` y por los botones regresar y buscar(se tiene un boton 'buscar' por cada caja de texto).
- Caja de texto `clave`: se solicita la `clave` de la mercancia
  - Boton buscar: Redireccionara a una pagina de consulta con los datos filtrados segun la `calve` que se ingrese en la caja de texto
- Caja de texto `descripcion`: se solicita la `descripcion` de la mercancia
  - Boton buscar: Redireccionara a una pagina de consulta con los datos filtrados segun la `descripcion` que se ingrese en la caja de texto
- Caja de texto `presentacion`: se solicita la `presentacion` de la mercancia
  - Boton buscar: Redireccionara a una pagina de consulta con los datos filtrados segun la `presentacion` que se ingrese en la caja de texto
- Boton regresar: reidreccionara a la pagina Index

<img src="https://github.com/chava1997/storage-api/blob/master/images/Storage-admin-0003-Consultar%20mercancias.png" width="550">


### Consulta de entradas
En `Storage-admin-0001-Consultar entradas` se mustran todas las entradas registradas y se dan las opciones de buscar datos por `ID`, `cantidad` y por `fecha`.
- Registrar entrada: Se conforma por las cajas de texto `ID`, `cantidad` y `fecha` y por los botones regresar y registrar.
- Caja de texto `ID`: se solicita la `ID` de la entrada
  - Boton buscar: Redireccionara a una pagina de consulta con los datos filtrados segun el `ID` que se ingrese en la caja de texto
- Caja de texto `cantidad`: se solicita la `cantidad` de la entrada
  - Boton buscar: Redireccionara a una pagina de consulta con los datos filtrados segun la `cantidad` que se ingrese en la caja de texto
- Caja de texto `fecha`: se solicita la `fecha` de la entrada
  - Boton buscar: Redireccionara a una pagina de consulta con los datos filtrados segun la `fecha` que se ingrese en la caja de texto
- Boton regresar: reidreccionara a la pagina Index

<img src="https://github.com/chava1997/storage-api/blob/master/images/Storage-admin-0001-Consultar%20entradas.png" width="550">


### Consulta de salidas
En `Storage-admin-0002-Consultar Salidas` se mustran todas las salidas registradas y se dan las opciones de buscar datos por `ID`, `cantidad` y por `fecha`.
- Registrar salida: se conforma por las cajas de texto `ID`, `cantidad` y `fecha` y por los botones regresar y registrar.
- Caja de texto `ID`: se solicita la `ID` de la salida
  - Boton buscar: Redireccionara a una pagina de consulta con los datos filtrados segun el `ID` que se ingrese en la caja de texto
- Caja de texto `cantidad`: se solicita la `cantidad` de la salida
  - Boton buscar: Redireccionara a una pagina de consulta con los datos filtrados segun la `cantidad` que se ingrese en la caja de texto
- Caja de texto `fecha`: se solicita la `fecha` de la salida
  - Boton buscar: Redireccionara a una pagina de consulta con los datos filtrados segun la `fecha` que se ingrese en la caja de texto
- Boton regresar: reidreccionara a la pagina Index

<img src="https://github.com/chava1997/storage-api/blob/master/images/Storage-admin-0002-Consultar%20Salidas.png" width="550">



## Futuros cambios al backend

### Log In
EN `Storage-admin-0007-login` se solicitan el `usuario` y la `crontraseña` de acceso para la utenticacion del usuario y posteriormente dejarlo entrar si los datos ingresados son validos, dependiendo de las credenciales que se le asignen al usuario podra tener permisos de registrar, exportar y consultar o solo de consultar y exportar o solo de consultar.
- Caja de texto `usuario`: se solicita el nombre del usuario
- Caja de texto `Contraseña`: se solicita la `contraseña` del usuario
- Boton continuar: si los datos son validos, el sistema redireccionara a la pagina "index", de lo contrario mostrara un mensaje de error.
- Boton registrar: redireccionara a la pagina "registrar usuario".

<img src="https://github.com/chava1997/storage-api/blob/master/images/Storage-admin-0007-login.png" width="550">


### Registro de Usuario
En `Storage-admin-0008-registrar usuario` se solicitaran el `usuario` y la `contraseña` a registrar asi como los permisos que se le asignaran al usuario, los cuales estan delimitados a las opciones "Consultar, exportar y registrar", "Consultar y exportar" y "Consultar".
- Caja de texto `usuario`: se solicita el nombre de usuario que se desea dar de alta
- Caja de texto `contraseña`: se solicita la contraseña que se desea asignar al usuairio, la cual se debera de ingresar cada vez que desee tener acceso al sistema.
- Caja de texto `confirmr contraseña`: se solicita repetir exactamente la misma contraseña que se ingreso en la caja de texto `contraseña`.
Combo box `permisos`: se solicita el nivel de permisos que se le asignara al nuevo usuario, dichos permisos estan delimitados a las siguientes opciones:
  - Consultar, exportar y registrar: esta opcion le concede los permisos de consultar cualquier dato que se desee de la base de datos del programa, asi como exportarlo en formato excel o txt, ademas de permitirle al usuario hacer nuevos registros de mercancia, entradas y salidas
  - Consultar y exportar: esta opcion le concede los permisos de consultar cualquier dato que se desee de la base de datos del programa, asi como exportarlo en formato excel o txt
  - Consultar: esta opcion solo concede el permisos de consultar cualquier dato que se desee de la base de datos del programa
- Boton regresar: redireccionra a la pagina "log in"
- Boton continuar: en caso de que los datos ingresados sean validos se mostrara un mensaje diciendo "Registro de usuario exitoso", de lo contrario se mostrara un mensaje diciendo "Datos invalidos"

<img src="https://github.com/chava1997/storage-api/blob/master/images/Storage-admin-0008-registrar%20usuario.png" width="550">


### Subir imagen a registros de entrada y salida
En `Storage-admin-0009-registrar entrada` y `Storage-admin-0010-registrar salida` se añadio el boton "subir foto", el cual permitira subir una foto como evidencia del estado de la mercancia tanto al momento de su entrada como en el momento de su salida.
- Boton subir foto: solicita un archivo de imagen

<img src="https://github.com/chava1997/storage-api/blob/master/images/Storage-admin-0009-registrar%20entrada.png" width="550">
<img src="https://github.com/chava1997/storage-api/blob/master/images/Storage-admin-0010-registrar%20salida.png" width="550">

### Exportar registros en paginas de consultas de entrada y salida
En `Storage-admin-0011-consultar entradas` y `Storage-admin-0012-consultar salida` se añadio el boton `exportar` asi como unos cuadros de seleccion al lado izquierdo de los registros para seleccionar los registros que se desean exportar, dichos registros se podran exportar en formato excel y txt

<img src="https://github.com/chava1997/storage-api/blob/master/images/Storage-admin-0011-consultar%20entradas.png" width="550">
<img src="https://github.com/chava1997/storage-api/blob/master/images/Storage-admin-0012-consultar%20salida.png" width="550">
