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
    assert not paypay.iseven(4)
    assert not paypay.iseven(1531)
    assert not paypay.iseven(2.3)
    assert paypay.iseven(8)
    assert paypay.iseven(200)
    assert paypay.iseven(230132)


@pytest.mark.parametrize('test_input, expected', prime_cases)
def test_isprime(test_input, expected):
    assert paypay.isprime(test_input) == expected


def test_sqrt_negative():
    with pytest.raises(ValueError):
        paypay.sqrt(-1)


@pytest.mark.parametrize('word, palindrome', [('holi', False),
                                              ('Python', False),
                                              ('dabalearrozalazorraelabad', True),
                                              ('dabale arroz a la zorra el abad', False),
                                              ('Bob', True)])
def test_ispalindrome(word, palindrome):
    assert paypay.ispalindrome(word) == palindrome