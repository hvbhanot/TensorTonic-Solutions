import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    Rows = samples
    Columns = features
    """
    
    X = np.asarray(X, dtype=float)

    if X.ndim < 2 or X.shape[0] == 1 : # Checks for just one row, if yes we cannot have a cov matrix
      return None

    n, _ = X.shape

    mean = np.mean(X, axis=0)

    X_centered = X - mean

    cov = (X_centered.T @ X_centered) / (n - 1)

    return cov