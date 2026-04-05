import numpy as np

def create_filled_array(shape, kind):
    """
    Returns: 2D numpy array of given shape with dtype float64
    """

    if kind == 'zeros':
        arr = np.zeros(shape, dtype=float)
        return arr 

    arr = np.ones(shape, dtype=float)
    return arr