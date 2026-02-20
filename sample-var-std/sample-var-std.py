import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    x = np.array(x, dtype=float)

    mean = np.mean(x)

    s_2 = np.sum((x-mean)**2) / (x.shape[0]-1)
    s = np.sqrt(s_2)
    return (s_2,s)