from fastai.vision.all import *

url = "https://github.com/deep-diver/fastai-course/raw/master/data/pascal-2007-tiny.tar.gz"
path = untar_data(url)
df = pd.read_csv(path/'train.csv')

dls = ImageDataLoaders.from_df(__, 
                               path=____, 
                               fn_col='_____',
                               folder='_____', 
                               label_delim='_',                               
                               valid_col='________',
                               bs=8,
                               item_tfms=Resize(224))
dls.show_batch()