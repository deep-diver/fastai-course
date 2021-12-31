import operator
from fastcore.foundation import L

t = L(range(5))
t *= 5
print(t)

# 고유한 값들로만 추리기
t_1 = t.unique()
print(t_1)

# 부호 바꾸기 - operator.neg 이용
t_2 = t_1.map(operator.neg)
print(t_2)

# -1보다 작은 값 제거(필터링하기) - filter() 메서드, lambda 활용
t_3 = t_2.filter(lambda o: o >= -1)
print(t_3)

# 0보다 작은 값 제거(필터링하기) - argwhere() 메서드
indicies = t_2.argwhere(lambda o: o >= -1)
print(indicies)

t_4 = t_2[indicies]
print(t_4)