
from pyspark.sql import SparkSession
import pyspark.sql.functions as f

if __name__ == "__main__":
    spark = SparkSession.builder.master("local[2]").appName("Stream_DF").getOrCreate()
    print("="*50)
    print("Zaczynamy DataFrame")
    print("="*50)
    spark.sparkContext.setLogLevel("ERROR")
    lines = spark.readStream\
        .format("socket")\
        .option("host", "localhost")\
        .option("port", 9999)\
        .load()
    words = lines.select(f.explode(f.split(lines.value, " ")).alias("word"))
    wordCounts = words.groupBy("word").count()
    query = wordCounts.writeStream.outputMode("complete").format("console").start()
    query.awaitTermination()
    query.stop()
