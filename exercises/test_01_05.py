def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "path.mk_write" in __solution__, "mk_write() 메서드를 사용하였나요?"
    assert "path.readlines" in __solution__, "ls() 메서드를 사용하였나요?"
    assert "path.delete" in __solution__, "rm() 메서드를 사용하였나요?"
    
    __msg__.good("잘 하셨습니다!")
