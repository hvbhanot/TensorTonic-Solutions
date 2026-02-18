import numpy as np
import math # math.erf does not accept vectors only scalers
from scipy.special import erf # This accecpts vectors

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: list or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    if np.isscalar(x): 
      submission = x/2 * ( 1 + erf(x/math.sqrt(2))) 
      return submission 
      
    x = np.array(x) 
    submission = x/2 * ( 1 + erf(x/math.sqrt(2)))

    return submission
