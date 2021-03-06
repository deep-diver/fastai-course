from fastai.vision.all import *

url = "https://github.com/deep-diver/fastai-course/raw/master/data/oxford-iiit-pet-tiny.tar.gz"
path = untar_data(url)/"images"
files = get_image_files(path)

dls = ImageDataLoaders.from_name_func(____, _____, lambda f: f[0].isupper(), 
                                      bs=4, item_tfms=Resize(224))
dls.show_batch()