import pyspark

# Criação da sessão Spark
spark = pyspark.sql.SparkSession.builder.appName("delivery_validation").getOrCreate()

# Caminhos de origem dos arquivos Parquet
source_path = '/home/alves/Projetos/eEDB-011-2024-3/atividade_3/tables/2_Trusted/'
source_file_complaints = "complaints_trusted"
source_file_reviews = "employees_trusted"

# Leitura dos arquivos Parquet
df_complaints = spark.read.format("parquet").load(source_path + source_file_complaints)
df_reviews = spark.read.format("parquet").load(source_path + source_file_reviews)

# Processamento dos dados
df_target_table = (df_complaints.join(df_reviews, df_complaints.INSTITUTION_NAME == df_reviews.INSTITUTION_NAME, "inner")
                   .select(df_complaints.YEAR,
                           df_complaints.QUARTER,
                           df_complaints.INSTITUTION_CATEGORY,
                           df_complaints.INSTITUTION_TYPE,
                           df_complaints.CNPJ,
                           df_complaints.INSTITUTION_NAME,
                           df_complaints.QTY_JUSTIFIED_REGULATED_COMPLAINTS,
                           df_complaints.QTY_OTHER_REGULATED_COMPLAINTS,
                           df_complaints.QTY_NOT_REGULATED_COMPLAINTS,
                           df_complaints.QTY_COMPLAINTS,
                           df_reviews.REVIEWS_COUNT,
                           df_reviews.OVERALL_RATING))

# Caminho de destino para salvar o Parquet
target_path = '/home/alves/Projetos/eEDB-011-2024-3/atividade_3/tables/3_Delivery/'
target_table = "reviews_complaints_delivery"

# Salvando o DataFrame em Parquet
df_target_table.write.format("parquet").mode("overwrite").save(target_path + target_table)
