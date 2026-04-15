import numpy as np

def linear_combination(vectors, coefficients):
    """
    Returns: float64 array, the weighted sum of vectors.
    """

    v = np.asarray(vectors,dtype=float)
    c = np.asarray(coefficients,dtype=float)

    return c@v