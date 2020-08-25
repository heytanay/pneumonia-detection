"""
Author: Tanay Mehta
Github: @heytanay
---------------------

This is where the model lives
"""

import numpy as np
from tensorflow.keras.layers import Conv2D, Flatten, MaxPooling2D, Dense
from tensorflow.keras.models import Sequential

class Model():
    def __init__(self, epochs):
        self.epochs = epochs
        self.model = Sequential()
        self.model.add(Conv2D(filters=128, kernel_size=(3,3), activation='relu', input_shape=(224, 224, 3)))
        self.model.add(MaxPooling2D(pool_size=(2,2)))
        self.model.add(Conv2D(filters=128, kernel_size=(3,3), activation='relu'))
        self.model.add(MaxPooling2D(pool_size=(2,2)))
        self.model.add(Conv2D(filters=64, kernel_size=(3,3), activation='relu'))
        self.model.add(MaxPooling2D(pool_size=(2,2)))
        self.model.add(Conv2D(filters=32, kernel_size=(3,3), activation='relu'))
        self.model.add(MaxPooling2D(pool_size=(2,2)))
        self.model.add(Flatten())

        self.model.add(Dense(256, activation='relu'))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(64, activation='relu'))
        self.model.add(Dense(2, activation='softmax'))
        self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    
    def fit(self, train_data, val_data):
        hist = self.model.fit(
            train_data,
            epochs=self.epochs,
            validation_data=val_data
        )
        return hist