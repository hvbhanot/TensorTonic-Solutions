import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    n = len(y_pred)
    sum = 0.0
    for i in range(n):
       sum += (y_pred[i] - y_true[i]) **2
    
    return sum/n
