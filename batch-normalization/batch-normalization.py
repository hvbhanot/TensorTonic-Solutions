import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    x = np.asarray(x, dtype=float)
    gamma = np.asarray(gamma, dtype=float)
    beta = np.asarray(beta, dtype=float)
    
    if x.ndim == 2:
      mean = np.mean(x, axis=0)
      var_x = np.var(x, axis=0)
      x_i = (x-mean) / np.sqrt(var_x + eps)
      y_i = gamma*x_i + beta
      return y_i

    mean = np.mean(x , axis=(0,2,3), keepdims=True) # Keeps in in the (1,x,1,1)
    var_x = np.var(x, axis=(0,2,3) , keepdims=True)

    gamma = gamma.reshape(1, -1, 1, 1)
    beta = beta.reshape(1, -1, 1, 1)
     
    x_i = (x-mean) / np.sqrt(var_x+eps)
    y_i = gamma*x_i + beta

    return y_i
    