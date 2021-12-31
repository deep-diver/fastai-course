from fastai.data.external import URLs, untar_data
from fastai.data.transforms import get_image_files
from pathlib import Path

path = untar_data(URLs.COCO_TINY)
Path.BASE_PATH = path

images = get_image_files(path)
print(f'images 유형: {type(images)}')
# 이미지 목록의 첫 5개를 출력
print(images[:5])