import numpy as np

def outer_product(u, v):
    """
    Returns: float64 matrix of shape (m, n), the outer product u v^T.
    """
    u = np.asarray(u, dtype=float)
    v = np.asarray(v, dtype=float)

    return np.outer(u,v) # Just use np.outer for outer product.