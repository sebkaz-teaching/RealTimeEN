from pyspark.sql import SparkSession

if __name__ == "__main__":
    
    spark = SparkSession.builder\
        .appName("spark1")\
        .getOrCreate()
    
    sc = spark.sparkContext
    
    sc.setLogLevel("ERROR")
    
    
    lines = sc.textFile('README.md')
    
    spark_count = lines.filter(lambda x: 'spark' in x.lower())
    print(spark_count.collect())

    result = spark_count.count()
    
    print(f"Masz {result} wierszy z wyrazem spark")