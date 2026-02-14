import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """

    arr = np.array(x)
    submission = 1 / (1 + np.exp(-arr))
    return submission.tolist()
