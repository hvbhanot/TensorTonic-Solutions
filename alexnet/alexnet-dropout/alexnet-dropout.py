import numpy as np

def dropout(x: np.ndarray, p: float = 0.5, training: bool = True) -> np.ndarray:
    """Apply dropout to input."""
    if training:
        mask = np.random.binomial(1, 1 - p, size=x.shape)
        y = (mask/(1-p)) * x
        return y

    return x