import numpy as np

def hadamard_product(A, B):
    """
    Returns: ndarray, the element-wise product A * B.
    """

    A = np.asarray(A, dtype=float)
    B = np.asarray(B, dtype=float)

    m,n = A.shape

    H_p = np.zeros((m,n))

    for i in range(m):
        for j in range(n):

            H_p[i,j] = A[i,j] * B[i,j]


    return H_p
    