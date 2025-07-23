from sklearn.svm import SVC
from matplotlib import pyplot as plt
import numpy as np

# Sample data
X = np.array([[1, 2], [2, 3], [3, 4], [5, 6], [6, 7]])
y = np.array([0, 0, 1, 1, 1])
# Create and fit the SVM model
svm = SVC(kernel='linear')
svm.fit(X, y)
# Make predictions
svm_predictions = svm.predict([[-0.8, -1]])
print("SVM Predictions:", svm_predictions)
# Plotting the predictions
plt.scatter(X[:, 0], X[:, 1], c=y, marker='o', label='Data Points')
plt.scatter([-0.8], [-1], c='red', marker='x', label='Prediction Point')
plt.title('SVM Prediction Visualization')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.grid()
plt.show()  