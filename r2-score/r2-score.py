import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination).
    """

    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)

    if y_true.shape != y_pred.shape:
        return None

    # constant target case
    if np.all(y_true == y_true[0]):
        if np.array_equal(y_true, y_pred):
            return 1.0
        else:
            return 0.0

    mean = np.mean(y_true)

    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - mean) ** 2)

    r2 = 1 - (ss_res / ss_tot)

    return r2