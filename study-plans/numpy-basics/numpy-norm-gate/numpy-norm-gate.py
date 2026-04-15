import numpy as np

def norm_gate(X, W, threshold):
    """Returns: np.ndarray of shape (n, k), gated projection where rows below threshold are zeroed"""

    X = np.asarray(X, dtype=float)
    W = np.asarray(W, dtype=float)
    
    yhat = X @ W

    row_norms = np.linalg.norm(yhat, axis=1, keepdims=True) 
    yhat[row_norms[:, 0] < threshold] = 0
    
    return yhat