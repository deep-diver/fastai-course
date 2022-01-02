from fastai.vision.all import *

url = "https://github.com/deep-diver/fastai-course/raw/master/data/pascal-2007-tiny.tar.gz"
path = untar_data(url)
df = pd.read_csv(path/'train.csv')

dls = ImageDataLoaders.from_df(df, 
                               path=path, 
                               fn_col='fname',
                               folder='train', 
                               label_delim=' ',                               
                               valid_col='is_valid',
                               bs=8,
                               item_tfms=Resize(224))
dls.show_batch()