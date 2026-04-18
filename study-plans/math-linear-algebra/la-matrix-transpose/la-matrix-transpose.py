import numpy as np

def matrix_transpose(A):
    """
    Returns: ndarray, the transpose of A.
    """

    A = np.asarray(A, dtype=float)
    m,n = A.shape

    output = np.zeros((n,m))
    
    for i in range(m):
        for j in range(n):
            output[j,i] = A[i,j]


    return output
    

            