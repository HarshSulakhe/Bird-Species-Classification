# Bird-Species-Classification

A deep learning approach to classify bird species through multi-class classification on images.

## Objective

To design a simple system that identifies the type of bird species in an image that a user uploads. This would make it easier for a person to identify and understand the rich variety of species within the BITS Pilani campus. We implemented a transfer learning approach that achieves the same. 

## Dataset

[Caltech-UCSD Birds-200-2011](http://www.vision.caltech.edu/visipedia/CUB-200-2011.html) for initial pilot run.
Once the model architecture (pre-trained ResNet50) was tested, a new custom dataset was curated consisting of birds specific to Pilani (BITS Pilani, Pilani Campus)

We use our current knowledge of the known bird species in Pilani to scrape images off Google. Approximately 100 images were collected for each of the 35 bird species.

![Pilani_Birds](./Images/Pilani_Birds.PNG?raw=true "Pilani_Birds")

## Proposed Technique

Our algorithm is divided into three main parts:
1. Data Augmentation
2. Model training
3. Web application development

### Phase I - Data Augmentation

During training, images were augmented using a random `horizontal flip`, `vertical flipping` and also `rotation of an angle of +10 degreees to -10 degrees`. This was done to allow for a user to click an image using a non-professional camera and be able to identify the bird specie using our model. Images were normalized using ImageNet statistics of mean and standard deviation.

###  PHASE II - Model

- We used a *ResNet50* architecture pre-trained on the *ImageNet* database. The reason for doing so is that a pre-trained model is already efficient at classifying a large number of real-life categories. On fine-tuning this model using our custom dataset, the model simply has to adjust a few of its parameters rather than begin from scratch. This reduces training time considerably. While training the model, we used a *cyclic learning rate* with the maximum set at 10^-4 and minimum set at 10^-6. The use of this cyclic learning rate was to avoid convergence at local optima. The model was trained on 8 epochs first, with only the last 5 layers trainable and then fine-tuned using all layers on 3 epochs. 

- The model is trained using a categorical cross-entropy loss function. 

![Cross_Entropy_Loss](./Images/Cross_Entropy_Loss.PNG?raw=true "Cross_Entropy_Loss")

### PHASE III - Web Application Development

We built a web platform where a user can upload an image of a bird and submit it to view the model’s prediction.

![Web_App](./Images/Web_App.PNG?raw=true "Web_App")

## Accuracy

* Caltech-UCSD Birds-200-2011 Dataset: `81.54%`
* Dataset specific to the Pilani region: `87%`

## Dependencies:

* Django 2.2
* fastai 1.0.61
* Python 3.7.6

## Instructions to Run

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

## Team Members

1. Vishal Mittal [Profile](https://github.com/vismit2000)
2. Harsh Sulakhe [Profile](https://github.com/HarshSulakhe)
