def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "L(range(12))" in __solution__, "range를 이용해 초기 L을 생성하였나요?"
    assert "t *= 2" in __solution__, "*= 연산자를 사용하였나요?"
    assert "t[0, 12]" in __solution__, "튜플 방식으로 찾아서 반환하였나요?"
    assert "t[mask]" in __solution__, "마스킹 방식으로 찾아서 반환하였나요?"

    __msg__.good("잘 하셨습니다!")
