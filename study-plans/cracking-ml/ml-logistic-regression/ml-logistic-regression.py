import numpy as np

def logistic_regression(X, y, lr=0.01, n_iters=1000):
    """
    Returns:
        tuple: (weights, bias) where weights is a list and bias is a float
    """

    X = np.asarray(X,dtype=float)
    y = np.asarray(y,dtype=float)

    n,m = X.shape
    W = np.zeros((m,))
    b = 0.0

    for iter in range(n_iters):

        z = X @ W + b
        yhat = np.where(z >= 0,
                1.0 / (1.0 + np.exp(-z)),
                np.exp(z) / (1.0 + np.exp(z))) # Numericall stable sigmoid...

        d_l_w = (X.T @ (yhat - y))/ n
        d_l_b = (np.sum(yhat - y)) / n

        W -= lr * d_l_w
        b -= lr * d_l_b


    return (W,b)    
        
