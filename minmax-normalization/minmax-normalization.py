import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    X = np.array(X,dtype=float)
    mins = np.min(X, axis = axis , keepdims=True) # Preserves dimensions 
    max = np.max(X, axis = axis, keepdims=True)

    scaled = np.zeros(X.shape)
      
    norm = max - mins
    norm[norm==0] = eps 
        
    scaled = (X - mins) / norm

    return scaled
      
  