from django.shortcuts import render
from django.http import HttpResponse
from .models import Bird
from fastai import *
from fastai.vision import *



path = "/home/harsh/SOP/fastai-model/PILANI_BIRDS"

learn = load_learner(path,'birdsofpilani.pkl')
learn.precompute = False
tfms = get_transforms()
# Create your views here.

def index(request):
    return render(request,'predict/index.html')
    # return HttpResponse("<h1>This is the index page</h1>")


def result(request):
    pass
    img = request.FILES['img']
    # learn.load('/home/harsh/SOP/models/birds-stage-1-50-unfrozen')
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