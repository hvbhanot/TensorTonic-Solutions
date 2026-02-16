import numpy as np

def relu(x: np.ndarray) -> np.ndarray:
    """ReLU activation: f(x) = max(0, x)"""
  
    less_vals =  (x <= 0)
    x[less_vals] = 0


    return x