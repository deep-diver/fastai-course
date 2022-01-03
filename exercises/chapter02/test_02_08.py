def test():
    assert "input.argmax(dim=axis)" in __solution__, "argmax를 사용하셨나요?"
    assert "return (prediction == target).float().mean()" in __solution__, "mean을 사용하셨나요?"

    __msg__.good("잘 하셨습니다!")
