import numpy as np

def sample_var_std(x):
    """
    Returns: dict with 'variance' and 'std_dev' as floats.
    """
    
    std  = np.std(x,ddof=1)
    var = np.var(x,ddof=1)

    return dict( {
        'std_dev' : std,
        'variance' : var
    })