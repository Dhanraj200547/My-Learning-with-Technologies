# from sklearn.linear_model import LinearRegression
# import numpy as np
# #dataset
# X = np.array([0,8,15,22])
# y = np.array([32,46.4,59,71.6])

# X_train = X.reshape(-1,1)
# y_train = y

# model = LinearRegression()
# model.fit(X_train,y_train)

# pred_X = model.predict(np.array([38]).reshape(-1, 1))
# print("Prediction for 38:", pred_X)

#This is the basic approach we would do using linear regression.
#Now we shall use tensorflow to do the same.

import tensorflow as tf
import numpy as np

X = np.array([-40, -10,  0,  8, 15, 22],dtype=float)
y = np.array([-40,  14, 32, 46, 59, 72],dtype=float)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1,input_shape=[1])
])

model.compile(loss="mean_squared_error", optimizer=tf.keras.optimizers.Adam(0.1))
model.fit(X, y, epochs=1000, verbose=False)

pred_X = model.predict(np.array([38.0]))

print(pred_X)
