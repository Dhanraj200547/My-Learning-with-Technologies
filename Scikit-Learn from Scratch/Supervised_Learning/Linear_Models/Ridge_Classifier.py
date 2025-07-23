from sklearn.linear_model import RidgeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load data
X, y = load_iris(return_X_y=True)
# Convert to binary classification
y = (y == 0).astype(int)

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Train Ridge Classifier
model = RidgeClassifier(alpha=1.0)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))

