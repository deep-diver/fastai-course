from fastcore.foundation import L

# 0~11 숫자를 포함한 L을 생성합니다 (range 사용)
t = ____________
print(t)

# L의 내용을 두 배 불립니다
t __ 2
print(t)

# 0이 담긴 위치 (0, 12) 를 튜플 방식으로 찾아서 반환합니다
t_1 = t[_, __]
print(t_1)

# 0이 담긴 위치 (0, 12) 를 마스킹 방식으로 찾아서 반환합니다
#  - 마스크를 만듭니다 0과 12번째 위치에만 True를 넣습니다
mask = L([True])
mask += L([False] * 11)
mask += L([True])
mask += L([False] * 11)

t_2 = t______
print(t_2)