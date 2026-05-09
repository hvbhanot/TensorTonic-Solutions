import numpy as np

def least_squares(A, b):
    """Returns: float64 array, the solution minimizing ||A @ x - b||^2."""
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    
    return np.linalg.lstsq(A, b, rcond=None)[0] # This function automatically calculates least squares. 


'''
rcond is a float, optional
Cut-off ratio for small singular values of a. For the purposes of rank determination, singular values are treated as zero if they are smaller than rcond times the largest singular value of a. The default uses the machine precision times max(M, N). Passing -1 will use machine precision.
'''    
