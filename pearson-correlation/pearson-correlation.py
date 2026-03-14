import numpy as np

def pearson_correlation(X):
    """
    Compute Pearson correlation matrix from dataset X.
    """

    X = np.asarray(X, dtype=float)
    n = X.shape[0]

    mean = np.mean(X, axis=0)

    X_centered = X - mean

    cov = (X_centered.T @ X_centered) / (n - 1)

    std_devs = np.std(X, axis=0, ddof=1)

    R = cov / np.outer(std_devs, std_devs)

    return R