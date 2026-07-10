import numpy as np

def maxpool_forward(X, pool_size, stride):
    """
    Compute the forward pass of 2D max pooling.
    """
    X = np.asarray(X, dtype=float)
    m, n = X.shape
    a = int(np.floor((m - pool_size) / stride)) + 1
    b = int(np.floor((n - pool_size) / stride)) + 1
    out = np.zeros((a, b))

    for i in range(a):
        for j in range(b):
            out[i, j] = np.max(X[i*stride : i*stride + pool_size, j*stride : j*stride + pool_size])

            
    return out.tolist()