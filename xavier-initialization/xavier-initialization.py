import numpy as np

def xavier_initialization(W, fan_in, fan_out):
    """
    Scale raw weights to Xavier uniform initialization.
    """
    
    L = np.sqrt(6/(fan_in+fan_out))
    arr = np.array(W)
    output = arr * (2*L) - L
    return output.tolist()