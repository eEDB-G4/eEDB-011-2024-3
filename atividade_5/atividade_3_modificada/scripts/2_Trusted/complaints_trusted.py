import pyspark
from pyspark.sql.functions import when, col, lpad, regexp_replace, trim, length, left, lit

spark = pyspark.sql.SparkSession.builder.appName("complaints_trusted").getOrCreate()

source_path = '/home/alves/Projetos/eEDB-011-2024-3/atividade_3/tables/1_Raw/'
source_file = "complaints_raw"

df_target_table = spark.read.format("parquet").load(source_path + source_file)

df_target_table = (df_target_table.withColumn("CNPJ_IF", when(length(trim(col("CNPJ_IF"))) == 0, "")
                                                        .when(col("CNPJ_IF").isNull(), "")
                                                        .otherwise(lpad(col("CNPJ_IF"), 14, "0")))
                                  .withColumn("Ano", col("Ano").cast("int"))
                                  .withColumn("Trimestre", left(col("Trimestre"), lit(1)).cast("int"))
                                  .withColumn("Instituicao_financeira", trim(regexp_replace(col("Instituicao_financeira"), "\(conglomerado\)", "")))
                                  .withColumn("Quantidade_de_reclamacoes_reguladas_procedentes", col("Quantidade_de_reclamacoes_reguladas_procedentes").cast("bigint"))
                                  .withColumn("Quantidade_de_reclamacoes_reguladas_outras", col("Quantidade_de_reclamacoes_reguladas_outras").cast("bigint"))
                                  .withColumn("Quantidade_de_reclamacoes_nao_reguladas", col("Quantidade_de_reclamacoes_nao_reguladas").cast("bigint"))
                                  .withColumn("Quantidade_total_de_reclamacoes", col("Quantidade_total_de_reclamacoes").cast("bigint")))

df_target_table = (df_target_table.withColumnRenamed("Ano", "YEAR")
                                  .withColumnRenamed("Trimestre", "QUARTER")
                                  .withColumnRenamed("Categoria", "INSTITUTION_CATEGORY")
                                  .withColumnRenamed("Tipo", "INSTITUTION_TYPE")
                                  .withColumnRenamed("CNPJ_IF", "CNPJ")
                                  .withColumnRenamed("Instituicao_financeira", "INSTITUTION_NAME")
                                  .withColumnRenamed("Quantidade_de_reclamacoes_reguladas_procedentes", "QTY_JUSTIFIED_REGULATED_COMPLAINTS")
                                  .withColumnRenamed("Quantidade_de_reclamacoes_reguladas_outras", "QTY_OTHER_REGULATED_COMPLAINTS")
                                  .withColumnRenamed("Quantidade_de_reclamacoes_nao_reguladas", "QTY_NOT_REGULATED_COMPLAINTS")
                                  .withColumnRenamed("Quantidade_total_de_reclamacoes", "QTY_COMPLAINTS"))

df_target_table = df_target_table.drop("Indice", "Quantidade_total_de_clientes_CCS_e_SCR", "Quantidade_de_clientes_CCS", "Quantidade_de_clientes_SCR", "_c14")

target_path = '/home/alves/Projetos/eEDB-011-2024-3/atividade_3/tables/2_Trusted/'
target_table = "complaints_trusted"

df_target_table.write.format("parquet").mode("overwrite").save(target_path + target_table)




