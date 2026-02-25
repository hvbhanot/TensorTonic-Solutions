import numpy as np

def one_hot(y, num_classes=None):
    """
    Convert integer labels y ∈ {0,...,K-1} into one-hot matrix of shape (N, K).
    """
    if num_classes == None:
      num_classes = max(y) + 1

    y = np.array(y,dtype=int)
    size = y.shape[0]
    submission = np.zeros((size,num_classes))
    submission[np.arange(size),y] = 1.0
   
    return submission  