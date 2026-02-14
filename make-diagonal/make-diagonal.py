import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """

    n = len(v)
    input_arr = np.array(v)
    if v == 1 : 
      return input_arr

    submission = np.zeros((n,n))

    for i in range(n):
      submission[i,i] = input_arr[i]

    return submission  
