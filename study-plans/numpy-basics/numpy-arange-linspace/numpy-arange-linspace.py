import numpy as np

def create_sequence(start, stop, param, kind):
    """
    Returns: 1D ndarray of float64 values
    """

    if 'arange' in kind:
        arr = np.arange(start, stop, param, dtype=float)
        return arr

    else :
        arr = np.linspace(start,stop,param,dtype=float)
        return arr