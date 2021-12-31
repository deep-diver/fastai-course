from fastai.data.external import URLs, untar_data
from pathlib import Path

path = untar_data(URLs.COCO_TINY)

Path.BASE_PATH = path
print(path.ls())