from ..dto.login import Login
from ..dao.usuario import UsuarioDAO

class UsuarioBO:
    
    @staticmethod
    def login(username: str, password: str):
        login_data: Login = Login(username, password)
        print(login_data.username)
        print(login_data.password)
        value = UsuarioDAO.teste()
        print(value)
        return value
