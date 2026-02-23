import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    s = sum(p)
    if not np.isclose(s, 1.0, atol=1e-12):
        raise ValueError("Probabilities do not sum to 1")

    e_x = 0.0
    for i in range(len(x)):
      e_x += x[i] * p[i]

    return e_x
