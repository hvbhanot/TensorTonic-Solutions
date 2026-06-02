import numpy as np

def vector_projection(u, v):
    """
    Returns: float64 array, the projection of u onto v.
    """

    u = np.asarray(u,dtype=float)
    v = np.asarray(v,dtype=float)

    proj_u_on_v = (np.dot(u,v) / np.dot(v,v)) * v

    return proj_u_on_v