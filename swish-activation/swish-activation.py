import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    x = np.array(x, dtype=float)

    sigma_x = 1 / ( 1 + np.exp(-x))

    submission = x * sigma_x

    return submission