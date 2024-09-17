import pyspark

spark = pyspark.sql.SparkSession.builder.appName("employees_raw").getOrCreate()

source_path = '/home/alves/Projetos/eEDB-011-2024-3/atividade_3/source_files/Empregados/'
source_file = "glassdoor_consolidado_join_match_v2.csv"

df_target_table = (spark.read.format("csv").option("header", "true")
                                           .option("sep", "|")
                                           .option("encoding", "utf-8")
                                           .load(source_path + source_file))

df_target_table = (df_target_table.withColumnRenamed("employer-website", "employer_website")
                                  .withColumnRenamed("employer-headquarters", "employer_headquarters")
                                  .withColumnRenamed("employer-founded", "employer_founded")
                                  .withColumnRenamed("employer-industry", "employer_industry")
                                  .withColumnRenamed("employer-revenue", "employer_revenue")
                                  .withColumnRenamed("Cultura e valores", "cultura_e_valores")
                                  .withColumnRenamed("Diversidade e inclusão", "diversidade_e_inclusao")
                                  .withColumnRenamed("Qualidade de vida", "qualidade_de_vida")
                                  .withColumnRenamed("Alta liderança", "alta_lideranca")
                                  .withColumnRenamed("Remuneração e benefícios", "remuneracao_e_beneficios")
                                  .withColumnRenamed("Oportunidades de carreira", "oportunidades_de_carreira")
                                  .withColumnRenamed("Recomendam para outras pessoas(%)", "chance_recomendacao_percentual")
                                  .withColumnRenamed("Perspectiva positiva da empresa(%)", "perspectiva_positiva_percentual"))

target_path = '/home/alves/Projetos/eEDB-011-2024-3/atividade_3/tables/1_Raw/'
target_table = "employees_raw"


df_target_table.write.format("parquet").mode("overwrite").save(target_path + target_table)




