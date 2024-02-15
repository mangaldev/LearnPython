# from pyspark.shell import spark
from pyspark.sql import SparkSession


spark = SparkSession.builder. \
    appName("pyspark-learning-1"). \
    getOrCreate()

df = spark.read.text("../../resources/Employee_Salaries_1.csv")

print(df.schema)

print(df.head())