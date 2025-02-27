from fastapi import APIRouter, Response
from config.db import conn
from models.user import users
from schemas.user import User
from starlette.status import HTTP_204_NO_CONTENT

from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

user = APIRouter()

@user.get('/users')
def get_users():
    return conn.execute(users.select()).fetchall()


@user.post('/users')
def create_user(user: User):
    new_user = {"name": user.name,
                "email": user.email
                }
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    result = conn.execute(users.insert().values(new_user))
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()


@user.get('/users/{id}')
def get_user(id: str):
    return conn.execute(users.select().where(users.c.id == id)).first()
   

@user.delete('/users/{id}')
def delete_user(id: str):
    conn.execute(users.delete().where(users.c.id == id)).first()
    return Response(status_code=HTTP_204_NO_CONTENT)


@user.put('/users/{id}')
def update_user(id: str, user: User):
    conn.execute(users.update(
        ).values(name = user.name,
                email = user.email,
                password = f.encrypt(user.password.encode("utf-8"))
        ).where(users.c.id == id))
    return "Updated"