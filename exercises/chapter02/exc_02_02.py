from fastai.vision.all import *

url = "https://github.com/deep-diver/fastai-course/raw/master/data/oxford-iiit-pet-tiny.tar.gz"
image_list = get_image_files(untar_data(url)/"images").sorted()

filename1 = image_list[0].name
filename2 = image_list[3].name
print(f"{filename1}, {filename2}")

def label_func(f):
    return ___
  
label1 = label_func(filename1)
label2 = label_func(filename2)
print(f"{label1}, {label2}")