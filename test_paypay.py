from pyspark.sql import SparkSession

import paypay
import pytest

def test_iseven():
    assert not paypay.iseven(1)
    assert not paypay.iseven(132461)
    assert not paypay.iseven(2.1)
    assert paypay.iseven(2)
    assert paypay.iseven(200)
    assert paypay.iseven(230132)


@pytest.fixture(scope="session")
def spark_session(request):
    """ fixture for creating a spark Session
    Args:
        request: pytest.FixtureRequest object
    """

    spark = SparkSession.builder.master('local[*]').appName('local-test').getOrCreate()

    request.addfinalizer(lambda: spark.stop())

    return spark


def test_count_customers(spark_session):
    assert paypay.count_customers('sample.csv', spark_session) == 193

