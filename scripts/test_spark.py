from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").getOrCreate()
df = spark.createDataFrame([("Alice", 23), ("Bob", 34)], ["Name", "Age"])
df.show()
spark.stop()
