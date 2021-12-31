def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "URLs.COCO_TINY" in __solution__, "데이터셋을 정확히 선택하셨나요?"
    assert "untar_data(URLs.COCO_TINY)" in __solution__, "untar_data 함수를 정확히 사용하셨나요?"
    assert "print(path)" in __solution__, "path 변수를 출력하고있지 않습니다"

    __msg__.good("잘 하셨습니다!")
