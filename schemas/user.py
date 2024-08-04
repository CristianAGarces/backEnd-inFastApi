from pydantic import BaseModel

class Usuario(BaseModel):
    idUsuario:str
    nombre: str
    edad: int
    contraseña: str
    correo: str
    peso: int
    añoNacimiento: int
    numeroContactos:str
    ciudadResidencia:str
    direccion:str
