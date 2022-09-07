# from pyspark.shell import spark
from pyspark.sql import SparkSession


def lengthOfList(x):
    l = []
    for i in x:
        l.append((i, len(i)))
    return l


spark = SparkSession.builder. \
    appName("pyspark-learning-1"). \
    config("spark.executor.memory", "512m"). \
    getOrCreate()

rdd = spark.sparkContext.textFile("../resources/random.txt")
print(rdd.collect())
rdd2 = rdd.flatMap(lambda x: x.split(' '))
print(rdd2.collect())
rdd3 = rdd2.map(lambda x: (x, 1))
print(rdd3.collect())

# rdd4 = rdd3.groupByKey()
# print(rdd4.mapValues(lambda x:len(x)).collect())

print(rdd3.reduceByKey(lambda x, y: x + y).collect())
# print(rdd2.collect())
#
# rdd3 = rdd2.flatMap(lambda x: lengthOfList(x))
#
# print(rdd3.collect())
#
#
#
#
#
# def freq(words):
#     freq ={}
#     for word in words:
#         if freq[word]:
#             freq[word] += freq[word]
#
# words.map(lambda x: (x,1))


# [5,12,1,2,]
#

# rdd = spark.sparkContext.parallelize(arr)
