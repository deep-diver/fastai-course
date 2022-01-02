import pandas as pd
from fastai.data.external import untar_data

url = "https://github.com/deep-diver/fastai-course/raw/master/data/pascal-2007-tiny.tar.gz"
path = untar_data(url)
df = pd.read_csv(path/'train.csv')
df.head()