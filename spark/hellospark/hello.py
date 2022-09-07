import time

from pyspark.sql import SparkSession

spark = SparkSession. \
    builder. \
    appName("pyspark-learning-1"). \
    master("spark://127.0.0.1:7077"). \
    config("spark.executor.memory", "512m"). \
    getOrCreate()

sc = spark.sparkContext
#
big_list = range(10000)
rdd = sc.parallelize(big_list, 2)
odds = rdd.filter(lambda x: x % 2 != 0)
print(odds.take(5))

while True:
    time.sleep(1)
# data = spark.read.csv("iris.data")
# data.show(n=5)
