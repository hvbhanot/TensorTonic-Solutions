import numpy as np

def discrete_moments(values: list, probabilities: list) -> list:
    """
    Returns the first moment, second moment, variance, and standard deviation.
    """

    values = np.asarray(values,dtype=float)
    probabilities = np.asarray(probabilities,dtype=float)

    
    E_X = np.dot(values,probabilities)
    E_X_2 = np.dot(values**2, probabilities)

    Var_X = E_X_2 - pow(E_X,2)
    Std_dev  = np.sqrt(Var_X)

    return [round(E_X,4), round(E_X_2,4), round(Var_X,4), round(Std_dev,4)]