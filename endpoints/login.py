from fastapi import APIRouter
from fastapi.responses import JSONResponse
from funciones.login import create_token

login_router = APIRouter()


@login_router.post('/login', tags=['auth'])
def login(user: User):
    
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)