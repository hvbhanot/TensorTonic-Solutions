import numpy as np

def filter_and_extract(data, row_start, row_stop, threshold):
    """
    Returns: 1D ndarray of float64
    """
    data = np.asarray(data,dtype=float)

    output = data[row_start:row_stop]

    output = output[output>threshold]

    return output