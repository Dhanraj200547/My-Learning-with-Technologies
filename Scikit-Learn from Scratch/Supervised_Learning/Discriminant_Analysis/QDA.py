import numpy as np
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from matplotlib import pyplot as plt

X = np.array([[1, 2], [2, 3], [3, 4], [5, 6], [6, 7]])
y = np.array([0, 0, 1, 1, 1])
Qda = QuadraticDiscriminantAnalysis()
Qda.fit(X, y)
Qda_predictions = Qda.predict([[-0.8,-1]])

print("Qda Predictions:", Qda_predictions)
# Plotting the predictions
plt.scatter(X[:, 0], X[:, 1], c=y, marker='o', label='Data Points')
plt.scatter([-0.8], [-1], c='red', marker='x', label='Prediction Point')
plt.title('Qda Prediction Visualization')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.grid()
plt.show()  