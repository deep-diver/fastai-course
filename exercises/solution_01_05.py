from fastcore.all import *

# 대상 경로로 ~/my_data/hello.txt를 지정합니다
path = Path('~/my_data/hello.txt')
print(path)

print('1 -- 경로(파일)을 생성합니다...')
# '안녕하세요 세상이여' 문자열이 담긴 경로(파일)을 생성합니다
path.mk_write('안녕하세요 세상이여')
# 생성된 파일의 내용(텍스트)를 출력합니다
print(path.readlines())

print('2 -- 경로(파일)을 제거합니다...')
# 삭제할 경로를 지정합니다
path = Path('~/my_data')
# 대상 경로를 삭제합니다
path.delete()

# ~/ 디렉터리에 my_data 디렉터리가 삭제된 것을 확인합니다
print('3 -- 삭제된 후 ~/ 디렉터리의 내용을 확인합니다...')
print(Path('~/').ls())