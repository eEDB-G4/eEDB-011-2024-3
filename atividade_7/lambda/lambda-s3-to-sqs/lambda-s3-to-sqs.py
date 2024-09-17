import json
import boto3
import os

# Inicializar clientes boto3
sqs = boto3.client('sqs')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    
    queue_url = os.environ['SQS_QUEUE_URL']
    
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        
        try:
            response = s3.get_object(Bucket=bucket_name, Key=object_key)
            file_size = response['ContentLength']
            print(f"Tamanho do arquivo {object_key}: {file_size} bytes")
            
            # Ler o arquivo como bytes
            file_content = response['Body'].read()
            print(f"Conteúdo bruto do arquivo (primeiros 100 bytes): {file_content[:100]}")
            
            # Verificar se o arquivo tem conteúdo
            if file_content:
                # Decodificar conteúdo usando ISO-8859-1 (ANSI) e ignorar erros
                decoded_content = file_content.decode('ISO-8859-1', errors='ignore')
                
                # Enviar o conteúdo decodificado para a fila SQS
                sqs.send_message(
                    QueueUrl=queue_url,
                    MessageBody=decoded_content
                )
                print(f"Arquivo {object_key} enviado para a fila SQS.")
            else:
                print(f"O arquivo {object_key} está vazio ou não pôde ser lido.")
        except Exception as e:
            print(f"Erro ao processar o arquivo {object_key}: {e}")

    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }
