# Autentication Module

Esto se trata de X cosa...

## Modo de uso

Se exponen rutas para la autenticacion en el servidor de datos, las rutas son

 - `/auth/login`
 - `/auth/signup`

Estas rutas se asisten del modulo `modules/auth.py` y de `models/auth.py`.

Un usuario puede solicitar reigstrarse al sistema mediante la ruta de signup, se requiere
un json con los datos `email`, `phone`, `username`, `password` y `password_confirmation`, si 
todo sale bien el usuario debe esperar una respuesta HTTP 201.

Un usuario puede solicitar un token de acceso al sistema mediante la ruta de login, se
un json con `username` y `password`, si todo sale bien, recibira un json en respuesta con
una llave nombrada `token` y una respuesta HTTP 201, dicha llave se utilizara como cabezar HTTP o consulta HTTP,
en las peticiones que deban ser autorizadas con dicho token.

Un usuario puede subscribirse a roles, utilizando la ruta `/auth/role/add`... por ejemplo...

