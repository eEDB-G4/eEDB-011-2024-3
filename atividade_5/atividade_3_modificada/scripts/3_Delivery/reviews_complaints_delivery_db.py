import pyspark

# Caminho do conector MySQL
jdbc_path = '/home/alves/Projetos/eEDB-011-2024-3/atividade_3/libs/mysql-connector-j-9.0.0.jar'

# Criação da sessão Spark
spark = pyspark.sql.SparkSession.builder.appName("reviews_complaints_delivery") \
    .config("spark.jars", jdbc_path) \
    .getOrCreate()

# Caminhos de origem dos arquivos Parquet
source_path = '/home/alves/Projetos/eEDB-011-2024-3/atividade_3/tables/3_Delivery/'
table_name = 'reviews_complaints_delivery'

# Leitura dos arquivos Parquet
df_reviews_complaints_delivery = spark.read.format("parquet").load(source_path + table_name)

# Configurações para salvar no banco de dados MySQL
mysql_url = "jdbc:mysql://localhost:3306/mydb"

mysql_properties = {
    "user": "alves",
    "password": "",
    "driver": "com.mysql.cj.jdbc.Driver"
}

# Escrevendo no MySQL
df_reviews_complaints_delivery.write.jdbc(url=mysql_url, table=table_name, mode="overwrite", properties=mysql_properties)
