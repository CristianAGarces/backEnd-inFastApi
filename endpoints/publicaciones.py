from fastapi import APIRouter
from schemas.publicaciones import Publicaciones
from fastapi.encoders import jsonable_encoder
from funciones.publicaciones import agregarPublicaciones
from fastapi.responses import JSONResponse
from config.db import dynamodb as db

publicaciones_endoints = APIRouter()

@publicaciones_endoints.get("/pub")
def obtenerPub():
    response = obtenerPublicaciones(db)
    return JSONResponse(status_code=200,content=jsonable_encoder(response))

@publicaciones_endoints.post("/pub")
def agregarPub(publicaciones : Publicaciones):
    response = agregarPublicaciones(db, publicaciones)
    return JSONResponse(status_code=201,content=jsonable_encoder(response))
