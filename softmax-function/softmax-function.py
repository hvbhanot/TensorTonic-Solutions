import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    x = np.array(x)
    dims = x.ndim
    shape = x.shape
  
    submission = np.zeros(shape)
    
    if dims == 1:
      num = np.exp(x - np.max(x))
      denom = np.sum( np.exp(x - np.max(x)) )

      for i in range(shape[0]):
        submission[i] = num[i] / denom


    else: 

      for i in range(shape[0]):
        num = np.exp(x[i,:] - np.max(x[i,:]))
        denom = np.sum( np.exp(x[i,:] - np.max(x[i,:])) )
      
        for j in range(shape[1]):
          submission[i,j] =  num[j] / denom


    return submission      