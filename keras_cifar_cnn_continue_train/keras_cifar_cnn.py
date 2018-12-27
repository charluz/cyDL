#!/usr/bin/env python

"""
Using Keras/CNN to do object classification.
"""
################################################
# Import Library
################################################
from keras.datasets import cifar10
import numpy as np
np.random.seed(10)

################################################
# Prepare (download) data
################################################
print("Preparing CIFAR10 data ...")
(x_img_train, y_label_train), (x_img_test, y_label_test) = cifar10.load_data()

print("Training data: ", "images: ", x_img_train.shape, " labels: ", y_label_train.shape)
print("Test data:     ", "images: ", x_img_test.shape, " labels: ", y_label_test.shape)

#------------------------------------------------
# Normalize training and test data
#------------------------------------------------
x_img_train_normalize = x_img_train.astype('float32') / 255.0
x_img_test_normalize = x_img_test.astype('float32') / 255.0

#------------------------------------------------
# Perform One hot encoding to labels
#------------------------------------------------
from keras.utils import np_utils
y_label_train_OneHot = np_utils.to_categorical(y_label_train)
y_label_test_OneHot = np_utils.to_categorical(y_label_test)

print("Before OneHot encoding: test labels: ", y_label_test.shape)
print("After OneHot encoding : test labels: ", y_label_test_OneHot.shape)

################################################
# Construct Model
################################################
