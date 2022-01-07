def test():
    assert "def grow_older(self: Person):" in __solution__, "grow_older 메서드의 파라미터를 정확히 지정하였나요?"
    assert "@patch(as_prop=True)" in __solution__, "full_name 메서드를 속성으로 만드는 방법을 다시 확인해보세요."
    assert "@patch(cls_method=True)" in __solution__, "CreatePerson 메서드를 클래스 메서드로 만드는 방법을 다시 확인해보세요."
    
    __msg__.good("잘 하셨습니다!")