import numpy as np

def cosine_similarity(z):
    return 1 / 1 + np.exp(-z)

def cosinesimilarity(vec1,vec2):
    return np.dot(vec1,vec2) / (np.linalg.norm(vec1)) * (np.linalg.norm(vec2))