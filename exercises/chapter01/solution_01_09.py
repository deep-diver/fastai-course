from fastcore.transform import Transform

class IntToFloat(Transform):
    def encodes(self, o): return float(o)
    def decodes(self, o): return int(o)

original = 100

t = IntToFloat()
encoded = t(original)
decoded = t.decode(encoded)

print(f"변형 전(원본): {original}")
print(f"변형 후(인코딩): {encoded}")
print(f"원복 후(디코딩): {decoded}")