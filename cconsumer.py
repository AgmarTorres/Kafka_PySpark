from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
import findspark

findspark.init()

sc = SparkContext('local')
spark = SparkSession(sc)


ds1 = spark \
  .read \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "localhost:9092") \
  .option("subscribe", "streaming_data") \
  .load() 
  
x = ds1.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
print(x)