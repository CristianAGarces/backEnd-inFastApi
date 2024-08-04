import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def agregarUsuario(db,user):
    table = db.Table('Usuarios')
    item={
        "usuario_id": user.idUsuario,
        "nombre":user.nombre,
        "edad": user.edad,
        "contraseña": user.contraseña,
        "correo": user.correo,
        "peso": user.peso,
        "añoNacimiento": user.añoNacimiento,
        "numeroContactos": user.numeroContactos,
        "ciudadResidencia": user.ciudadResidencia,
        "direccion": user.direccion
    }

    try:
        table.put_item(Item=item)
        return({"message":"item agregado correctamente"})
    except (NoCredentialsError, PartialCredentialsError):
        return("Error: No se encontraron las credenciales de AWS.")
    except Exception as e:
        return(f"Error al insertar el ítem: {e}")

def obtenerUsuario(db):
    table = db.Table('Usuario')
    response = table.scan()
    print(response)
    usuarios = response['Items']
    print(usuarios)
    return usuarios

def obtenerUsuarioID(db, id):
    table = db.Table('Usuarios')
    response = table.get_item(Key={ 'usuario_id': id  })
    print(response)
    return response["Item"]


