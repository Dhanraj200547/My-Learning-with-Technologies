import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from matplotlib import pyplot as plt

X = np.array([[1, 2], [2, 3], [3, 4], [5, 6], [6, 7]])
y = np.array([0, 0, 1, 1, 1])
lda = LinearDiscriminantAnalysis()
lda.fit(X, y)
lda_predictions = lda.predict([[-0.8,-1]])

print("LDA Predictions:", lda_predictions)
# Plotting the predictions
plt.scatter(X[:, 0], X[:, 1], c=y, marker='o', label='Data Points')
plt.scatter([-0.8], [-1], c='red', marker='x', label='Prediction Point')
plt.title('LDA Prediction Visualization')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.grid()
plt.show()  