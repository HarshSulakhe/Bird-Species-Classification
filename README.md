# Bird-Species-Classification

A deep learning approach to classify bird species through multi-class classification on images.

Dataset Used - [Caltech-UCSD Birds-200-2011](http://www.vision.caltech.edu/visipedia/CUB-200-2011.html) for initial pilot run.
Once the model architecture (pre-trained ResNet50) was tested, a new custom dataset was curated consisting of birds specific to Pilani (BITS Pilani, Pilani Campus)

Dependencies:
* Django 2.2
* fastai 1.0.61
* Python 3.7.6


To run the model on your system, first clone the repository
```
git clone https://github.com/HarshSulakhe/Bird-Species-Classification.git
```

Shift to the cloned directory
```
cd Bird-Species-Classification/birds
```

Run the following command
```
python manage.py runserver
```

