def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "result = URLs.COCO_TINY" in __solution__, "데이터셋을 정확히 선택하셨나요?"
    assert "print(result)" in __solution__, "result 변수를 출력하고있지 않습니다"
    assert result == 'https://s3.amazonaws.com/fast-ai-coco/coco_tiny.tgz', "다른 데이터셋을 지정하지 않았나요?"

    __msg__.good("잘 하셨습니다!")
