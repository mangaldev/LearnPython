from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, lit
from pyspark.sql.types import IntegerType

# Create a SparkSession
spark = SparkSession.builder \
    .appName("UDF Example") \
    .getOrCreate()

# Sample DataFrame
df = spark.createDataFrame([(1, "John"), (2, "Alice"), (3, "Bob")], ["id", "name"])


# Define a UDF to compute the length of a string
def string_length(name):
    return len(name)


# SQLSQL User-Defined Functions (UDFs)

df.createOrReplaceTempView("random")

df.show()
#
# # Register a UDF to convert names to uppercase
# spark.udf.register("to_uppercase", lambda s: s.upper())
#
# # Use the UDF in a SQL query
# result = spark.sql("SELECT id, to_uppercase(name) AS uppercase_name FROM random")
#
# result.show()

#
# # DataFrame User-Defined Functions (UDFs):
#
# Register the UDF
string_length_udf = udf(string_length, IntegerType())

# Apply the UDF to a DataFrame column
df = df.withColumn("name_length", string_length_udf("name"))

# Show the result
df.show()
