import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    arr = np.array(A)
    m,n = arr.shape

    if m == n == 1:
      return arr[0,0]

    sum = 0.0

    for i in range(n):
      sum += arr[i,i]

    return sum
