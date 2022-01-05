---
title: '1장: 유틸리티 기능'
description:
  'fastai가 제공하는, 귀찮은 작업을 간단하게 만들어주는 유틸리티 함수들을 살펴봅니다.'
prev: null
next: /chapter2
type: chapter
id: 1
---

<exercise id="1" title="제공되는 데이터셋의 URL 접근">

fastai의 `data.external` 모듈에서는 `URLs` 클래스를 제공합니다.

`URLs` 클래스에는 미리 정의된 다양한 종류의 데이터셋을 다운로드 받기위한 주소가 상수로 등록되어 있습니다. 주피터 노트북이나 Colab 같은 환경에서는 `URLs.` 까지
입력하면 접근 가능한 데이터셋 목록을 **자동완성** 기능으로 확인할 수 있습니다. 다만 여기서는 자동완성 기능은 제공하지 않기 때문에, 몇 가지 종류를 나열합니다. 

가령 `MNIST_TINY`라는 데이터셋의 URL에는 `URLs.MNIST_TINY` 같은 방식으로 접근할 수 있습니다 (모든 목록은 _[[링크](https://docs.fast.ai/data.external.html)]_ 에서 확인해 보세요). 

fastai에서 제공하지 **않는** 데이터셋은 무엇인가요?

<choice>
<opt text="ML_SAMPLE">

잘못 선택하셨습니다!

</opt>

<opt text="IMAGENET" correct="true">

정답입니다!

</opt>

<opt text="PETS">

잘못 선택하셨습니다!

</opt>
</choice>

아래 코드를 완성하여 `COCO_TINY` 데이터셋에 접근해서 반환되는 값을 출력해 보세요.

<codeblock id="01_01">

힌트를 줄 만큼 어려운 문제는 아닙니다 :> 

</codeblock>

</exercise>

<exercise id="2" title="제공되는 데이터셋의 다운로드">

fastai의 `data.external` 모듈에서는 `URLs` 클래스 외 `untar_data` 함수도 제공합니다. 

`untar_data` 함수는 첫 번째 파라미터로 입력된 URL 문자열이 가리키는 압축 파일을 다운로드하고, 압축을 해제한 다음, 압축이 해제된 경로를 가리키는 파이썬의 표준 [`Path` 객체](https://docs.python.org/3/library/pathlib.html#pathlib.Path)를 반환합니다. 

다운 및 압축이 해제되는 기본 디렉터리는 경로는 `~/.fastai/data/압축파일명`이 되며, `~/.fastai/` 이후의 경로는 `c_key` 파라미터로 조정될 수 있습니다([링크](https://docs.fast.ai/data.external.html#untar_data)). `archive` 파라미터는 다운로드된 압축 파일이 보존될 경로를 별도로 지정하기 위해 제공됩니다. 이 파라미터가 설정되지 않았다면, 압축이 해제된 후 압축 파일은 삭제됩니다.

`URLs` 클래스가 제공하는 다양한 데이터셋을 다운로드하고, 압축을 해제하는 데도 `untar_data`가 활용될 수 있습니다. 가령 `MNIST_TINY` 라는 데이터셋을 다운로드하려면 `untar_data(URLs.MNIST_TINY)` 처럼 코드를 작성할 수 있습니다. 

아래 코드를 완성하여 `COCO_TINY` 데이터셋을 다운로드하고 압축을 해제해 보세요. 그리고 반환된 자료형과 값을 출력해 보세요.

<codeblock id="01_02">

힌트를 줄 만큼 어려운 문제는 아닙니다 :> 

</codeblock>

</exercise>

<exercise id="3" title="확장된 Path 객체 - 1">

fast.ai에서는 fastai 외에도 여러가지 오픈소스 프로젝트를 진행했습니다. 그 중 fastcore는 파이썬의 기본 기능을 좀 더 편리하게 사용할 수 있도록 확장된 기능을 제공하는 패키지 입니다.

앞서 `untar_data` 함수는 `Path` 객체를 반환했습니다. 그리고 이 `Path`는 파이썬의 표준 라이브러리가 제공하는 것이죠. 파이썬에서는 [몽키패치(Monkey Patch)](https://en.wikipedia.org/wiki/Monkey_patch)가 어렵지 않기 때문에, 부가적인 기능을 얹거나 기존 기능을 약간 변형한 커스터마이징을 간단히 할 수 있습니다. 

fastcore 패키지는 몽키패치를 보다 쉽고, 명시적으로 할 수 있는 방법으로 `@patch` 데커레이터를 제공합니다. 이 데커레이터를 사용하는 방법은 다른 섹션에서 다루겠지만, 몽키패치를 통해 fastcore가 기존 `Path` 객체에 어떤 기능을 확장시켜뒀는지를 이해하는것은 흥미롭습니다. 가령 리눅스 터미널에서 파일 목록을 확인할 때 사용하는 `ls` 명령어와 같은것을 심어두었죠 ([몽키패치된 소스코드 링크](https://github.com/fastai/fastcore/blob/3c4da0a3a702c4b790bcf2bbe27231b250356542/fastcore/xtras.py#L312)). 

가령 `untar_data` 함수가 반환한 경로내 파일 목록을 확인하고 싶다면 `ls()` 메서드를 활용해볼 수 있습니다. 아래 코드를 완성하여 `ls()` 메서드가 반환하는 내용이 무엇인지를 확인해 보세요.

<codeblock id="01_03">

`ls()` **메서드** 를 사용해 보세요.

</codeblock>

또 다른 몽키패치로는 `BASE_PATH`가 있습니다. 다만 이것은 속성(attribute)으로, `Path.BASE_PATH=경로` 처럼 직접 추가해야 합니다. `BASE_PATH` 속성이 설정되면 fastcore는 내부적으로 설정된 경로로 `relative_to` 메서드를 호출합니다. 즉 상대 경로를 결정하는 것이죠([relative_to 메서드 공식 문서](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.relative_to)). 

앞서 `ls()` 메서드가 출력한 결과가 `Path('/home/jovyan/.fastai/data/coco_tiny/train')` 처럼 다소 난잡해 보일 수도 있다는것을 확인했습니다. 전체를 다 알아야하는 경우도 있지만, 정확한 경로를 알고난 후에는 `/home/jovyan/.fastai/data/coco_tiny/` 처럼 긴 베이스 경로는 더 이상 출력할 필요가 없겠죠. 수 많은 파일이 포함된 경우 육안으로 쫒아가기 힘들 때가 있습니다. 

따라서 `untar_data`로 얻은 `Path` 객체 자체를 `BASE_PATH` 속성 값으로 할당해주면, `/home/jovyan/.fastai/data/coco_tiny/` 까지를 상대경로로 인식하게 됩니다 (실제 경로 자체를 바꾸는게 아닙니다). 그 영향을 확인해보죠. 아래 코드를 완성하여 `BASE_PATH` 속성이 할당된 후의 출력 결과를 확인해 보세요.

<codeblock id="01_04">

`BASE_PATH` 속성을 설정해 보세요

</codeblock>

</exercise>

<exercise id="4" title="확장된 Path 객체 - 2">

fastcore에서는 앞서 본 `ls()`와 `BASE_PATH` 외에도 `Path`에 몇 가지 기능을 더 부여하고 있습니다. 많이는 없어서 겁먹을 필요 없어요. 몇 가지 더 있을 뿐입니다. 

- [`readlines()` 메서드](https://github.com/fastai/fastcore/blob/3c4da0a3a702c4b790bcf2bbe27231b250356542/fastcore/xtras.py#L288): `Path` 경로가 가리키는 파일의 내용을 읽어옵니다. 단순히 `open`이 내장된 메서드로 볼 수 있습니다.
- [`mk_write()` 메서드](https://github.com/fastai/fastcore/blob/3c4da0a3a702c4b790bcf2bbe27231b250356542/fastcore/xtras.py#L299): `Path` 경로가 가리키는 파일에 텍스트 데이터를 채워넣어 생성합니다. 이 때 해당 파일이 포함될 경로 트리가 존재하지 않는다면 모든 경로도 함께 생성합니다. 채워넣을 텍스트(문자열) 데이터를 첫 번째 파라미터에 부여합니다.
- [`delete()` 메서드](https://github.com/fastai/fastcore/blob/3c4da0a3a702c4b790bcf2bbe27231b250356542/fastcore/xtras.py#L333): `Path` 경로가 가리키는 파일, 심볼릭링크, 디렉터리 등을 삭제합니다. 디렉터리가 지정된 경우 하위 디렉터리까지 모두 삭제하며, 심볼릭링크가 지정된 경우 링크를 해제하는 `unlink()` 메서드가 호출됩니다. 

아래 코드를 완성하여 `"안녕하세요 세상이여"` 라는 문자열이 적힌 파일을 `~/my_data/hello.txt`에 만들고, 그 내용을 출력해 보세요. 또 그 다음 생성한 파일을 삭제해 보세요. 삭제 대상은 `~/my_data` 디렉터리를 포함해 하위에 든 모든것입니다.

<codeblock id="01_05">

파일을 생성하고, 읽고, 삭제하는 데는 어떤 메서드가 사용될까요?

</codeblock>

</exercise>

<exercise id="5" title="경로내 모든 이미지 목록을 만들기">

fastai는 주어진 특정 경로내 모든 이미지 목록을 가져오는 간단한 수단을 제공합니다. `data.transforms` 서브 모듈에 정의된 `get_image_files()` 함수가 바로 그 역할을 하죠. 

`get_image_files()`는 단순히 재귀적으로 모든 하위 경로에 포함된 이미지 목록을 가져옵니다. 이때 표준 파이썬 라이브러리가 제공하는 [`memetypes`](https://github.com/python/cpython/blob/1b37268ef10bd20c30d349b8401c88215c8a6be8/Lib/mimetypes.py#L431)를 참조하여, `memtype`이 `image/`에 매핑된 파일만을 수집합니다([근거링크](https://github.com/fastai/fastai/blob/99d38fec7207db9b4209568bebc85ded7e3d3f1b/fastai/data/transforms.py#L54)). 

가령 `get_image_files(Path 또는 문자열로 표현된 경로)`를 호출하면, 주어진 경로내의 모든 이미지 파일 목록을 `list` 형태로 반환합니다. 정확히는 fastcore에서 `list`를 확장해 만든 `L` 이라는 객체를 반환하죠. `L`에 대한 내용은 차차 알아봅니다.

아래 코드를 완성하여 주어진 경로 `path`에 포함된 모든 이미지 목록을 가져온 뒤, 첫 5개를 출력해 보세요. 출력 결과를 통해 반환된 `images`가 `L` 이라는 유형의 클래스이며, 각 이미지 목록에 대한 경로 또한 `Path.BASE_PATH`가 적용되었다는 사실을 확인해 보세요.

<codeblock id="01_06">

get_image_files 함수를 사용해 보세요.

</codeblock>

</exercise>

<exercise id="6" title="list(리스트) 기능을 확장시킨 L - 1">

앞서 본 `L`은 fastcore에서 `list`의 기능을 확장시킨 클래스 입니다. 확장시킨 것이기 때문에 기존 `list`가 사용되어야 하는 모든 곳에서 사용될 수 있으며, 여기에 부가적으로 편리한 연산자 또는 메서드를 제공합니다.

제공되는 전체 기능이 생각보다 많기 때문에 여기서는 모든것을 다루지 않습니다. 몇 가지만 다룰게요. 다만 전체 기능 목록은 [여기](https://fastcore.fast.ai/foundation.html#L)에서 확인할 수 있으니 참조하기 바랍니다.

우선 `L` 객체는 파이썬에서 제공하는 `list`, `range` 등 `iterable`한 객체를 대입해서 만들 수 있습니다. 그리고 기본적으로 `list` 처럼 작동하기 때문에 `list` 에서 사용 가능한 모든 초기화 방법을 제공하죠. 가령 `0~11` 까지의 숫자를 가진 `L`을 만드는 방법은 `L(range(12))`와 같습니다. 이는 `list`와 동일한 사용법 입니다.

이미 `list`에서도 `append`, `+`와 같은 연산자를 지원합니다. 그리고 `L`에서는 `*` 연산자를 추가적으로 더 지원합니다. 작동 방식은 예상한바와 같이 현재 담긴 리스트를 `*` 뒤에 지정된 만큼 복제하여 리스트를 만듭니다. 

또한 특정 요소에 접근하는 방식으로 튜플, 마스킹을 지원합니다. 즉 길이가 4인 `t` 라는 `L` 객체가 있다고 가정했을 때, `t[0, 3]`은 첫 번째와 네 번째 요소를 담은 `L`을 반환합니다. 또한 `t[[False, False, True, False]]`는 `True`로 마스킹된 세 번째 요소만을 담은 `L`을 반환하죠. 

한번 실습해보겠습니다. 아래 코드는 `0~11` 까지의 숫자를 담은 `L` 객체를 생성한 다음, 또 다른 `0~11`을 이어 붙입니다. 그리고 그 중 `0`이라는 숫자가 담긴 위치를 튜플과 마스킹 방식으로 접근해 출력합니다. 아래 코드를 완성해보세요.

<codeblock id="01_07">

range, *=, 튜플 인덱싱, 마스크 인덱싱 방법을 활용해 보세요.

</codeblock>

</exercise>

<exercise id="7" title="list(리스트) 기능을 확장시킨 L - 2">

`L` 객체는 또 아래와 같은 유용한 기능을 제공합니다.

- [`unique()` 메서드](https://fastcore.fast.ai/foundation.html#L.unique): 리스트에서 고유한 값들만 추려내어 반환합니다. 기본적으로는 추려진 값 목록은 정렬되어 있지 않지만, 원본의 순서는 보장됩니다. `sort` 파라미터를 `True`로 설정하는 경우 목록의 정렬을 함께 수행합니다. 또한 `bidir` 파라미터를 `True`로 설정하면 결괏값에 각 목록에 인덱스를 부여한 딕셔너리도 함께 반환해 줍니다. 
- [`filter()` 메서드](https://fastcore.fast.ai/foundation.html#L.filter): 이름 그대로 `L` 객체에 포함된 요소를 필터링합니다. 필터링은 함수를 통해 수행되며, `filter()` 메서드의 첫 번째 파라미터 또는 `f` 파라미터에 해당 함수를 등록합니다. `lambda`를 써도 상관 없습니다. 추가적으로 `negate` 파라미터를 `True`로 설정하는 경우 지정된 함수의 조건에 매칭되지 **않는** 요소만을 선택합니다. 만약 지정된 함수에 다양한 파라미터를 전달하고 싶다면 `args` 및 `kwargs` 파라미터를 활용할 수 있습니다.
- [`argwhere()` 메서드](https://fastcore.fast.ai/foundation.html#L.argwhere): `filter()` 메서드와 동일하게 작동하지만, 실제 값 대신 조건을 만족하는 값이 위치한 인덱스 목록을 반환합니다. 마찬가지로 `negate` 파라미터가 존재합니다.
- [`map()` 메서드](https://fastcore.fast.ai/foundation.html#L.map): 첫 번째 인자로 주어진 함수를 모든 요소에 적용하여 반환합니다. 즉 X->Y 처럼 특정 규칙에 의해 변형된 요솟값 목록을 반환하는 데 쓰입니다. 만약 지정된 함수에 다양한 파라미터를 전달하고 싶다면 `args` 및 `kwargs` 파라미터를 활용할 수 있습니다.

아래 코드를 완성하여 중복된 정수 값들이 존재하는 `L` 객체가 고유한 값들만을 가지도록 만든 뒤, 모든 값들의 부호를 뒤집어 보세요 (이 때 사용되는 함수는 파이썬 표준 라이브러리인 [`operator.neg`](https://github.com/python/cpython/blob/1b37268ef10bd20c30d349b8401c88215c8a6be8/Lib/operator.py#L112)가 사용됩니다). 그 다음 특정 크기 이상의 요소들만을 추려내 보세요. `filter()`와 `argwhere()` 두 방식을 모두 사용해 보기 바랍니다 (`argwhere()` 사용시 앞서 배운 `L`의 마스킹 기법이 활용되어야 합니다)

<codeblock id="01_08">

`unique()`, `filter()`, `argwhere()`, `map()` 메서드를 모두 사용해야 합니다.

</codeblock>

</exercise>

<exercise id="8" title="데이터 인코딩/디코딩을 위한 Transform">

종종 데이터는 일련의 변형 과정을 거쳐 원하는 최종 결과물로 만들어집니다. 가령 파일명(`Path`) => 파이썬 객체로 표현된 이미지(`PIL.Image.Image`) => 텐서로 표현된 이미지(`torch.tensor.Tensor`) 처럼 데이터의 형식 자체를 바꿔버리는 데이터 변형 파이프라인이 있을 수 있습니다. 여기에 추가적으로 텐서로 표현된 이미지(`torch.tensor.Tensor`)를 => 부동소수로 표현된 픽셀 값 => 픽셀 값 정규화와 같이 모델이 기대하는 입력 값으로 변형시키는 파이프라인도 존재할 수 있겠죠. 

fastcore 패키지에서는 이러한 데이터 변형 파이프라인을 손쉽게 작성할 수 있는 클래스로, `transform` 서브 모듈내 `Transform`과 `Pipeline`을 제공하고 있습니다. 그리고 이것이 실제로 fastai 라이브러리에서 데이터 변형을 처리하는 주요 수단으로 이용되고 있죠.

이름에서 알 수 있듯이 `Pipeline`은 일련의 `Transform` 객체로 구성되어 데이터 변형 파이프라인을 구성합니다. 가령 `Pipeline([변형1, 변형2, ...])`와 같은 식이죠. 그리고 나만의 `Transform` 클래스를 작성하는 방법은 `Transform` 클래스를 상속받고, 여기에 변형될 값을 반환하는 `encodes(self, o)` 메서드를 구현하는 간단한 절차로 구성됩니다. 또한 변형된 값을 다시 원복하려면 원복될 값을 `decodes(self, o)`라는 디코딩용 메서드를 구현하면 됩니다(`decodes`의 `o`는 `encodes`를 통해 변형된 데이터라고 가정합니다).

그리고 작성된 변형 클래스를 입력 데이터에 적용하는 방법은 단순 **호출** 입니다. 즉 `IntToFloat` 이라는 `Transform` 클래스가 있다면, 이 클래스의 객체를 만든 뒤 `객체(10)`과 같이 호출할 수 있으며, 그 결과로 얻는 결과물은 부동소수가 될 것입니다. 반대인 디코딩(원복)은 `decode(변형된 값)` 메서드를 호출해주면 됩니다. 아래 코드를 완성하여 정수 값을 입력받아 부동 소수로 변형하고, 부동 소수를 다시 정수로 원복하는 `IntToFloat`를 작성해보세요. 그리고 실제 작동하는 모습을 확인해 보세요.

<codeblock id="01_09">
타입에 알맞은 캐스팅을 해보세요. Transform 객체를 통해 변형, 원복하는 방법을 떠올려보세요!
</codeblock>

</exercise>

<exercise id="9" title="견고하면서 일반화된 Transform 만들기">

앞서 만든 `Transform`의 단점은 변형될 입력 데이터가 반드시 **정수**라고 가정한 채 실행되어야 한다는 것입니다. 즉 **정수** 외 다른 자료형 데이터가 입력된다면 오작동하거나 에러가 발생할겁니다. 따라서 특정 데이터 유형에만 작동하게끔 만들어줄 필요가 있겠죠. 이는 단순히 **mypy**의 타입 어노테이션으로 가능한데요, `def encodes(self, o:int)` 처럼 인코딩 메서드를, `def decodes(selef, o:float)` 처럼 디코딩 메서드를 정의하면 됩니다. 그러면 해당 데이터 유형에 대해서만 작동하며, 그 외 자료형이 들어오는 경우에는 무시하게됩니다.

한편 일부 `Transform`은 개념적으로 다양한 자료형에 대해 작동할 수 있습니다. 가령 **이미지**를 PyTorch의 `Tensor`로 변환하는 과정을 생각해보죠. **이미지**라는것은 매우 _추상적인_ 말입니다. 파일경로, 넘파이로 표현된 이미지, PIL 이미지 객체, 단순히 픽셀 값 리스트로 표현된 이미지, 또는 완전히 바이트 수준으로 표현된 이미지 등 다양할 것입니다. 따라서 _어떤_ **이미지**라도 `Tensor`로 변환될 수 있다면 좋겠죠. 

가장 간단히는 인코딩 메서드를 구현할 때, `isinstance` 키워드로 자료 형 체크를 수행해볼 수 있습니다. 하지만 더 명료하게 만드는 방법이 있습니다. 이는 여러개의 `encodes` 메서드를 정의하는 것입니다. 즉 `def encodes(self, o:Path)`, `def encodes(self, o:np.array)`, `def encodes(self, o:PIL.Image.Image)`, ... 와 같이 메서드들을 오버로딩해줍니다. 그러면 `Transform` 객체 호출시 입력된 데이터 유형에 따라 알맞은 녀석이 자동으로 선택됩니다. 

아래의 코드를 완성해보세요. 방금 설명한바와 같이 `Path`와 `PIL.Image.Image` 두 개를 모두 수용하는 `ImageToTensor`라는 클래스를 정의합니다. 이미지를 텐서로, 텐서를 다시 이미지로 변환하는 메서드는 미리 제공됩니다. 

<codeblock id="01_10">
타입에 알맞은 캐스팅을 해보세요. Transform 객체를 통해 변형, 원복하는 방법을 떠올려보세요!
</codeblock>

눈치채셨겠지만, 모든 정보가 완벽히 **원복** 가능한 것은 아닙니다. 텐서로 변환된 이미지를 다시 동일한 파일 이름으로 돌려놓을 수는 없습니다. 이를 가능하게 하려면 `ImageToTensor` 객체내 멤버 변수를 두어야해요. 하지만 이는 계산에 의한 원복은 아니죠. 대표적인 예로는 이미지 크기를 축소한 뒤 다시 원래 크기로 늘리거나, 텍스트를 특수한 기호로 인코딩한 뒤 다시 텍스트로 돌려놓는 등의 작업이 있습니다. 

</exercise>

<exercise id="10" title="일련의 데이터 인코딩/디코딩을 위한 Pipeline">
<codeblock id="01_11">
타입에 알맞은 캐스팅을 해보세요. Transform 객체를 통해 변형, 원복하는 방법을 떠올려보세요!
</codeblock>
</exercise>