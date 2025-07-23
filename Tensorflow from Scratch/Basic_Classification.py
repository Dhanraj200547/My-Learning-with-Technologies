# import time
# start = time.time()
# import tensorflow as tf
# end = time.time()
# print("Import took:", end - start, "seconds")
# print("TF version:", tf.__version__)

from tracemalloc import start
import tensorflow as tf
#helper libraries
import numpy as np
import matplotlib.pyplot as plt

# dataset loading
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

#preprocessing the data
X_train = X_train / 255
X_test = X_test / 255

#model

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28,1)),    #coverts 2d images to 1d arrays
    tf.keras.layers.Dense(128, activation = "relu"),     #its a fully connected layer with 128 neurons
    tf.keras.layers.Dense(10, activation = "softmax")    #output layer with 10 neurons for 10 classes
])

model.compile(optimizer="adam",loss = "sparse_categorical_crossentropy", metrics=["accuracy"]) #adam optimizer, loss function for multi-class classification using gradient descent

model.fit(X_train,y_train,epochs = 5)

y_pred = model.evaluate(X_test, y_test)
print("Test accuracy:", y_pred)
