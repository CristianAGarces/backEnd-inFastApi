import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def agregarMedico(db,medicos):
    table = db.Table('Medicos')
    item={
        "Id medico": medicos.idMedico,
        "nombre":medicos.nombre,
        "edad": medicos.edad,
        "contraseña": medicos.contraseña,
        "correo":medicos.correo,
        "añoNacimiento":medicos.añoNacimiento,
        "numeroTelefono":medicos.numeroTelefono,
        "ciudadResidencia":medicos.ciudadResidencia,
        "direccion":medicos.direccion,
        "rutProfesional":medicos.rutProfesional,
        "experiencia":medicos.experiencia
    }

    try:
        table.put_item(Item=item)
        return({"message":"item agregado correctamente"})
    except (NoCredentialsError, PartialCredentialsError):
        return("Error: No se encontraron las credenciales de AWS.")
    except Exception as e:
        return(f"Error al insertar el ítem: {e}")
    
def obtenerMedico(db):
    table = db.Table('Usuario')
    response = table.scan()
    print(response)
    medicos = response['Items']
    print(medicos)
    return medicos