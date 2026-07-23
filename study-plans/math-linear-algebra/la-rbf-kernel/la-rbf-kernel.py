import numpy as np

def rbf_kernel_matrix(X, gamma):
    """Returns: ndarray of shape (n, n), the RBF kernel matrix."""
    
    X = np.array(X, dtype=float)
    
    sq_norms = np.sum(X ** 2, axis=1)
    sq_dists = sq_norms[:, None] + sq_norms[None, :] - 2 * X @ X.T
    sq_dists = np.maximum(sq_dists, 0)  # numerical fix
    
    return np.exp(-gamma * sq_dists)
