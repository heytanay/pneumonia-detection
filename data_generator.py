"""
Author: Tanay Mehta
Github: @heytanay
---------------------

This script contains Data Generators for the Image CNN model 
"""
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import tensorflow.keras as keras

class DataGenerator():
    def __init__(self, img_dir):
        """
        Pass in the folder where images folders are extracted.
        Passed in folder should have the following structure:

        -img_dir/
        | -train/
        |   | NORMAL/
        |   |   | -...
        |   | PNEUMONIA/
        |   |   | -...
        | -test/
        |   | NORMAL/
        |   |   | -...
        |   | PNEUMONIA/
        |   |   | -...
        | -val/
        |   | NORMAL/
        |   |   | -...
        |   | PNEUMONIA/
        |   |   | -...          

        """
        self.img_dir = img_dir
        
        if not os.path.exists(self.img_dir):
            raise FileNotFoundError(f"{self.img_dir} is not a valid Image Folder")

    def _make_generator(self):
        """
        Initialize data generators (train and validation only)
        """
        train_data_generator = ImageDataGenerator(
            rescale=1/255.,
            horizontal_flip=True,
            vertical_flip=True,
            rotation_range=0.4,
            zoom_range=0.4
        )
        valid_data_generator = ImageDataGenerator(
            rescale=1/255.
        )
        return (train_data_generator, valid_data_generator)
    
    def get_data(self):
        """
        Flow the data from the directory provided
        """
        train_dgen, val_dgen = self._make_generator()
        
        train_generator = train_dgen.flow_from_directory(
            os.path.join(self.img_dir, "train"),
            target_size=(224, 224),
            batch_size=16
        )
        valid_generator = val_dgen.flow_from_directory(
            os.path.join(self.img_dir, "val"),
            target_size=(224, 224),
            batch_size=8
        )

        return (train_generator, valid_generator)