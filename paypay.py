from pyspark.sql import SparkSession, functions


def iseven(n: int) -> bool:
    return n % 2 == 0


def sqrt(n: float, threshold: 1e-3) -> float:

    L = n
    W = n / L

    rel_error = abs(L - W) / L

    while rel_error > threshold:
        L = (L + W) / 2
        W = n / L
        rel_error = abs(L - W) / L

    return L


def count_customers(path: str, spark: SparkSession) -> int:
    df = spark.read.csv(path, header=True, inferSchema=True)
    result = df.select(functions.countDistinct('msisdn').alias('result'))
    return result.first()['result']
