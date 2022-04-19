import sys
sys.path.insert(0, '..')

from typing import Optional
from fastapi import FastAPI

from .viewer.login import Login

from core.bo.usuario import UsuarioBO

app = FastAPI()

@app.post("/")
def read_root(login: Login):
    return UsuarioBO.login(username=login.username, password=login.passoword)