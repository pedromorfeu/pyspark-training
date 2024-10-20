from spark_app.util.spark_util import multiply
from util import spark_util
from pyspark.sql import functions as F


def main():
    print("hello")
    spark = spark_util.get_spark()
    df = spark \
        .createDataFrame([
        (1, 1.0),
        (1, 2.0),
        (2, 3.0),
        (2, 5.0),
        (2, 10.0)
    ], ("id", "v"))
    df.show()
    df \
        .withColumn("v1", multiply(F.col("v"), 2)) \
        .show()


if __name__ == "__main__":
    main()
