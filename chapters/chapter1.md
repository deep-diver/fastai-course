---
title: 'Chapter 1: 유틸리티 함수'
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