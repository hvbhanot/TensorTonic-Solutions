import numpy as np

def linear_regression(X, y, lr, epochs):
    """
    Returns: tuple (weights, bias)
    """
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    m, n = X.shape
    W = np.zeros(n)
    b = 0.0

    for _ in range(epochs):
        err = X @ W + b - y            # (m,)
        W  = W - lr * (2.0 / m) * (X.T @ err)
        b  = b - lr * (2.0) * err.mean()

    weights = [round(float(v), 4) for v in W]
    bias    = round(float(b), 4)
    return (weights, bias)
