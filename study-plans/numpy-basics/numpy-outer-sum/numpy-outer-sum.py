import numpy as np

def outer_sum(a, b):
    """Returns: np.ndarray of shape (m, n), outer sum where out[i,j] = a[i] + b[j]"""

    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    
    output = np.add.outer(a, b) # Just this function does the outer sum
    return output