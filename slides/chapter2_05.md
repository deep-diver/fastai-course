---
type: slides
---

# cnn_learner 함수의 파라미터

---

# cnn_learner 함수의 파라미터

`cnn_learner` 함수의 파라미터 대부분은 fast.ai 기관의 연구 경험 상, 보편적으로 잘 작동하는 기본 값으로 설정되어 있습니다. 따라서 처음에 모델을 학습시킬 때는 이 값들을 건드릴 필요가 없습니다. 나름대로 나쁘지않은 베이스라인 모델을 만들어주기 때문이죠. 

다만 이후 좀 더 성능을 끌어올리기 위해서 다양한 실험을 해야만 합니다. 여기에 예외는 없어요. fastai가 만능, 원하는 결과를 즉시 만들어주는 마법의 가루라고는 생각하지 않기 바랍니다. 또한 평가지표(메트릭)는 비즈니스 목적에 따라서 상이할 수 있기 때문에, 이를 유연하게 설정할 방법도 필요합니다. 가령 이미지 분류에서 흔히 사용되는 기본 평가지표로 정확도(accuracy)가 있습니다. 이 모든것을 가능하게 해 주는 수단이 바로 `cnn_learner` 함수가 제공하는 다양한 파라미터입니다. 이를 조금 알아볼 필요가 있겠죠.

그리고 여기서 알아보는 파라미터의 종류는 이후 복잡한 주제를 다룰 때에 그대로 활용됩니다. 

---

# 기본

- **첫 번째 파라미터**: `DataLoaders` 유형의 객체(인스턴스)를 지정합니다. 앞서 1~3 섹션에서 팩터리 메서드로 만들었던 `dls` 라는 이름의 변수에 담긴것이 바로 `DataLoaders` 유형의 객체입니다. 
  
