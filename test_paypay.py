import pytest
import paypay

prime_cases = [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (6, False),
    (7, True),
    (8, False),
    (9, False),
    (10, False),
    (11, True),
    (12, False),
    (13, True)]


def test_iseven():
    assert paypay.iseven(1) == False
    assert paypay.iseven(132461) == False
    assert paypay.iseven(2.1) == False
    assert paypay.iseven(2) == True
    assert paypay.iseven(200) == True
    assert paypay.iseven(230132) == True


@pytest.mark.parametrize('test_input, expected', prime_cases)
def test_isprime(test_input, expected):
    assert paypay.isprime(test_input) == expected
