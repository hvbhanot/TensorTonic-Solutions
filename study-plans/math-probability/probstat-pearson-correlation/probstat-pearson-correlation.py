import numpy as np

def pearson_correlation(X):
    """
    Returns: ndarray, the Pearson correlation matrix.
    """
    X = np.asarray(X,dtype=float)

    p_corr = np.corrcoef(X,rowvar=False) # rowvar : If rowvar is True (default), then each row represents a variable, with observations in the columns. Otherwise, the relationship is transposed: each column represents a variable, while the rows contain observations.

    return p_corr