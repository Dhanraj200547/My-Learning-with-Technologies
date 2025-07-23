#CNN classification for MNIST dataset
import tensorflow as tf

#dataset loading
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
#preprocessing the data
X_train = X_train / 255
X_test = X_test / 255

#model 

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation="relu",input_shape=(28,28,1)),
    tf.keras.layers.MaxPooling2D((2,2),strides=2),
    tf.keras.layers.Conv2D(64, (3,3), activation="relu"),
    tf.keras.layers.MaxPooling2D((2,2),strides=2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(10, activation="softmax")
])

model.compile(optimizer="adam",loss = "sparse_categorical_crossentropy",metrics=["accuracy"])
model.fit(X_train, y_train, epochs=10)

y_pred = model.evaluate(X_test, y_test)
print("Test accuracy:", y_pred[1])  # Print only the accuracy from the evaluation