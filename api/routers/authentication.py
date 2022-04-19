from fastapi import APIRouter

from viewer.login import Login
from core.bo.usuario import UsuarioBO

router  = APIRouter()

@router.post("/", tags=["authentication"])
async def login(login: Login):
    return UsuarioBO.login(username=login.username, password=login.passoword)