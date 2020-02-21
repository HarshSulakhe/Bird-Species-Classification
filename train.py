import matplotlib
matplotlib.use("Agg")

from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from keras.preprocessing.image import img_to_array
from sklearn.preprocessing import MultiLabelBinarizer,OneHotEncoder
from sklearn.model_selection import train_test_split
from BirdModel.birdnet import BirdNet
import matplotlib.pyplot as plt
from imutils import paths
import numpy as np
import argparse
import random
import pickle
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="path to input dataset (i.e., directory of images)")
ap.add_argument("-m", "--model", required=True,
	help="path to output model")
ap.add_argument("-l", "--labelbin", required=True,
	help="path to output label binarizer")
ap.add_argument("-p", "--plot", type=str, default="plot.png",
	help="path to output accuracy/loss plot")
args = vars(ap.parse_args())


EPOCHS = 1
INIT_LR = 1e-3
BS = 32
IMAGE_DIMS = (112, 112, 3)


print("[INFO] loading images...")
imagePaths = sorted(list(paths.list_images(args["dataset"])))
random.seed(42)
random.shuffle(imagePaths)
# initialize the data and labels
data = []
labels = []
i = 0

for imagePath in imagePaths:
	l = str(int(imagePath[7:10]))
	image = cv2.imread(imagePath)
	image = cv2.resize(image, (IMAGE_DIMS[1], IMAGE_DIMS[0]))
	image = img_to_array(image)
	data.append(image)
	labels.append([l])
	# print(l)

data = np.array(data, dtype="float") / 255.0
labels = np.array(labels)

print("[INFO] class labels:")
# mlb = MultiLabelBinarizer()
# labels = mlb.fit_transform(labels)
# print(mlb.classes_)

ohc = OneHotEncoder()
labels = ohc.fit_transform(labels)
print(ohc.categories_)
# loop over each of the possible class labels and show them
for (i, label) in enumerate(ohc.categories_):
	print("{}. {}".format(i + 1, label))

(trainX, testX, trainY, testY) = train_test_split(data,
	labels, test_size=0.2, random_state=42)
# construct the image generator for data augmentation
# aug = ImageDataGenerator(rotation_range=25, width_shift_range=0.1,
# 	height_shift_range=0.1, shear_range=0.2, zoom_range=0.2,
# 	horizontal_flip=True, fill_mode="nearest")

model = BirdNet.build(
	width=IMAGE_DIMS[1], height=IMAGE_DIMS[0],
	depth=IMAGE_DIMS[2], classes=len(ohc.categories_))
# initialize the optimizer
opt = Adam(lr=INIT_LR, decay=0.05)

model.compile(loss="binary_crossentropy", optimizer=opt,
	metrics=["accuracy"])
# train the network
print("[INFO] training network...")
H = model.fit(x = trainX,y = trainY, batch_size = BS,validation_data = (testX,testY),
	epochs=EPOCHS, verbose=1)


print("[INFO] serializing network...")
model.save(args["model"])
# save the multi-label binarizer to disk
print("[INFO] serializing label binarizer...")
f = open(args["labelbin"], "wb")
f.write(pickle.dumps(ohc))
f.close()

plt.style.use("ggplot")
plt.figure()
N = EPOCHS
plt.plot(np.arange(0, N), H.history["loss"], label="train_loss")
plt.plot(np.arange(0, N), H.history["val_loss"], label="val_loss")
plt.plot(np.arange(0, N), H.history["acc"], label="train_acc")
plt.plot(np.arange(0, N), H.history["val_acc"], label="val_acc")
plt.title("Training Loss and Accuracy")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend(loc="upper left")
plt.savefig(args["plot"])
