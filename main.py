from fastapi import FastAPI
from endpoints.usuarios import usuarios_endpoints
from endpoints.publicaciones import publicaciones_endoints
from endpoints.medicos import medicos_endpoints

app = FastAPI()

app.include_router(usuarios_endpoints)
app.include_router(publicaciones_endoints)
app.include_router(medicos_endpoints)

@app.get("/")
def inicio():
    return {"Message":"Hola mundo"}


