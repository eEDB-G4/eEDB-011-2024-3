import json
import io
import psycopg2
import boto3
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import os

# Inicializar o cliente S3
s3 = boto3.client('s3')

# Configurações do banco de dados
DB_HOST = 'my-postgresql-db'
DB_PORT = '5432'
DB_NAME = 'mydatabase'
DB_USER = 'postgres'
DB_PASSWORD = 'mysecretpassword'

# Configurações do bucket S3
S3_BUCKET_NAME = 'eedb-011-enriched-data-bucket'
S3_KEY = 'enriched_data.parquet'

# Função para conectar ao banco de dados PostgreSQL
def connect_to_db():
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    
    enriched_data = []
    
    # Conectar ao banco de dados
    conn = connect_to_db()
    cursor = conn.cursor()

    # Processar cada mensagem na fila
    for record in event['Records']:
        # Mensagem recebida
        message_body = record['body']
        
        # Usar StringIO para tratar a mensagem como um arquivo CSV
        csv_file = io.StringIO(message_body)
        csv_reader = csv.reader(csv_file, delimiter=';')

        # Iterar sobre cada linha do CSV e inserir na tabela tb_complaints
        for row in csv_reader:
            # Inserir dados na tabela tb_complaints
            cursor.execute("""
                INSERT INTO tb_complaints (
                ano,
                trimestre,
                categoria,
                tipo,
                cnpj_if,
                instituicao_financeira,
                indice,
                quantidade_de_reclamacoes_reguladas_procedentes,
                quantidade_de_reclamacoes_reguladas_-_outras,
                quantidade_de_reclamacoes_nao_reguladas,
                quantidade_total_de_reclamacoes,
                quantidade_total_de_clientes_ccs_e_scr,
                quantidade_de_clientes_ccs,
                quantidade_de_clientes_scr
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            );
            """, (row[0], row[1]))
    
    conn.commit()

    # Realizar JOIN e carregar dados na tabela tb_spec_final
    query = """
        INSERT INTO spec_final (complaint_id, complaint_description, employee_name, bank_name)
        SELECT c.complaint_id, c.complaint_description, e.employee_name, b.bank_name
        FROM tb_complaints c
        JOIN tb_employees e ON c.employee_id = e.employee_id
        JOIN tb_banks b ON e.bank_id = b.bank_id
    """
    cursor.execute(query)
    conn.commit()
    
    # Ler os dados da tabela tb_spec_final para DataFrame
    df_query = "SELECT * FROM tb_spec_final"
    df = pd.read_sql(df_query, conn)

    # Converter DataFrame para Parquet
    table = pa.Table.from_pandas(df)
    buffer = io.BytesIO()
    pq.write_table(table, buffer)
    buffer.seek(0)
    
    # Salvar o Parquet no S3
    s3.put_object(
        Bucket=S3_BUCKET_NAME,
        Key=S3_KEY,
        Body=buffer.getvalue(),
        ContentType='application/x-parquet'
    )

    # Fechar a conexão com o banco de dados
    cursor.close()
    conn.close()

    return {
        'statusCode': 200,
        'body': json.dumps('Processed and enriched data successfully')
    }
