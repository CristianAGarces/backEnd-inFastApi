from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from funciones.usuarios import agregarUsuario, obtenerUsuario, obtenerUsuarioID
from fastapi.responses import JSONResponse
from schemas.user import Usuario
from config.db import dynamodb as db

usuarios_endpoints = APIRouter()

@usuarios_endpoints.get("/usuarios")
def obtenerUsu():
    response = obtenerUsuario(db)
    return JSONResponse(status_code=200,content=jsonable_encoder(response))

@usuarios_endpoints.get("/usuarios/{id}")
def obtenerUsuPorID(id:str):
    response = obtenerUsuarioID(db, id)
    return JSONResponse(status_code=200,content=jsonable_encoder(response))

@usuarios_endpoints.post("/usuarios")
def agregarUsu(user: Usuario):
    response = agregarUsuario(db, user)
    return JSONResponse(status_code=201,content=jsonable_encoder(response))
