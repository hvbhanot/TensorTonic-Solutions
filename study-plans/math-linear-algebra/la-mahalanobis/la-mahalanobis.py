import numpy as np

def mahalanobis_distance(x, mean, cov):
    """Returns: float, the Mahalanobis distance from x to the distribution."""
    
    x = np.array(x, dtype=float)
    mean = np.array(mean, dtype=float)
    cov = np.array(cov, dtype=float)
    diff = x - mean
    
    return float(np.sqrt(diff @ np.linalg.inv(cov) @ diff))
