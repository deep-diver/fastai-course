from fastai.data.external import URLs, untar_data

path = untar_data(URLs.COCO_TINY)
print(type(path))
print(path)