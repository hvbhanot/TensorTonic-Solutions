import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Calculating mode manually.
    # Its wrong, need to fix it.
    x = np.array(x)
  
    m = Counter(x).most_common(1)

    return ((np.mean(x)) , (np.median(x)) , m)