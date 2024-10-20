from pyspark.sql import SparkSession


def get_spark():
    spark = SparkSession.builder.appName("my pyspark").getOrCreate()
    return spark


def multiply(col, factor=2):
    return col * factor
