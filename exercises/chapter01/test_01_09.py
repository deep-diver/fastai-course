def test():
    assert "float(o)" in __solution__, "float()을 사용하셨나요?"
    assert "int(o)" in __solution__, "int()을 사용하셨나요?"
    assert "IntToFloat()" in __solution__, "IntToFloat()을 사용하셨나요?"
    assert "t(original)" in __solution__, "IntToFloat 객체를 적절히 호출해 인코딩 하셨나요?"
    assert "t.decode(encoded)" in __solution__, "IntToFloat 객체의 decode를 적절히 호출하셨나요?"
    
    __msg__.good("잘 하셨습니다!")