import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
  
    e = np.abs(y_true - y_pred)
    
    submission = np.zeros(y_pred.shape[0])

    for i in range(y_pred.shape[0]):
      if e[i] <= delta:
        submission[i] = (e[i]**2)/2
      else:
        submission[i] = delta * ( e[i] - (delta/2) )

    return np.mean(submission)    