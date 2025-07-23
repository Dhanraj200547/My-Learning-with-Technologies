import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Step 1: Generate synthetic data
# Create a dataset with 3 clusters
X, y_true = make_blobs(n_samples=300, centers=3, cluster_std=1.0, random_state=42)

# Step 2: Visualize the data
plt.scatter(X[:, 0], X[:, 1], s=50)
plt.title("Generated Data")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()

# Step 3: Apply K-Means clustering
# Specify the number of clusters (k)
kmeans = KMeans(n_clusters=3, random_state=42)

# Fit the model to the data
kmeans.fit(X)

# Step 4: Retrieve cluster centers and labels
centers = kmeans.cluster_centers_
labels = kmeans.labels_

# Step 5: Visualize the clustering results
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=50, alpha=0.7)
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='x', s=200, label='Centers')
plt.title("K-Means Clustering Results")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()

# Step 6: Print the cluster centers
print("Cluster Centers:")
print(centers)
