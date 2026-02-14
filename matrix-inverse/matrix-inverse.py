import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    
    arr = np.array(A)

    if np.linalg.det(arr) == 0: # Checking for singularity.
       return

    A_inverse = np.linalg.inv(arr)
    return A_inverse