- **두 번째 파라미터**: 첫 번째 파라미터로 주어진 데이터를 학습할 모델의 기본 구조를 선택합니다. 선택 가능한 모델의 종류는 [`models`](https://github.com/fastai/fastai/blob/master/fastai/vision/models/tvm.py) 모듈에 정의되어 있습니다. 

---
# 초기화 및 경로

- **pretrained**: 두 번째 파라미터로 지정된 모델의 **사전 학습된 가중치** 사용 여부를 결정하는 불리언 파라미터 입니다. **기본 값**은 `True`지만, 만약 여러분의 문제가 사전 학습된 문제(이미지넷 분류)와 매우 다르다면 `False`로 설정하여 밑바닥에서부터 모델을 학습시키는 편이 좋을수도 있습니다.
  
- **path**, **model_dir**: 이 두 파라미터는 모델을 저장하고, 불러오는 대상 경로를 지정하는 데 쓰입니다. 즉 `path`/`model_dir` 위치가 되겠죠. **기본 값**은 각각 `None`과 `models`로 설정되어 있으며, `path`가 `None`인 경우 기반 경로는 `cnn_learner`에 입력된 `DataLoaders` 경로에 기반해 설정됩니다. 

---

# 입력과 출력

- **n_in**: 모델의 입력 데이터가 가진 채널 수를 지정합니다. 보통 3개 채널의 이미지(R, G, B)가 사용되기 때문에, 이 파라미터의 **기본 값**은 `3`으로 설정되어 있습니다. 하지만 때로는 흑백이미지(1 채널), CMYK 형식으로 표현되는 이미지(4 채널)을 사용하는 경우도 있기 때문에 이 때는 이 값의 조정이 필요합니다. 

- **n_out**: 모델의 출력 수를 지정합니다. 여러가지 목적으로 설정될 수 있지만, 이미지 분류 문제의 경우 분류하고자 하는 범주의 개수와 동일해야 합니다. **기본 값**은 `None`이지만, `None`으로 설정된 경우 내부적으로 입력된 `DataLoaders`가 표현하는 범주의 수로 설정됩니다. 한편 fastai에서는 `DataLoaders` 객체의 범주 수를 가져오기위한 간편 함수로 `get_c`를 제공하기도 합니다(예시. `get_c(dls)`). 

- **y_range**: **n_out**으로 지정된 각 출력의 범위를 설정할 수 있습니다. 멀티 레이블 예측 문제에서 주로 활용됩니다. 이 값이 설정되지 않으면 이미지가 전체 범주 중 단일 범주에만 속한다는것을 예측합니다. 즉 각 출력 중 가장 강도가 센 출력(범주)을 찾아내는 것이죠. 이 파라미터를 설정하면 각 출력마다 독립적으로 예측을 수행하여, 이미지가 전체 범주 중 속할 수 있는 다중 범주를 예측할 수 있습니다. **기본 값**은 `None` 입니다.
  
---

# 모델의 구조 - 1

- **custom_head**: 일반적으로 컨볼루션 신경망은 몸통과 머리로 나뉘어집니다. 이 중 머리 부분은 해결하고자는 문제 마다 다르게 정의될 수 있습니다. 다만 fastai에서는 이 파라미터가 `None`인 경우, 통상적으로 잘 작동한다고 경험적으로 발견한 머리 구조를 사용합니다. 이 파라미터에는 PyTorch의 `Module`로 정의된 모델을 설정하는것도 가능한데, 이 경우 `n_out`, `y_range`, `concat_pool`, `lin_ftrs`, `ps`, `first_bn`, `bn_final`, `lin_first`, `init`과 같은 파라미터가 모두 무시됩니다. 즉 나열된 파라미터는 **머리** 부분을 만드는데 연관된 것들이며, **머리**를 만드는 별도의 함수로 제공되는 [`create_head()`](https://docs.fast.ai/vision.learner.html#create_head)가 내부적으로 사용됩니다.

아래는 fastai의 `create_head()` 함수에의해 만들어지는 기본 **머리** 구조입니다.

<img src="https://i.ibb.co/ScV1ShM/Screen-Shot-2022-01-03-at-1-26-58-PM.png" alt="create_head()"/>

---

# 모델의 구조 - 2

여기에 나열된 파라미터는 기본적으로 `create_head()`의 작동 방식을 제어하기위한 것입니다.

- **concat_pool**: 일반적으로 **컨볼루션 신경망**에서는 층마다 풀링 층이 존재하며, 여기서 **최대 풀링(`AdaptiveMaxPool2d`)** 방식을 사용하는것이 보통입니다. 그리고 몸통의 마지막에는 컨볼루션 층이 존재하고, 이를 다음 단계로 이어주기위해 풀링 층을 추가합니다. **concat_pool** 파라미터를 `False`로 설정하면 정확히 이 방식으로 작동하지만, `True`로 설정한다면 추가적으로 **평균 풀링(`AdaptiveAvgPool2d`)** 층을 하나 더 삽입합니다. 평균과 최대로 얻는 정보는 다르며 이를 조합해 최종 결과를 얻는것이 합리적이다는게 fast.ai에서의 연구가 생각한 방법이죠. **기본 값**은 `True` 입니다.

- **first_bn**: 풀링 층을 통과한 몸통의 마지막 층은 평평해집니다(`Flatten`). 그 다음 평평해진 결과물은 선형 층(`Linear`)을 통과하게 되는데, 이 파라미터는 그 사이에 배치 정규화(`BatchNorm`)를 둘 것인지를 정합니다. **기본 값**은 `True` 입니다. 

- **ps**: 평평해진 결과물이 연결되는 선형 층(`Linear`)을 통과하기 전 드롭아웃(`Dropout`) 층을 둘 것인지를 지정합니다. **기본 값**은 `[0.5]` 입니다. 즉 절반의 확률을 가진 드롭아웃 층을 추가하는 것이죠.

- **lin_ftrs**: 평평해진 결과물이 연결되는 선형 층(`Linear`)의 특징 수를 지정합니다. **기본 값**은 `[512]` 입니다. 즉 `512`개의 특징을 가진 선형 층을 추가한다는 것이죠. 

---

# 모델의 구조 - 3

여기에 나열된 파라미터는 기본적으로 `create_head()`의 작동 방식을 제어하기위한 것입니다.

- **lin_first**: 앞 슬라이드에서의 설명에 따르면 **평평 층(`Flatten`)** => **배치 정규화 층(`BatchNorm`)** => **드롭아웃 층(`Dropout`)** => **선형 층(`Linear`)**의 순서를 따르는 것처럼 보이며, 이것이 기본 배치 순서입니다. 다만 이 파라미터의 값을 `True`로 설정하면 그 순서가 **평평 층(`Flatten`)** => **선형 층(`Linear`)** => **배치 정규화 층(`BatchNorm`)** => **드롭아웃 층(`Dropout`)** 으로 바뀔 수 있습니다. 

- **bn_final**: 가장 마직막(최종 출력용 선형 층 뒤)에 **배치 정규화 층(`BatchNorm`)**을 추가로 둘지에 대한 불리언 파라미터입니다. **기본 값**은 `False` 입니다.

- **init**: **머리**를 구성하는 층들의 가중치 초기화 방식을 지정합니다. **기본 값**은 Kaiming He 초기화 방식인 `kaiming_normal_`으로 지정되어 있습니다.

참고로 `ps`와 `lin_ftrs` 파라미터는 리스트 값을 수용합니다. 기본 값으로는 하나의 값만 포함된 리스트지만, 여러개의 값을 넣어줄 수 있습니다. 이 경우 (**배치 정규화 층(`BatchNorm`)** => **드롭아웃 층(`Dropout`)** => **선형 층(`Linear`)**)을 하나의 묶음(블록)으로, 여러개를 반복적으로 더 추가할 수 있으며, 리스트의 각 값은 블록의 드롭아웃률과 선형층의 특징 수를 지정하는 데 쓰입니다. 

---

# 학습 - 1

- **loss_func**: 손실 함수를 지정합니다. **기본 값**은 `None`으로, 이 경우 팩터리 메서드로 만들어진 `DataLoaders`로부터 사용될 손실 함수를 추론합니다. 다만 원하는 손실 함수도 얼마든지 직접 지정할 수 있습니다. fastai에서 제공하는 [목록](https://docs.fast.ai/losses.html)에서 고르거나, 여러분만의 손실 함수를 직접 만들 수도 있습니다([참고](https://docs.fast.ai/losses.html#BaseLoss)). 

- **opt_func**: 최적화 알고리즘을 지정합니다. **기본 값**은 `Adam` 입니다. 그 외 사용 가능한 최적화 알고리즘은 [공식문서의 `Optimizer` 섹션](https://docs.fast.ai/optimizer.html)을 확인해 보기 바랍니다. 

- **splitter**: `freeze()` 메서드 호출시 학습을 동결시킬 부분과, 학습될 수 있는 부분을 나누어 반환하는 함수를 지정합니다. **기본 값**은 `None`인데, 이 경우 모델의 몸통과 머리 부분이 그대로 각 부분에 매핑되는 방식을 따릅니다. 

- **train_bn**: 배치 정규화 층도 학습될 것인지를 지정하는 불리언 파라미터 입니다. **기본 값**은 `True` 입니다.

---

# 학습 - 2

- **metrics**: 평가 지표 목록을 지정합니다. [단일 레이블 예측 문제](https://docs.fast.ai/metrics.html#Single-label-classification), [다중 레이블 예측 문제](https://docs.fast.ai/metrics.html#Multi-label-classification), [회귀](https://docs.fast.ai/metrics.html#Regression), [세그먼테이션](https://docs.fast.ai/metrics.html#Segmentation), [자연어 처리](https://docs.fast.ai/metrics.html#NLP) 에 따라 제공되는 목록을 확인할 수 있습니다. 하지만 여러분만의 평가 지표를 계산하는 함수도 만들 수 있는데, 여기에는 두 가지 종류가 존재합니다. 
  - 단순히 현재 학습이 진행된 에포크마다 레이블과 예측을 비교해 결과를 계산하는 **정확도**의 경우는 `input`과 `target` 텐서 파라미터를 수용하는 함수만으로 작성할 수 있습니다. 이 두 파라미터를 통해 계산된 결과를 반환하기만 하면되죠.
  - **재현률**, **정밀도** 등과 같이, 평가 지표 계산에 누적된 값이 필요한 경우라면 `AccumMetric` 인스턴스를 반환하면 됩니다. 자세한 내용은 추후 다시 살펴보겠습니다. 

- **cbs**: 콜백을 지정합니다. fastai는 학습 루프의 모든 지점에서 모델, 데이터를 접근하고 수정할 수 있는 특별한 시스템을 제공합니다. 콜백에 대해서는 추후 다시 알아보겠습니다. 다만 학습 루프내 어떤 지점들이 지정되는지는 [공식 문서](https://docs.fast.ai/callback.core.html#Callback)에서 확인할 수 있습니다. 

---

# 끝
