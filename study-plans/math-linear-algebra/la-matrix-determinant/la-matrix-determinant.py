import numpy as np

def is_singular_rank(A):
    # Works for square matrices
    return np.linalg.matrix_rank(A) < A.shape[0]

def matrix_determinant(A):
    """
    Returns: float, the determinant of square matrix A.
    """

    A = np.asarray(A,dtype=float)
    if is_singular_rank(A):
        return 0

    else:
        det = np.linalg.det(A)
        return det