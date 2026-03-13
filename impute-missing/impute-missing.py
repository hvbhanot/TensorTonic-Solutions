import numpy as np

def impute_missing(X, strategy='mean'):
    """
    Fill NaN values in each feature column using column mean or median.
    If an entire column is NaN, fill that column with 0.
    """
    X = np.asarray(X, dtype=float).copy()

    if strategy not in ('mean', 'median'):
        raise ValueError("strategy must be 'mean' or 'median'")

    # 1D case
    if X.ndim == 1:
        if strategy == 'mean':
            stat = np.nanmean(X)
        else:
            stat = np.nanmedian(X)

        if np.isnan(stat):
            stat = 0.0

        X[np.isnan(X)] = stat
        return X

    # 2D case
    if strategy == 'mean':
        stat = np.nanmean(X, axis=0)
    else:
        stat = np.nanmedian(X, axis=0)

    # Replace NaN statistics from all-NaN columns with 0
    stat = np.where(np.isnan(stat), 0.0, stat)

    rows, cols = np.where(np.isnan(X))
    X[rows, cols] = stat[cols]

    return X