## TheGenderClassifier
This project takes the images from camera and detects gender on the basis of its experience that it had learned from traning from 339 female faces and 291 male faces. This is machine learning project using logistic regression as a traning algorithm.

Requirements.
Python 2.4
numpy
Matlab
Scipy

Matlab is used for traning and then their variables are transfered to python by scipy!

Description of various script...

#COMPUTER VISION(PYTHON):

BEGIN.PY- This is the main program which takes the feed from the camera, detect face and crop it.Then it loads a .mat file which is a pre-trained matrix trained from matlab.

FACE CROP- This is a simple program that was used to crop the dataset images which had used for training.

RENAME MULTIPLE- This is also a very simple program which is used to rename multiple file numerically.

RESIXE- This program resizes the image.

#TRAINING:

COSTFUNCTION: Calculate the cost.

TRAIN LOGISTIC:The training code for logistic regression.

