from pydantic import BaseModel

class Publicaciones(BaseModel):
    medicoDePublicacion:str
    titulo:str
    pago:int
