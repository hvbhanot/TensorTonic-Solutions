import numpy as np

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    v = np.array(v)
    w = np.array(w)

    v_norm = np.linalg.norm(v)
    w_norm = np.linalg.norm(w)

    if v_norm == 0 or w_norm == 0:
      return np.nan

    theta = np.arccos( (np.dot(v,w)) / (v_norm*w_norm) )  
    
    return theta