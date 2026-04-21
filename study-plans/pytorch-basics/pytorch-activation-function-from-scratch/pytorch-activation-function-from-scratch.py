import torch

def activate(x, method="relu"):
    """
    Returns: list (activated tensor converted via .tolist())
    """

    x = torch.tensor(x,dtype=torch.float)
    
    if method == 'relu':
        return torch.relu(x).tolist()

    elif method == 'sigmoid':
        return (1/(1 + torch.exp(-x))).tolist()
        
    elif method == 'tanh':
        return torch.tanh(x).tolist()
    else:
        x[x>0] = x[x>0]
        x[x<=0] = 0.01 * x[x<=0]

        return x.tolist()
        