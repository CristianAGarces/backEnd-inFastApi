from pydantic import BaseModel
from schemas.certificados import Certificados

class Medicos(BaseModel):
    idMedico:str
    nombre:str
    edad:int
    contraseña:str
    correo:str
    numeroTelefono:str
    añoNacimiento:str
    numeroTelefono:str
    ciudadResidencia:str
    direccion:str
    rutProfesional:str
    experiencia:str
    certificados: list[Certificados]
    