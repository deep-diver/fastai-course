---
title: 'Chapter 1: 유틸리티 함수'
description:
  'fastai가 제공하는, 귀찮은 작업을 간단하게 만들어주는 유틸리티 함수들을 살펴봅니다.'
prev: null
next: /chapter2
type: chapter
id: 1
---

<exercise id="1" title="제공되는 데이터셋 다운로드">

fastai의 `data.external` 모듈에서는 `URLs` 클래스와 `untar_data` 함수를 제공합니다. 

`URLs` 클래스에는 미리 정의된 다양한 종류의 데이터셋을 다운로드 받기위한 주소가 상수로 등록되어 있습니다. 주피터 노트북이나 Colab 같은 환경에서는 `URLs.` 까지
입력하면 접근 가능한 데이터셋 목록을 **자동완성** 기능으로 확인할 수 있습니다. 다만 여기서는 자동완성 기능은 제공하지 않기 때문에, 몇 가지 종류를 나열합니다. 
가령 `MNIST_TINY`라는 데이터셋의 URL에는 `URLs.MNIST_TINY` 같은 방식으로 접근할 수 있습니다 (모든 목록은 _[[링크](https://docs.fast.ai/data.external.html)]_ 에서 확인해 보세요).

아래 코드를 완성하여 `IMAGENETTE` 데이터셋에 접근해서 반환되는 값을 출력해 보세요.

<codeblock id="01_01">

힌트를 줄 만큼 어려운 문제가 아닙니다 :> 

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
