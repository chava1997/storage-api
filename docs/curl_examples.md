# Server interaction examples using curl

If you want to check the `CORS` response, you should populate the environment variable named `CORS_DOMAINS` with a value, let's say `http://localhost:1234`, then any request with that value in it's `ORIGIN` _HTTP Header_ should pass the `CORS` check politics in your browser.

You can go ahead and check the differences between a `cors` and `no-cors` request by executing the following command.

```

# This is a cors valid request
curl -vq http://localhost:8080/storage/json \
    -X OPTIONS \
    -H 'ORIGIN: http://localhost:1234' \
    2>&1 | grep '^<'

# This is a cors in valid request
curl -vq http://localhost:8080/storage/json \
    -X OPTIONS \
    -H 'ORIGIN: http://example.com' \
    2>&1 | grep '^<'
```


If you want to store a json file using, you should send a request as

```
POST /storage/json
ORIGIN: http://localhost:1234
Content-Type: application/json

{
 "json": "data"
}
```

The curl command should be 

```
curl -vq http://localhost:8080/storage/json \
    -X POST \
    -H 'ORIGIN: http://localhost:1234' \
    -H 'Content-Type: application/json' \
    --data '{ "json": "data" }'
```

If you `json` data is stored in a file (let's say `foo.json`) you can run


```
curl -vq http://localhost:8080/storage/json \
    -X POST \
    -H 'ORIGIN: http://localhost:1234' \
    -H 'Content-Type: application/json' \
    --data @./foo.json
```

## Performing Authentication

This project includes basic `jwt` authentication, first you need a registered user,
the registration endpoint is `/auth/signup`, and it receives a `json` with keys
`username`, `email`, `password`, `password_confirmation`, and `phone`.

> Currently there is no actual validation for `phone` or `email`.

One can create a user with a `POST /auth/signup`, such as 


```

curl -qv http://localhost:8080/auth/signup \
    -H 'Content-Type: application/json' \
    -d '{"username": "baz", "email": "baz@baz.com", "password": "baz", "password_confirmation": "baz", "phone":"0911"}'

curl -qv http://localhost:8080/auth/login\
    -H 'Content-Type: application/json' \
    -d '{"username": "baz", "email": "baz@baz.com", "password": "baz"}'

```
