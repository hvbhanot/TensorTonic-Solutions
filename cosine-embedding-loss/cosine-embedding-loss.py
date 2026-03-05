import numpy as np
def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """

    x1 = np.asarray(x1, dtype=float)
    x2 = np.asarray(x2, dtype=float)

    n1 = np.linalg.norm(x1)
    n2 = np.linalg.norm(x2)

    cos = np.dot(x1, x2) / (n1 * n2)

    if label == 1:
        loss = 1.0 - cos
    else:
        loss = max(0.0, cos - margin)

    return loss