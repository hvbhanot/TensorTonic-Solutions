import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    n = len(y)
    if n == 0:
        return 0.0
    _, counts = np.unique(y, return_counts=True)
    probs = counts / n
    # Filter out zero-prob classes to avoid log2(0)
    probs = probs[probs > 0]
    return -np.sum(probs * np.log2(probs))