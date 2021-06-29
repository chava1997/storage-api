import peewee as pe
from models.base import EnvModel


class User(EnvModel):
    username = pe.CharField(unique=True)
    password = pe.CharField()
    email = pe.CharField(unique=True)
    phone = pe.CharField(unique=True)
    join_date = pe.DateTimeField()
