# Bird-Species-Classification
A deep learning approach to classify bird species through multi-class classification on images.

Dataset Used - [Caltech-UCSD Birds-200-2011](http://www.vision.caltech.edu/visipedia/CUB-200-2011.html)

Dependencies:
* Tensorflow 2.0.0
* Keras 2.3.1
* Python 3.7.6


To run the model on your system, first clone the repository
```
git clone https://github.com/HarshSulakhe/Bird-Species-Classification.git
```

Shift to the cloned directory
```
cd Bird-Species-Classification
```

Run the following command
```
python train.py --dataset <insert image folder name here> --model BirdModel --labelbin mlb.pickle
```

Training will take time if you do not have a CUDA enabled GPU

## To Do
- [ ] Implement the same model in PyTorch
- [ ] Update ReadMe with plots of accuracy and the final confusion matrix


