import numpy as np

def dice_loss(p: list, y: list, eps: float = 1e-8) -> float:
    """
    Returns the loss as a float.
    """
    y = np.asarray(y,dtype=float)
    p = np.asarray(p,dtype=float)
    
    p_n = 2.0 * np.sum(p*y) + eps
    p_d = (np.sum(p) + np.sum(y) + eps)

    L = 1.0 - (p_n/p_d)

    return float(L)