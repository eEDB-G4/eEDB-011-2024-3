import pyspark

spark = pyspark.sql.SparkSession.builder.appName("complaints_raw").getOrCreate()

source_path = '/home/alves/Projetos/eEDB-011-2024-3/atividade_3/source_files/Reclamacoes'

df_target_table = (spark.read.format("csv").option("header", "true")
                                           .option("sep", ";")
                                           .option("encoding", "cp1252")
                                           .load(source_path))

df_target_table = (df_target_table.withColumnRenamed("CNPJ IF", "CNPJ_IF")
                                  .withColumnRenamed("Instituição financeira", "Instituicao_financeira")
                                  .withColumnRenamed("Índice", "Indice")
                                  .withColumnRenamed("Quantidade de reclamações reguladas procedentes", "Quantidade_de_reclamacoes_reguladas_procedentes")
                                  .withColumnRenamed("Quantidade de reclamações reguladas - outras", "Quantidade_de_reclamacoes_reguladas_outras")
                                  .withColumnRenamed("Quantidade de reclamações não reguladas", "Quantidade_de_reclamacoes_nao_reguladas")
                                  .withColumnRenamed("Quantidade total de reclamações", "Quantidade_total_de_reclamacoes")
                                  .withColumnRenamed("Quantidade total de clientes – CCS e SCR", "Quantidade_total_de_clientes_CCS_e_SCR")
                                  .withColumnRenamed("Quantidade de clientes – CCS", "Quantidade_de_clientes_CCS")
                                  .withColumnRenamed("Quantidade de clientes – SCR", "Quantidade_de_clientes_SCR"))

target_path = '/home/alves/Projetos/eEDB-011-2024-3/atividade_3/tables/1_Raw/'
target_table = "complaints_raw"

df_target_table.write.format("parquet").mode("overwrite").save(target_path + target_table)




