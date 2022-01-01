def test():
    assert "r'^(.*)_\d+.jpg'" in __solution__, "정규표현식을 정확히 입력하셨나요?"

    __msg__.good("잘 하셨습니다!")
