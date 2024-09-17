import pyspark
from pyspark.sql.functions import col, lpad, regexp_replace, trim, length, row_number
from pyspark.sql.window import Window

spark = pyspark.sql.SparkSession.builder.appName("banks_trusted").getOrCreate()

source_path = '/home/alves/Projetos/eEDB-011-2024-3/atividade_3/tables/1_Raw/'
source_file = "banks_raw"

df_target_table = spark.read.format("parquet").load(source_path + source_file)

df_target_table = (df_target_table.withColumn("CNPJ", lpad(col("CNPJ"), 14, "0"))
                                  .withColumn("Nome", trim(regexp_replace(col("Nome"), " - PRUDENCIAL", "")))
                                  .withColumnRenamed("Segmento", "SEGMENT")
                                  .withColumnRenamed("Nome", "INSTITUTION_NAME"))

window_clause = Window.partitionBy("CNPJ").orderBy(length(col("INSTITUTION_NAME")))

df_target_table = (df_target_table.withColumn("POSIT", row_number().over(window_clause))
                                  .filter(col("POSIT") == 1)
                                  .drop("POSIT"))

target_path = '/home/alves/Projetos/eEDB-011-2024-3/atividade_3/tables/2_Trusted/'
target_table = "banks_trusted"

df_target_table.write.format("parquet").mode("overwrite").save(target_path + target_table)




