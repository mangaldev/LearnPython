# from pyspark.shell import spark
from pyspark.sql import SparkSession


spark = SparkSession.builder. \
    appName("pyspark-learning-1"). \
    config("spark.executor.memory", "512m"). \
    getOrCreate()

rdd = spark.sparkContext.textFile("../resources/random.txt")



print(rdd.collect())

rdd1 = rdd.flatMap(lambda x: x.split(' '))
print(rdd1.collect())
rdd2 = rdd1.map(lambda x: (x,1))
print(rdd2.collect())
rdd3 = rdd2.groupByKey().mapValues(len)
print(rdd3.collect())