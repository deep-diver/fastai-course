def test():
    assert "Pipeline([fn2Image, ToMyTensor, IntToFloatTensor, NormalizeTensor])" in __solution__, "변형 절차의 순서가 올바른가요?"
    
    __msg__.good("잘 하셨습니다!")