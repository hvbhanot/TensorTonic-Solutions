import numpy as np

def reshape_array(data, operation):
    """
    Returns: ndarray of float64 with shape determined by the operation
    """

    data = np.asarray(data, dtype=float)
     
    if operation == 'flatten':
        return data.flatten()
    elif operation  == 'transpose':
        return data.T
    else:
        m,n = data.shape
        return data.reshape(1, m,n)
      
        