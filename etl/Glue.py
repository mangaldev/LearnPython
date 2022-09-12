import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import when
from pyspark.sql import SparkSession

args = getResolvedOptions(sys.argv, ['s3_target_path_key', 's3_target_path_bucket', 's3_output_path_bucket'])
bucket = args['s3_target_path_bucket']
fileName = args['s3_target_path_key']
output_bucket = args['s3_output_path_bucket']

print("<<<<<<<<Starting Glue Job>>>>>>>>>>>>>")
print(bucket, fileName, output_bucket)

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

inputFilePath = f"s3a://{bucket}/{fileName}"
finalFilePath = f"s3a://{output_bucket}/result/output"
tempFilePath = f"s3a://{output_bucket}/result/temp"

if "LOAD" in fileName:
    fldf = spark.read.csv(inputFilePath)
    fldf = fldf.withColumnRenamed("_c0", "id").withColumnRenamed("_c1", "FullName").withColumnRenamed("_c2", "City")
    fldf.write.mode("overwrite").csv(finalFilePath)
else:
    udf = spark.read.csv(inputFilePath)
    udf = udf.withColumnRenamed("_c0", "action").withColumnRenamed("_c1", "id") \
        .withColumnRenamed("_c2", "FullName").withColumnRenamed("_c3", "City")
    ffdf = spark.read.csv(finalFilePath)
    ffdf.repartition(1).write.format("csv").mode("overwrite").save(tempFilePath)
    print("<< Reading the file again from temp directory.... >>")
    ffdf = spark.read.csv(tempFilePath)
    ffdf = ffdf.withColumnRenamed("_c0", "id").withColumnRenamed("_c1", "FullName").withColumnRenamed("_c2", "City")

    for row in udf.collect():
        if row["action"] == 'U':
            ffdf = ffdf.withColumn("FullName",
                                   when(ffdf["id"] == row["id"], row["FullName"]).otherwise(ffdf["FullName"]))
            ffdf = ffdf.withColumn("City", when(ffdf["id"] == row["id"], row["City"]).otherwise(ffdf["City"]))

        if row["action"] == 'I':
            insertedRow = [list(row)[1:]]
            columns = ['id', 'FullName', 'City']
            newdf = spark.createDataFrame(insertedRow, columns)
            ffdf = ffdf.union(newdf)

        if row["action"] == 'D':
            ffdf = ffdf.filter(ffdf.id != row["id"])

    print("<< Overwriting the file now .... >>")
    ffdf.write.format("csv").mode("overwrite").save(finalFilePath)

job = Job(glueContext)
job.init('Glue Job for CDC aggregated file', args)
job.commit()

# --JOB_NAME something
# --s3_target_path_bucket	de-batch-aug2022/cdc/world/Persons
# --s3_output_path_bucket	de-batch-aug2022-result
# --s3_target_path_key	LOAD00000001.csv