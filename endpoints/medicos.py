from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from funciones.medicos import agregarMedico, obtenerMedico
from fastapi.responses import JSONResponse
from schemas.medicos import Medicos
from config.db import dynamodb as db

medicos_endpoints = APIRouter()

@medicos_endpoints.get("/medicos")
def obtenerMed():
    response = obtenerMedico(db)
    return JSONResponse(status_code=200,content=jsonable_encoder(response))

@medicos_endpoints.post("/usuarios")
def agregarMed(medicos: Medicos):
    response = agregarMedico(db, medicos)
    return JSONResponse(status_code=201,content=jsonable_encoder(response))
