import sys
sys.path.insert(0, '..')

from fastapi import FastAPI
from routers import authentication


app = FastAPI()
app.include_router(authentication.router)