import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    v = np.array(v)
    dims = v.ndim
    if dims == 1:
      norm = np.linalg.norm(v, keepdims=True)
      submission = v / norm
      
    else:  
      norm = np.linalg.norm(v, axis=1)
      norm[norm == 0] = 1  # Fixing the divide issue for zero vectors, avoiding 0/0
      submission = v / norm[:, np.newaxis] 

    return submission
