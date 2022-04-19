from pydantic import BaseModel

class Login(BaseModel):
    username: str
    #perceba que a palavra é passOword!!!!!
    passoword: str