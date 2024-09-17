import pyspark
from great_expectations.dataset import SparkDFDataset


spark = pyspark.sql.SparkSession.builder.appName("delivery_validation").getOrCreate()


source_path = '/home/alves/Projetos/eEDB-011-2024-3/atividade_3/tables/3_Delivery/'
source_table = "reviews_complaints_delivery"

df_reviews_complaints_delivery = spark.read.format("parquet").load(source_path + source_table)

ge_df_reviews_complaints_delivery = SparkDFDataset(df_reviews_complaints_delivery)

ge_df_reviews_complaints_delivery.expect_column_values_to_not_be_null("CNPJ")

ge_df_reviews_complaints_delivery.expect_column_values_to_not_match_regex("CNPJ", r"^\s*$")

validation_results = ge_df_reviews_complaints_delivery.validate()

if not validation_results["success"]:
    raise ValueError("Validação falhou: CNPJ contém valores nulos ou vazios.")
