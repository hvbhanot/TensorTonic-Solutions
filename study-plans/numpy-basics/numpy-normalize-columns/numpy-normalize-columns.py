import numpy as np

def normalize(data):
    """Returns: np.ndarray of shape (m, n), z-score normalized per column"""

    data = np.asarray(data, dtype=float)

    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)

    data = (data - mean) / std

    return data