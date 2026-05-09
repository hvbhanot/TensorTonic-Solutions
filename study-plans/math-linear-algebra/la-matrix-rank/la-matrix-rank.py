import numpy as np

def matrix_rank(A):
    """
    Returns: int, the rank of matrix A.
    """
    A = np.asarray(A,dtype=float)

    rank = np.linalg.matrix_rank(A)

    return rank