from pyspark.sql import SparkSession

spark = SparkSession. \
    builder. \
    appName("pyspark-learning"). \
    master("spark://127.0.0.1:7077"). \
    config("spark.executor.memory", "512m"). \
    getOrCreate()

sc = spark.sparkContext
#
# data = spark.read.csv("s3a://de-batch-aug2022/Employee_Salaries_1.csv")
# data.show(n=5)
#
# def myFunc(x):
#     return x.split(' ')
#
# rdd = spark.sparkContext.readFile("some_file")
# rdd.map(lambda x: x.split(' '))

