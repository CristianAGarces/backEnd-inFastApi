from pydantic import BaseModel

class Certificados(BaseModel):
    titulo:str
    archivo: str
