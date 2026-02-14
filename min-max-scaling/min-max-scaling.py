def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    import numpy as np
    data = np.array(data, dtype=float)

    mins = data.min(axis=0)
    maxs = data.max(axis=0)

    denom = maxs - mins
    denom[denom == 0] = 1 

    submission = (data - mins) / denom
    return submission.tolist()
            
    