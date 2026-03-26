import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    mean = np.mean(x)
    s = np.std(x, ddof=1)

    t_stat = (mean - mu0) / (s/ np.sqrt(len(x)))
    return t_stat