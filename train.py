"""
Author: Tanay Mehta
Github: @heytanay
---------------------

This script is the entry point and will be used when training the model
"""
import os
import numpy as np
import sys

from helper import get_arg
from data_generator import DataGenerator
from model import Model

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Conv2D, Flatten, MaxPooling2D, Dense
from tensorflow.keras.models import Sequential

# Get image directory from arguments
img_dir = get_arg(2)

# Get epochs from arguments 
epochs = get_arg(4)
if epochs == -1:
    epochs = 20

# Initialize the data generator and get their objects
data_generator = DataGenerator(img_dir=img_dir)

train_gen, val_gen = data_generator.get_data()

# Initialize the model and train on data
nn = Model(epochs=int(epochs))

nn.fit(train_gen, val_gen)