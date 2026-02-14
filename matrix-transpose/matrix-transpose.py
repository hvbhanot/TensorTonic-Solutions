import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    arr = np.array(A)
    m , n = arr.shape
    transposed_matrix = np.zeros((n,m))

    for i in range(m):
      for j in range(n):
        transposed_matrix[j,i] = arr[i,j]

    return transposed_matrix