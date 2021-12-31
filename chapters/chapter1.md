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

<!-- <exercise id="1" title="Introduction" type="slides">

<slides source="chapter1_01_introduction">
</slides>

</exercise>

<exercise id="2" title="Getting Started">

Let's ask some questions about the slides. Whats the correct answer?

<choice>
<opt text="Answer one">

This is not the correct answer.

</opt>

<opt text="Answer two" correct="true">

Good job!

</opt>

<opt text="Answer three">

This is not correct either.

</opt>
</choice>

</exercise>

<exercise id="3" title="First steps">

This is a code exercise. The content can be formatted in simple Markdown – so
you can have **bold text**, `code` or [links](https://spacy.io) or lists, like
the one for the instructions below.

- These are instructions and they can have bullet points.
- The code block below will look for the files `exc_01_03`, `solution_01_03` and
  `test_01_03` in `/exercises`.

<codeblock id="01_03">

This is a hint.

</codeblock>

</exercise> -->
