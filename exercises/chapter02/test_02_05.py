def test():
    assert "path=path" in __solution__, "path를 정확히 입력 하셨나요?"
    assert "fn_col='fname'" in __solution__, "fn_col를 정확히 입력 하셨나요?"
    assert "folder='train'" in __solution__, "folder를 정확히 입력 하셨나요?"
    assert "valid_col='is_valid'" in __solution__, "valid_col를 정확히 입력 하셨나요?"
    assert "label_delim='_'" in __solution__, "label_delim을 정확히 입력 하셨나요?"

    __msg__.good("잘 하셨습니다!")
