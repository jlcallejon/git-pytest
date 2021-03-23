import paypay

def test_iseven():
    assert paypay.iseven(1) == False
    assert paypay.iseven(132461) == False
    assert paypay.iseven(2.1) == False
    assert paypay.iseven(2) == True
    assert paypay.iseven(200) == True
    assert paypay.iseven(230132) == True


