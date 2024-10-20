from spark_app.util import spark_util
from pyspark.sql import functions as F

spark = spark_util.get_spark()


def test_get_spark():
    assert spark_util.get_spark()


def test_multiply():
    df = spark \
        .createDataFrame([
        (1, 1.0),
        (2, 2.0),
    ], ("id", "v"))
    df1 = df.withColumn("v1", spark_util.multiply(F.col("v"), 2))
    res = df1 \
        .filter(F.col("id") == 1) \
        .select("v1") \
        .first() \
        .asDict()["v1"]
    assert (res == 2.0)
