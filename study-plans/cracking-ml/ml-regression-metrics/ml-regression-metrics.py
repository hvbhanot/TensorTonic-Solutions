import numpy as np

def regression_metrics(y_true, y_pred):
    """
    Returns: dict with keys "mse", "mae", "r2" rounded to 4 decimal places
    """
    y_pred = np.asarray(y_pred, dtype=float)
    y_true = np.asarray(y_true, dtype=float)

    mse = np.mean((y_true-y_pred)**2)
    mae = np.mean(np.abs(y_true - y_pred))

    mean = np.mean(y_true)

    ss_res = float(np.sum((y_true-y_pred) ** 2))
    ss_tot = float(np.sum((y_true - np.mean(y_true)) ** 2))
    r_2 = 1.0 - ss_res / ss_tot if ss_tot != 0 else 0.0

    output =  {"mse": round(mse,4), "mae": round(mae,4), "r2": round(r_2,4)}


    return output