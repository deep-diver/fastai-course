from fastcore.transform import Transform, Pipeline
from torchvision.transforms.functional import to_pil_image
from IPython.display import display 

from fastai.vision.all import *

url = "https://github.com/deep-diver/fastai-course/raw/master/data/oxford-iiit-pet-tiny.tar.gz"
filename = (untar_data(url)/'images').ls()[0]

# 파일 경로를 PIL 이미지로 변환
def fn2Image(x): 
    return Image.open(x)

# PIL 이미지를 텐서로 변환
class ToMyTensor(Transform):
    def image2tensor(self, img):
        res = tensor(img)
        return res.permute(2,0,1)
    
    def tensor2img(self, tensor_img):
        res = tensor_img.permute(1,2,0).numpy().astype(np.uint8)
        return to_pil_image(res)
    
    def encodes(self, o:Image.Image): return self.image2tensor(o)
    def decodes(self, o:Tensor): return self.tensor2img(o)

# 정수형 텐서를 부동소수형 텐서로 변환
class IntToFloatTensor(Transform):
    def encodes(self, o:Tensor): return o.to(torch.float)
    def decodes(self, o:Tensor): return o.to(torch.int32)

# 텐서의 값을 0~1 사이의 값으로 변환
class NormalizeTensor(Transform):
    def encodes(self, o:Tensor): return o/255
    def decodes(self, o:Tensor): return torch.minimum(o*255, tensor(255))

pipe = Pipeline([fn2Image, ToMyTensor, IntToFloatTensor, NormalizeTensor])
encoded_img = pipe(filename)
decoded_img = pipe.decode(encoded_img)
print(f"{type(encoded_img)}, {type(decoded_img)}")

print("변환 후")
print(encoded_img.size(), encoded_img)
print("원복 후")
display(decoded_img)