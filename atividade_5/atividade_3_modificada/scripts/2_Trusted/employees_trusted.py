import pyspark
from pyspark.sql.functions import col, row_number
from pyspark.sql.window import Window

spark = pyspark.sql.SparkSession.builder.appName("employees_trusted").getOrCreate()

source_path = '/home/alves/Projetos/eEDB-011-2024-3/atividade_3/tables/1_Raw/'
source_file = "employees_raw"

df_target_table = spark.read.format("parquet").load(source_path + source_file)

df_target_table = (df_target_table.withColumn("reviews_count", col("reviews_count").cast("bigint"))
                                  .withColumn("culture_count", col("culture_count").cast("bigint"))
                                  .withColumn("salaries_count", col("salaries_count").cast("bigint"))
                                  .withColumn("benefits_count", col("benefits_count").cast("bigint"))
                                  .withColumn("Geral", col("Geral").cast("double"))
                                  .withColumn("cultura_e_valores", col("cultura_e_valores").cast("double"))
                                  .withColumn("diversidade_e_inclusao", col("diversidade_e_inclusao").cast("double"))
                                  .withColumn("qualidade_de_vida", col("qualidade_de_vida").cast("double"))
                                  .withColumn("alta_lideranca", col("alta_lideranca").cast("double"))
                                  .withColumn("remuneracao_e_beneficios", col("remuneracao_e_beneficios").cast("double"))
                                  .withColumn("oportunidades_de_carreira", col("oportunidades_de_carreira").cast("double"))
                                  .withColumn("chance_recomendacao_percentual", col("chance_recomendacao_percentual").cast("double")/100)
                                  .withColumn("perspectiva_positiva_percentual", col("perspectiva_positiva_percentual").cast("double")/100))

df_target_table = (df_target_table.withColumnRenamed("employer_name", "EMPLOYER_NAME")
                                  .withColumnRenamed("reviews_count", "REVIEWS_COUNT")
                                  .withColumnRenamed("culture_count", "CULTURE_REVIEWS_COUNT")
                                  .withColumnRenamed("salaries_count", "SALARY_REVIEWS_COUNT")
                                  .withColumnRenamed("benefits_count", "BENEFIT_REVIEWS_COUNT")
                                  .withColumnRenamed("Geral", "OVERALL_RATING")
                                  .withColumnRenamed("cultura_e_valores", "CULTURE_RATING")
                                  .withColumnRenamed("diversidade_e_inclusao", "DIVERSITY_RATING")
                                  .withColumnRenamed("qualidade_de_vida", "LIFE_QUALITY_RATING")
                                  .withColumnRenamed("alta_lideranca", "HIGH_LEADERSHIP_RATING")
                                  .withColumnRenamed("remuneracao_e_beneficios", "SALARY_RATING")
                                  .withColumnRenamed("oportunidades_de_carreira", "CAREER_OPORTUNITY_RATING")
                                  .withColumnRenamed("chance_recomendacao_percentual", "RECOMMENDATION_CHANCE")
                                  .withColumnRenamed("perspectiva_positiva_percentual", "POSITIVE_PERSPECTIVE")
                                  .withColumnRenamed("Nome", "INSTITUTION_NAME"))

window_clause = Window.partitionBy("INSTITUTION_NAME").orderBy(col("REVIEWS_COUNT").desc())

df_target_table = (df_target_table.withColumn("POSIT", row_number().over(window_clause))
                                  .filter(col("POSIT") == 1))

df_target_table = df_target_table.drop("employer_website", "employer_headquarters", "employer_founded", "employer_industry", "employer_revenue", "url", "Segmento", "match_percent", "POSIT")

target_path = '/home/alves/Projetos/eEDB-011-2024-3/atividade_3/tables/2_Trusted/'
target_table = "employees_trusted"

df_target_table.write.format("parquet").mode("overwrite").save(target_path + target_table)




