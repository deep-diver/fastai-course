def test():
    assert "cnn_learner(dls, models.resnet18)" in __solution__, "DataLoaders와 모델을 정확히 입력하셨나요?"
    assert "learner.fine_tune(1)" in __solution__, "fine_tune 메서드를 사용하셨나요?"

    __msg__.good("잘 하셨습니다!")
