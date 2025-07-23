#problems in color images and general datasets
#sizes of images we need to resize all types of images to same size
#color images have 3 channels (RGB) instead of 1 channel in grayscale images

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator # type: ignore
import os

#datset load
_URL = 'https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip'
zip_dir = tf.keras.utils.get_file('cats_and_dogs_filterted.zip', origin=_URL, extract=True)

base_dir = os.path.join(zip_dir, 'cats_and_dogs_filtered')
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')

train_cats_dir = os.path.join(train_dir, 'cats')  # directory with our training cat pictures
train_dogs_dir = os.path.join(train_dir, 'dogs')  # directory with our training dog pictures
validation_cats_dir = os.path.join(validation_dir, 'cats')  # directory with our validation cat pictures
validation_dogs_dir = os.path.join(validation_dir, 'dogs')  # directory with our validation dog pictures

batch_size = 100
image_shape = (150,150)

#data augmentation
train_datagen = ImageDataGenerator(rescale=1./255)
validation_datagen = ImageDataGenerator(rescale=1./255)

train_data = train_datagen.flow_from_directory(
    train_dir,
    shuffle=True,
    target_size=image_shape,
    batch_size=batch_size,
    class_mode='binary'
)

validation_data = validation_datagen.flow_from_directory(
    validation_dir,
    shuffle=False,
    target_size=image_shape,
    batch_size=batch_size,
    class_mode='binary'
)

#model
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(150, 150, 3)),
    tf.keras.layers.MaxPooling2D((2,2)),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2,2)),
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2,2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dropout(0.5),  # Adding dropout to prevent overfitting
    tf.keras.layers.Dense(1, activation ="sigmoid")
])

model.compile(optimizer= "adam",loss= 'binary_crossentropy', metrics=['accuracy'])

model.fit(train_data, epochs=30, validation_data=validation_data)
validation_loss, validation_acc = model.evaluate(validation_data)
print("validation accuracy:", validation_acc)  # Print only the accuracy from the evaluation
print("validation loss:", validation_loss)  # Print the validation loss
print("Model summary:")
model.summary()  # Print the model summary to see the architecture


"""
CNNs with RGB Images of Different Sizes:

Resizing: When working with images of different sizes, you must resize all the images to the same size so that they can be fed into a CNN.

Color Images: Computers interpret color images as 3D arrays.

RGB Image: Color image composed of 3 color channels: Red, Green, and Blue.

Convolutions: When working with RGB images we convolve each color channel with its own convolutional filter. Convolutions on each color channel are performed in the same way as with grayscale images, i.e. by performing element-wise multiplication of the convolutional filter (kernel) and a section of the input array. The result of each convolution is added up together with a bias value to get the convoluted output.

Max Pooling: When working with RGB images we perform max pooling on each color channel using the same window size and stride. Max pooling on each color channel is performed in the same way as with grayscale images, i.e. by selecting the max value in each window.

Validation Set: We use a validation set to check how the model is doing during the training phase. Validation sets can be used to perform Early Stopping to prevent overfitting and can also be used to help us compare different models and choose the best one.

Methods to Prevent Overfitting:

Early Stopping: In this method, we track the loss on the validation set during the training phase and use it to determine when to stop training such that the model is accurate but not overfitting.

Image Augmentation: Artificially boosting the number of images in our training set by applying random image transformations to the existing images in the training set.

Dropout: Removing a random selection of a fixed number of neurons in a neural network during training.

You also created and trained a Convolutional Neural Network to classify images of Dogs and Cats with and without Image Augmentation and Dropout. You were able to see that Image Augmentation and Dropout greatly reduces overfitting and improves accuracy. As an exercise, you were able to apply everything you learned in this lesson to create your own CNN to classify images of flowers."""
