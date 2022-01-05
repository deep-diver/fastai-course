from pathlib import Path
from fastcore.transform import Transform
from torchvision.transforms.functional import to_pil_image
from IPython.display import display 

from fastai.vision.all import *

class ImageToTensor(Transform):
    def image2tensor(self, img):
        res = tensor(img)
        return res.permute(2,0,1)

    def tensor2img(self, tensor_img):
        res = tensor_img.permute(1,2,0).numpy().astype(np.uint8)
        return to_pil_image(res)

    def encodes(self, o:Path): return self.image2tensor(Image.open(o))
    def encodes(self, o:Image.Image): return self.image2tensor(o)

    def decodes(self, o:Tensor): return self.tensor2img(o)

url = "https://github.com/deep-diver/fastai-course/raw/master/data/oxford-iiit-pet-tiny.tar.gz"
filename = (untar_data(url)/'images').ls()[0]
pil_image = Image.open(filename)

t = ImageToTensor()
encoded_img1 = t(filename)
encoded_img2 = t(pil_image)

assert torch.equal(encoded_img1, encoded_img2) == True

decoded_img = t.decode(encoded_img1)
print(encoded_img1)
display(decoded_img)