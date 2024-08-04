import boto3

session = boto3.Session(
    aws_access_key_id='AKIA2UC3FU7HYA4MLJWS',
    aws_secret_access_key='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',
    region_name='us-east-2'  # Cambia a tu región
)

# Conectar a DynamoDB
dynamodb = session.resource('dynamodb')
