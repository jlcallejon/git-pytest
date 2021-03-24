import paypay

def test_iseven():
    assert not paypay.iseven(1)
    assert not paypay.iseven(132461)
    assert not paypay.iseven(2.1)
    assert paypay.iseven(2)
    assert paypay.iseven(200)
    assert paypay.iseven(230132)