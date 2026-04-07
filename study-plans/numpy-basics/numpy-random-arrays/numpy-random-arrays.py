import numpy as np

def generate_random_array(shape, kind, seed):
    """
    Returns: 2D ndarray of float64 random values
    """
    np.random.seed(seed)
    if 'normal' in kind:
        arr = np.random.randn(*shape)
        return arr

    else:
        return np.random.rand(*shape) # *shape unpacks [2,3] -> (2,3)
    
