def test():
    assert t_1 == L([0, 1, 2, 3, 4]), "t_1 결과가 다릅니다"
    assert t_2 == L([0, -1, -2, -3, -4]), "t_2 결과가 다릅니다"
    assert t_3 == L([0, -1]), "t_3 결과가 다릅니다"
    assert indicies == L([0, 1]), "indicies 결과가 다릅니다"
    assert t_4 == L([0, -1]), "t_4 결과가 다릅니다"

    assert "t.unique" in __solution__, "unique()를 사용하셨나요?"
    assert "t_1.map" in __solution__, "map()을 사용하셨나요?"
    assert "operator.neg" in __solution__, "operator.neg를 사용하셨나요?"
    assert "t_2.filter" in __solution__, "filter()을 사용하셨나요?"
    assert "t_2.argwhere" in __solution__, "argwhere()을 사용하셨나요?"
    assert "t_2[indicies]" in __solution__, "마스크 인덱스로 indicies를 사용하셨나요?"
    
    __msg__.good("잘 하셨습니다!")