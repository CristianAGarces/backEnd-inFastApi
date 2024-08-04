import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def agregarPublicaciones(db,publicaciones):
    table = db.Table('Publicaciones')
    item={
        "medicoDePublicacion":publicaciones.medicoDePublicaciones,
        "titulo":publicaciones.str,
        "pago":publicaciones.int,
    }

    try:
        table.put_item(Item=item)
        return({"message":"item agregado correctamente"})
    except (NoCredentialsError, PartialCredentialsError):
        return("Error: No se encontraron las credenciales de AWS.")
    except Exception as e:
        return(f"Error al insertar el ítem: {e}")