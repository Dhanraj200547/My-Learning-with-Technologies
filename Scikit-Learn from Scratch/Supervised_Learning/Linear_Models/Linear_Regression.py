from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

import numpy as np

X = np.array([1,2,3,4]).reshape(-1,1)
y = np.array([5,6,7,8])

X_train, X_test, y_train , y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = LinearRegression()

model.fit(X_train,y_train)

predictions = model.predict(X_test)

print(mean_squared_error(predictions,y_test))

print(model.predict(np.array([9]).reshape(-1,1)))