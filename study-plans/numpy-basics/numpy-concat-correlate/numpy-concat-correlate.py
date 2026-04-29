import numpy as np

def compare_correlations(a, b):
    """Returns: np.ndarray of shape (3, n, n), stacked correlation matrices"""

    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)

    combined = np.concatenate([a,b], axis = 0)

    a_c = np.corrcoef(a.T)
    b_c = np.corrcoef(b.T)
    c_c = np.corrcoef(combined.T)

    return [a_c, b_c, c_c]