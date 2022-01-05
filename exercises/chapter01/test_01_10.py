def test():
    assert "self.image2tensor(Image.open(o))" in __solution__, "Path 입력에 대한 인코딩 메서드를 적절히 구현하셨나요?"
    assert "self.image2tensor(o)" in __solution__, "PIL Image에 대한 인코딩 메서드를 적절히 구현하셨나요?"
    assert "t(filename)" in __solution__, "Path에 대해 ImageToTensor 객체를 적절히 호출해 인코딩 하셨나요?"
    assert "t(pil_image)" in __solution__, "PIL Image에 대해 ImageToTensor 객체를 적절히 호출해 인코딩 하셨나요?"
    
    __msg__.good("잘 하셨습니다!")