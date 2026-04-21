import torch

def deriv(x):
     return 3*(x**2) + 2

def compute_gradient(values):
    """
    Returns: list of float gradient values dy/dx
    """
    values = torch.tensor(values,dtype=torch.float)
    
    return deriv(values).tolist()
