# School API

> Autor: Alejandro Salgado

Deseamos construir un sistema de control de calificaciones de alumnos donde se puedan registar alumnos, materias y docentes, y
se puedan realizar consultas generales a los datos, asi como registrar calificaciones para alumnos en cada curso.

Entonces pensaremos que tenemos las siguientes _entidades_,

 - Alumno (nombre, edad, matricula, estatus)
 - Profe (nombre, edad, titulo, numero_empleado)
 - Materia (clave, nombre, profe, periodo)
 - Calificaciones (periodo, materia_clave, profe_no_emp, matricula, calificación)

Ya que tenemos los datos, necesitamos pensar en los _famosos_ **CRUD** (_Create, Read, Update, Delete_).

Entonces tenemos que tener que exponerle al usuario una manera de realizar estas operaciones, en este caso lo haremos mediante rutas HTTP, con un verbo/método en especifico.

## Operaciones de Almacenamiento de datos 

### Operaciones de Alumno

Registrar un alumno
: solicitamos nombre y fecha de nacimiento
: la matricula sera auto asiganada ya que sera nuestro identificador unico

Actualización de estatus del alumno
: dar de baja a un alumno
: re activar a un alumno

### Operaciones de profes

Registrar un Profe
: solicitamos nombre, edad y titulo
: numero de empleado sera asignado de manera automatica ya que sera nuestro identificador unico

### Operaciones de materias

Registrar una materia
: solcitiamos nombre de la materia, clave, numero de empleado del profesor, y periodo en que sera impartida

### Operaciones de Calificaciones

Registrar a un alumno en el curso
: Solicitamos periodo, materia_clave, profe_no_emp, matricula del alumno.

Registrar calificación para un alumno
: Solicitamos periodo, materia_clave, matricula del alumno, y calificación


> Con esto ya tenemos todas las interacciones correspondientes al almacenamiento de datos.

## Operaciones de consulta de datos

 - Solicitar datos de un alumno
    - básicos
    - con cursos
    - con cursos activos
    - todas las calificaciones 
    - calificaciones por periodo
 - Solicitar datos de un profe
    - básico
    - con historial de materias 
    - con materias activas materias 
 - Solicitar datos de una materia
 - Lista de profes
    - Activos
    - Todos
 - Lista de Alumnos
    - Activos
    - Por Materia
    - Todos
 - Lista de Materias
    - Por Periodo
    - Todos
    - Con datos del profesor
    - Con resumen de alumnos

## Estructuras de solicitud y respuesta

#### Registro de alumno

```
{
    "nombre": "Juanito Johns",
    "fecha_de_nacimiento": "1990-01-01"
}
```

#### Respuesta de registro de alumno exitoso

```
{ "matricula": "XX-XX-XX-00" }
```

#### Mensaje de fallo

```
{
    "code": 500,
    "message": "mensaje de error"
}
```

> Pendiente

## Implementación de rutas para los recursos


`POST /alumno`
: recibe una estructura de registor de alumo
: 201, registrar alumno regresa estructura de matricula para nuevo alumno
: D.O.M, regresa estructura de mensaje de fallo

`GET /alumno/listar`
: 200 regresa una lista de alumnos
: D.O.M, regresa mensaje de fallo en formato `json`

`GET /alumno/<matricula>`
: 200, datos de alumno con matricula 
: D.O.M, regresa mensaje de fallo en formato `json`

`POST /docente`
: 201, regitrar un profe, y regresar numero de emplado
: D.O.M, regresa mensaje de fallo

`GET /docente/list`
: 200, lista de profes en formato json
: D.O.M, regresa mensaje de fallo

`GET /docente/<no_emp>`
: 200, datos de un profe por numero de empleado
: D.O.M, regresa mensaje de fallo

`POST /materia`
: 201, registrar una materia y regresa confirmacion de registro
: D.O.M, regresa mensaje de fallo

`POST /materia/<periodo>/<clave>/<matricula>/registrar`
: 201, Registrar alumno a una materia
: D.O.M, regresa mensaje de fallo

`POST /materia/<periodo>/<clave>/<matricula>/calificar`
: 201, asignar una calificacion a un alumno
: D.O.M, regresa mensaje de fallo

