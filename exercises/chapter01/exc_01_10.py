from torch import tensor
from torch import Tensor
from fastcore.transform import Transform, Pipeline
from torchvision.transforms.functional import to_pil_image
from IPython.display import display 

from fastai.vision.all import *

url = "https://github.com/deep-diver/fastai-course/raw/master/data/oxford-iiit-pet-tiny.tar.gz"
filename = (untar_data(url)/'images').ls()[0]

def fn2Image(x): 
    return Image.open(x)

class ToMyTensor(Transform):
    def img2tensor(img):
        "Transform image to byte tensor in `c*h*w` dim order."
        res = tensor(img)
        if res.dim()==2: res = res.unsqueeze(-1)
        return res.permute(2,0,1)
    
    def encodes(self, o:Image.Image): return image2tensor(o)
    def decodes(self, o:Tensor): return to_pil_image(o)

pipe = Pipeline([fn2Image, ToMyTensor])
encoded_img = pipe(filename)
decoded_img = pipe.decode(encoded_img)
print(f"{type(encoded_img)}, {type(decoded_img)}")

print(encoded_img)
display(decoded_img)