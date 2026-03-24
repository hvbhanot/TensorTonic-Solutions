import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """

    norm_a = np.linalg.norm(a) if np.linalg.norm(a) != 0 else 1
    norm_b = np.linalg.norm(b) if np.linalg.norm(b) != 0 else 1
    cos_a_b = (np.dot(a,b)) / (norm_a * norm_b)

    return cos_a_b