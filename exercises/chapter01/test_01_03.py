def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "path.ls()" in __solution__, "ls() 메서드를 사용하였나요?"
    
    __msg__.good("잘 하셨습니다!")
