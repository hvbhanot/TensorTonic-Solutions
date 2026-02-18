import numpy as np

def selu(x, lam=1.0507009873554804934193349852946, alpha=1.6732632423543772848170429916717):
    """
    Apply SELU activation element-wise.
    Returns a list of floats rounded to 4 decimal places.
    """
    x = np.array(x, dtype=float)

    x[x>0] = x[x>0] * lam
    x[x<=0] = alpha * lam * (np.exp(x[x<=0]) - 1)

    return x
