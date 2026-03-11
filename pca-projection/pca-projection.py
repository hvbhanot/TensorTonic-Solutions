import numpy as np

def pca_projection(X, k):
    X = np.asarray(X, dtype=float)
    m, n = X.shape

    X = X - np.mean(X, axis=0)
    co_var = (1 / (m - 1)) * (X.T @ X)

    e_val, e_vec = np.linalg.eigh(co_var)

    idx = np.argsort(e_val)[::-1] # NOTE : Returns sorted aurguments.

    vectors = e_vec[:, idx[:k]]

    X_proj = X @ vectors

    return X_proj