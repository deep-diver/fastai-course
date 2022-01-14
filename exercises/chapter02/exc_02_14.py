from fastai.vision.all import *

url = 'https://github.com/deep-diver/fastai-course/raw/master/data/oxford-iiit-pet-tiny.tar.gz'
path = untar_data(url)

block = DataBlock(blocks=(ImageBlock, CategoryBlock),
                  get_items=get_image_files,
                  get_y=lambda f: f.name[0].isupper(),
                  splitter  = RandomSplitter(),
                  item_tfms = [Resize(224)])

dls = block.dataloaders(path/'images', bs=4)
dls.show_batch()