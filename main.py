from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .master('local') \
    .appName("SimpleApp") \
    .getOrCreate()

print(spark)