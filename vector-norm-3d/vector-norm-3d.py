import numpy as np

def vector_norm_3d(v):
    """
    Compute the Euclidean norm of 3D vector(s).
    """
    v = np.array(v)
    dim = v.ndim
  
    if dim == 1:
      norm = np.linalg.norm(v)
    else:
      norm = np.linalg.norm(v, axis=1)
      
    return norm