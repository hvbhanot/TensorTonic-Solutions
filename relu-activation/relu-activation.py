import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    if not isinstance(x,list):
      return np.array([max(0,x)])
      
    arr = np.array(x)
    negative = (arr <= 0)
    arr[negative] = 0 
    return arr