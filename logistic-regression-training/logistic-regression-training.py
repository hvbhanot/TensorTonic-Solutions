import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # y = y.reshape(-1, 1)
    w = np.zeros((X.shape[1]), dtype=float)
    b = 0.0

    for _ in range(steps):
        z = X @ w + b
        yhat = _sigmoid(z)

        w = w + lr / X.shape[0] * (X.T @ (y - yhat))
        b = b + lr / X.shape[0] * np.mean((y - yhat))


    return (w, b)
    
      
    