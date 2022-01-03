from fastai.vision.all import *

url = "https://github.com/deep-diver/fastai-course/raw/master/data/oxford-iiit-pet-tiny.tar.gz"
path = untar_data(url)/"images"
files = get_image_files(path)

dls = ImageDataLoaders.from_name_func(path, files, lambda f: f[0].isupper(), 
                                      bs=4, item_tfms=Resize(224))

def my_accuracy(input, target, axis=-1):
    prediction = input.______(dim=axis)
    return (prediction == target).float().____()

learner = cnn_learner(dls, models.resnet18, metrics=[my_accuracy])
learner.fine_tune(5)
learner.recorder.plot_loss()