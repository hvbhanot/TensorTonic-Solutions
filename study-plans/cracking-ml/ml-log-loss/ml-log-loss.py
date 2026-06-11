import numpy as np

def log_loss(y_true, y_pred):
    """
    Returns: float
    """
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred,dtype=float)

    esp = 1e-15

    y_pred[y_pred == 0] = y_pred[y_pred == 0] + esp
    y_pred[y_pred == 1] = y_pred[y_pred == 1] - esp
     
    loss = -np.mean(y_true * np.log(y_pred) + (1- y_true) * np.log(1 - y_pred))

    return loss