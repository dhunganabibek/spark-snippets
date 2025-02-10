from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .master('local') \
    .appName("SimpleApp") \
    .getOrCreate()

spark.sql('SELECT current_date()').show()