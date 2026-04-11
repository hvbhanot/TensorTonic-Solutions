import numpy as np

def euclidean_distance(x, y):
    """
    Returns: float, the Euclidean distance between x and y.
    """

    x = np.asarray(x,dtype=float)
    y = np.asarray(y,dtype=float)
    
    d_x_y = np.sqrt(np.sum((x-y)**2))

    return d_x_y