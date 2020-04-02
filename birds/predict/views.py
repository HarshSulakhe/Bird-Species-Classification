from django.shortcuts import render
from django.http import HttpResponse
from .models import Bird
from fastai import *
from fastai.vision import *


bs = 64
path = "/home/vishal/Documents/Bird-Species-Classification"
path_img = path+'/images'
from pathlib import Path
p = Path(path_img)
dirs = [x for x in p.iterdir() if x.is_dir()]
fnames = [get_image_files(y) for y in dirs]
fnames = [item for sublist in fnames for item in sublist]
np.random.seed(2)
pat = r'/([^/]+)_\d+_\d+.jpg$'
data = ImageDataBunch.from_name_re(path_img, fnames, pat, ds_tfms=get_transforms(), size=320, bs=bs//4)
data.normalize(imagenet_stats)
learn = cnn_learner(data, models.resnet50, metrics = error_rate)
learn.precompute = False
tfms = get_transforms()
# Create your views here.

def index(request):
    return render(request,'predict/index.html')
    # return HttpResponse("<h1>This is the index page</h1>")


def result(request):
    pass
    img = request.FILES['img']
    learn.load('/home/vishal/Documents/Bird-Species-Classification/birds-stage-1-50-unfrozen')
    im = open_image(img)
    for i in range(len(tfms)):
        im.apply_tfms(tfms[i])
    preds = learn.predict(im)
    context = {
        'preds': preds[0],
    }
    return render(request,'predict/result.html',context)
    #get image from form 
    #predict
    #get array of top 5 probabilities
    #get 5 birds corresponding to top 5
    #send these 5 birds in order through dictionary
    #display in table form in result.html