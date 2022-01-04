from fastai.vision.all import *

url = "https://github.com/deep-diver/fastai-course/raw/master/data/oxford-iiit-pet-tiny.tar.gz"
path = untar_data(url)/"images"
files = get_image_files(path)

dls = ImageDataLoaders.from_name_func(path, files, lambda f: f[0].isupper(), 
                                      bs=4, item_tfms=Resize(224))

learner = cnn_learner(dls, models.resnet18)

model = learner.model

# ResNet의 splitter 함수의 구현체
# - https://github.com/fastai/fastai/blob/6e44b354f4d12bdfa2c9530f38f851c54a05764d/fastai/vision/learner.py#L105
# - def  _resnet_split(m): 
#       return L(m[0][:6], m[0][6:], m[1:]).map(params)

layers = list(model.children())
print(f'모델의 길이: {len(layers)}')

layers_body = list(layers[0].children())
layers_head = list(layers[1].children())
print(f'부분 모델(몸통)의 길이: {len(layers_body)}')
print(f'부분 모델(머리)의 길이: {len(layers_head)}')
