from fastcore.transform import Transform

class IntToFloat(Transform):
    def encodes(self, o): return _____(o)
    def decodes(self, o): return ___(o)

original = 100

t = __________()
encoded = t(________)
decoded = t.______(_______)

print(f"변형 전(원본): {original}")
print(f"변형 후(인코딩): {encoded}")
print(f"원복 후(디코딩): {decoded}")