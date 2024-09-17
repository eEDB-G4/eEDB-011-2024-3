import pyspark

spark = pyspark.sql.SparkSession.builder.appName("banks_raw").getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

source_path = '/home/alves/Projetos/eEDB-011-2024-3/atividade_3/source_files/Bancos/'
source_file = 'EnquadramentoInicia_v2.tsv'

df_target_table = (spark.read.format("csv").option("header", "true")
                                           .option("sep", "\t")
                                           .option("encoding", "ISO-8859-1")
                                           .load(source_path))

target_path = '/home/alves/Projetos/eEDB-011-2024-3/atividade_3/tables/1_Raw/'
target_table = 'banks_raw'

df_target_table.write.format("parquet").mode("overwrite").save(target_path + target_table)
